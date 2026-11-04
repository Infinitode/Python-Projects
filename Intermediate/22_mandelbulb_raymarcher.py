"""Render the Mandelbulb, a 3D fractal, with a pure-Python ray marcher.

The Mandelbulb (White & Nylander, 2009) generalizes the Mandelbrot set's
z -> z^2 + c iteration into three dimensions. A point (x, y, z) is read
in spherical coordinates, its radius is raised to a power (usually 8)
and its angles are multiplied by that power, then the original point is
added back -- exactly like squaring a complex number, but in 3D.

Because the shape has no simple surface formula, we render it with
*ray marching*: for every pixel a ray is shot from the camera, and a
*distance estimator* tells us how far we can safely jump without
crossing the fractal surface. When the remaining distance is tiny, the
ray has hit the bulb and we shade the point using an estimated normal.

Run with:
    python Intermediate/22_mandelbulb_raymarcher.py
    python Intermediate/22_mandelbulb_raymarcher.py --output bulb.png --width 400 --height 260
    python Intermediate/22_mandelbulb_raymarcher.py --power 5 --angle 80 --output bulb5.png
    python Intermediate/22_mandelbulb_raymarcher.py --width 100 --height 64 --no-ascii

Rendering is pure Python and takes a few seconds for the terminal
preview and longer for big PNG images -- start small, then scale up.
Only the Python standard library is used (math, zlib, struct).
"""

import argparse
import math
import struct
import sys
import time
import zlib

ASCII_RAMP = " .:-=+*#%@"
BACKGROUND_TOP = (0.05, 0.08, 0.16)
BACKGROUND_BOTTOM = (0.015, 0.02, 0.06)
BULB_COLOR = (1.0, 0.87, 0.68)
BOUNDING_RADIUS = 1.5  # the whole bulb fits inside this sphere


# ---------------------------------------------------------------------------
# The fractal itself
# ---------------------------------------------------------------------------

def mandelbulb_de(px, py, pz, power, iterations, bailout=2.0):
    """Distance estimate from (px, py, pz) to the Mandelbulb surface.

    Iterate z -> z^power + c in spherical coordinates while tracking dr,
    the running derivative of the radius. The classic estimate
    0.5 * log(r) * r / dr is a safe lower bound on the distance, which is
    what lets rays jump through empty space without missing the surface.
    """
    x, y, z = px, py, pz
    dr = 1.0
    r = 0.0
    for _ in range(iterations):
        r = math.sqrt(x * x + y * y + z * z)
        if r > bailout:
            break
        if r < 1e-12:
            return 0.0  # essentially at the origin, deep inside the set

        theta = math.acos(z / r) * power
        phi = math.atan2(y, x) * power
        zr = r ** power
        # dr = power * r^(power-1) * dr + 1, reusing zr to save a pow().
        dr = (zr / r) * power * dr + 1.0

        sin_theta = math.sin(theta)
        x, y, z = (
            zr * sin_theta * math.cos(phi) + px,
            zr * sin_theta * math.sin(phi) + py,
            zr * math.cos(theta) + pz,
        )
    return 0.5 * math.log(r) * r / dr


def surface_normal(px, py, pz, power, iterations, h=0.0005):
    """Estimate the surface normal from four distance samples.

    The gradient of the distance field points away from the surface;
    sampling it at the corners of a tiny tetrahedron is a cheap way to
    approximate it with only four extra evaluations.
    """
    offsets = ((1, -1, -1), (-1, -1, 1), (-1, 1, -1), (1, 1, 1))
    nx = ny = nz = 0.0
    for ox, oy, oz in offsets:
        d = mandelbulb_de(px + h * ox, py + h * oy, pz + h * oz, power, iterations)
        nx += ox * d
        ny += oy * d
        nz += oz * d
    length = math.sqrt(nx * nx + ny * ny + nz * nz)
    if length < 1e-12:
        return (0.0, 0.0, 1.0)
    return (nx / length, ny / length, nz / length)


# ---------------------------------------------------------------------------
# Ray marching and shading
# ---------------------------------------------------------------------------

def normalize(vx, vy, vz):
    length = math.sqrt(vx * vx + vy * vy + vz * vz)
    return (vx / length, vy / length, vz / length)


def march_ray(cam, direction, power, iterations, max_steps, t_start, t_end):
    """March along a ray; return (hit_distance, steps, closest_approach)."""
    cx, cy, cz = cam
    dx, dy, dz = direction
    t = t_start
    closest = float("inf")
    for step in range(max_steps):
        d = mandelbulb_de(cx + dx * t, cy + dy * t, cz + dz * t, power, iterations)
        if d < closest:
            closest = d
        if d < max(0.0002, 0.0006 * t):
            return t, step + 1, closest
        t += d * 0.85  # slightly under-jump: the estimate is not exact
        if t > t_end:
            break
    return None, max_steps, closest


def shade(px, py, pz, steps, max_steps, power, iterations):
    """Diffuse lighting plus a cheap step-count ambient occlusion."""
    nx, ny, nz = surface_normal(px, py, pz, power, iterations)
    lx, ly, lz = normalize(0.55, 0.65, 0.85)
    diffuse = max(0.0, nx * lx + ny * ly + nz * lz)
    # A dim fill light from the opposite side keeps shadows readable.
    fill = max(0.0, -(nx * lx + ny * ly + nz * lz)) * 0.18
    # Rays that needed many steps to land sit in crevices -> darker.
    occlusion = max(0.25, 1.0 - 0.75 * steps / max_steps)
    brightness = (0.12 + 0.95 * diffuse + fill) * occlusion
    return tuple(channel * brightness for channel in BULB_COLOR)


def render(width, height, power, iterations, max_steps, angle, elevation, zoom,
           progress=True):
    """Render the bulb into a width x height buffer of (r, g, b) floats."""
    ang = math.radians(angle)
    elev = math.radians(max(-89.0, min(89.0, elevation)))
    distance = 3.2 / zoom
    cam = (
        distance * math.cos(elev) * math.cos(ang),
        distance * math.cos(elev) * math.sin(ang),
        distance * math.sin(elev),
    )
    forward = normalize(-cam[0], -cam[1], -cam[2])
    # Camera basis with the world z axis as "up":
    # right = forward x (0, 0, 1), then up = right x forward.
    right = normalize(forward[1], -forward[0], 0.0)
    up = (
        right[1] * forward[2] - right[2] * forward[1],
        right[2] * forward[0] - right[0] * forward[2],
        right[0] * forward[1] - right[1] * forward[0],
    )
    aspect = width / height
    fov = 0.42  # tan(half field of view); the bulb comfortably fills the frame
    cam_sq = cam[0] ** 2 + cam[1] ** 2 + cam[2] ** 2

    buffer = []
    report_every = max(1, height // 10)
    for row in range(height):
        v = (1.0 - 2.0 * (row + 0.5) / height) * fov
        for col in range(width):
            u = (2.0 * (col + 0.5) / width - 1.0) * fov * aspect
            direction = normalize(
                forward[0] + right[0] * u + up[0] * v,
                forward[1] + right[1] * u + up[1] * v,
                forward[2] + right[2] * u + up[2] * v,
            )

            # Intersect the bounding sphere first so empty corners cost
            # almost nothing. b = dot(cam, dir); c = |cam|^2 - R^2.
            b = cam[0] * direction[0] + cam[1] * direction[1] + cam[2] * direction[2]
            c = cam_sq - BOUNDING_RADIUS ** 2
            discriminant = b * b - c
            if discriminant < 0.0:
                buffer.append(background_color(row, height))
                continue
            root = math.sqrt(discriminant)
            t_start = max(0.0, -b - root)
            t_end = -b + root

            hit, steps, closest = march_ray(
                cam, direction, power, iterations, max_steps, t_start, t_end
            )
            if hit is None:
                color = background_color(row, height)
                # A faint glow where rays only just missed the surface.
                glow = max(0.0, 1.0 - closest / 0.06) * 0.30
                color = tuple(
                    channel + glow * 0.4 for channel in color
                )
            else:
                color = shade(
                    cam[0] + direction[0] * hit,
                    cam[1] + direction[1] * hit,
                    cam[2] + direction[2] * hit,
                    steps, max_steps, power, iterations,
                )
            buffer.append(color)
        if progress and (row + 1) % report_every == 0:
            percent = 100 * (row + 1) // height
            print("  rendering... {}%".format(percent), file=sys.stderr)
    return buffer


def background_color(row, height):
    """Vertical gradient from deep navy to a slightly lighter horizon."""
    blend = row / max(1, height - 1)
    return tuple(
        top + (bottom - top) * blend
        for top, bottom in zip(BACKGROUND_TOP, BACKGROUND_BOTTOM)
    )


# ---------------------------------------------------------------------------
# Output: PNG writer and ASCII preview (no third-party libraries)
# ---------------------------------------------------------------------------

def write_png(filename, width, height, buffer):
    """Write an 8-bit RGB PNG using only zlib and struct.

    PNG files are a signature plus 'chunks'; each chunk carries its
    length, a 4-byte type, the data, and a CRC32 checksum. Image rows
    are prefixed with filter byte 0 (no filtering) before compression.
    """

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    raw = bytearray()
    for color in buffer:
        raw.extend(
            int(255 * max(0.0, min(1.0, channel)) ** (1.0 / 2.2))
            for channel in color
        )
    stride = width * 3
    scanlines = b"".join(
        b"\x00" + bytes(raw[y * stride:(y + 1) * stride]) for y in range(height)
    )
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(scanlines, 9))
        + chunk(b"IEND", b"")
    )
    with open(filename, "wb") as handle:
        handle.write(png)


def ascii_preview(buffer, width, height, columns):
    """Downsample the rendered image into ASCII art for the terminal."""
    # Terminal characters are roughly twice as tall as they are wide.
    rows = max(1, round(columns * height / width / 2))
    lines = []
    for r in range(rows):
        line = []
        for c in range(columns):
            # Average the luma of the pixel block behind this character.
            x0 = c * width // columns
            x1 = max(x0 + 1, (c + 1) * width // columns)
            y0 = r * height // rows
            y1 = max(y0 + 1, (r + 1) * height // rows)
            total = 0
            for y in range(y0, y1):
                for x in range(x0, x1):
                    red, green, blue = buffer[y * width + x]
                    total += 0.299 * red + 0.587 * green + 0.114 * blue
            luma = total / ((x1 - x0) * (y1 - y0))
            index = int(max(0.0, min(1.0, luma)) * (len(ASCII_RAMP) - 1))
            line.append(ASCII_RAMP[index])
        lines.append("".join(line))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Render the Mandelbulb 3D fractal with a pure-Python ray marcher."
    )
    parser.add_argument("--width", type=int, default=240, help="image width in pixels (default: 240)")
    parser.add_argument("--height", type=int, default=150, help="image height in pixels (default: 150)")
    parser.add_argument("--power", type=float, default=8.0, help="Mandelbulb power, 2-20 (default: 8)")
    parser.add_argument("--iterations", type=int, default=10, help="fractal iterations per sample (default: 10)")
    parser.add_argument("--steps", type=int, default=90, help="max ray-march steps (default: 90)")
    parser.add_argument("--angle", type=float, default=35.0, help="camera orbit angle in degrees (default: 35)")
    parser.add_argument("--elevation", type=float, default=18.0, help="camera elevation in degrees (default: 18)")
    parser.add_argument("--zoom", type=float, default=1.0, help="camera zoom factor (default: 1.0)")
    parser.add_argument("--output", metavar="FILE", help="save the render as a PNG image")
    parser.add_argument("--no-ascii", action="store_true", help="skip the terminal ASCII preview")
    parser.add_argument("--ascii-width", type=int, default=78, help="ASCII preview width (default: 78)")
    args = parser.parse_args()

    if args.width < 8 or args.height < 8:
        parser.error("--width and --height must be at least 8")
    if not 2.0 <= args.power <= 20.0:
        parser.error("--power must be between 2 and 20")
    if not 1 <= args.iterations <= 30:
        parser.error("--iterations must be between 1 and 30")
    if not 10 <= args.steps <= 500:
        parser.error("--steps must be between 10 and 500")
    if not 0.2 <= args.zoom <= 5.0:
        parser.error("--zoom must be between 0.2 and 5")
    if args.ascii_width < 20:
        parser.error("--ascii-width must be at least 20")

    print(
        "Rendering Mandelbulb (power {}, {} x {} pixels)...".format(
            args.power, args.width, args.height
        ),
        file=sys.stderr,
    )
    start = time.perf_counter()
    buffer = render(
        args.width, args.height, args.power, args.iterations, args.steps,
        args.angle, args.elevation, args.zoom,
    )
    elapsed = time.perf_counter() - start
    print("Rendered in {:.1f} s.".format(elapsed), file=sys.stderr)

    if args.output:
        write_png(args.output, args.width, args.height, buffer)
        print("Saved PNG to {}".format(args.output), file=sys.stderr)

    if not args.no_ascii:
        try:
            print(ascii_preview(buffer, args.width, args.height, args.ascii_width))
        except UnicodeEncodeError:
            print("(ASCII preview skipped: this console cannot display it.)")
    elif not args.output:
        print("Nothing to show: pass --output FILE.png or drop --no-ascii.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
