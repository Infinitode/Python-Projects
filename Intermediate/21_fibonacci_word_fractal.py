"""Draw the Fibonacci word fractal -- a fractal grown from the Fibonacci sequence.

The Fibonacci *word* is built like the Fibonacci numbers, but with strings:

    S(0) = "0"
    S(1) = "01"
    S(n) = S(n-1) + S(n-2)      (concatenation instead of addition)

Its lengths are exactly the Fibonacci numbers: 1, 2, 3, 5, 8, 13, 21, ...
Reading the word as turtle-graphics instructions produces a self-similar
curve called the Fibonacci word fractal:

    * every digit draws one unit segment forward;
    * on a "0" the turtle turns 90 degrees -- left on even positions,
      right on odd positions;
    * on a "1" the turtle keeps going straight.

Run with:
    python Intermediate/21_fibonacci_word_fractal.py
    python Intermediate/21_fibonacci_word_fractal.py --iterations 16 --width 120
    python Intermediate/21_fibonacci_word_fractal.py --svg fibonacci.svg
    python Intermediate/21_fibonacci_word_fractal.py --png fibonacci.png
    python Intermediate/21_fibonacci_word_fractal.py --word

The terminal preview uses two characters per cell so the curve keeps its
proportions; --svg writes a crisp vector image you can open in a browser,
and --png writes a raster image with thin strokes (tune with --stroke and
--png-width) so the fractal is clear outside the terminal.
Only the Python standard library is used.
"""

import argparse
import struct
import sys
import zlib


def fibonacci_word(n):
    """Return the n-th Fibonacci word (S(0) = '0', S(1) = '01')."""
    if n < 0:
        raise ValueError("n must be non-negative")
    previous, current = "0", "01"
    if n == 0:
        return previous
    for _ in range(n - 1):
        previous, current = current, current + previous
    return current


def fractal_path(word):
    """Turn a Fibonacci word into a list of (x, y) turtle positions.

    Headings are 0=east, 1=north, 2=west, 3=south, so turning left is +1
    and turning right is -1 (mod 4). y grows upward, like in math class.
    """
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    x = y = 0
    heading = 0
    points = [(x, y)]
    for index, digit in enumerate(word):
        x += dx[heading]
        y += dy[heading]
        points.append((x, y))
        if digit == "0":
            turn = 1 if index % 2 == 0 else -1
            heading = (heading + turn) % 4
    return points


def path_bounds(points):
    """Return (min_x, min_y, max_x, max_y) of a path."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), min(ys), max(xs), max(ys)


def choose_iterations(max_width, max_height):
    """Pick the largest iteration whose curve fits the requested box.

    Terminal cells are about twice as tall as they are wide, and the
    preview draws each cell with two characters, so a curve W cells wide
    needs 2*W characters.
    """
    best = 1
    for n in range(1, 25):
        points = fractal_path(fibonacci_word(n))
        min_x, min_y, max_x, max_y = path_bounds(points)
        width_chars = 2 * (max_x - min_x + 1)
        height_lines = max_y - min_y + 1
        if width_chars > max_width or height_lines > max_height:
            break
        best = n
    return best


def render_ascii(points, plain=False):
    """Rasterize the turtle path into a string of block characters."""
    min_x, min_y, max_x, max_y = path_bounds(points)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [["  "] * width for _ in range(height)]
    ink = "##" if plain else "██"
    for x, y in points:
        # Flip y so north is at the top of the terminal.
        grid[max_y - y][x - min_x] = ink
    return "\n".join("".join(row).rstrip() for row in grid)


def save_svg(points, filename, scale=10, stroke="#1b2a4a"):
    """Write the curve as an SVG polyline (pure standard library)."""
    min_x, min_y, max_x, max_y = path_bounds(points)
    padding = scale
    width = (max_x - min_x) * scale + 2 * padding
    height = (max_y - min_y) * scale + 2 * padding
    # SVG's y axis points down, so mirror the turtle's y coordinate.
    coords = " ".join(
        "{},{}".format((x - min_x) * scale + padding, (max_y - y) * scale + padding)
        for x, y in points
    )
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        'viewBox="0 0 {w} {h}">\n'
        '  <rect width="{w}" height="{h}" fill="white"/>\n'
        '  <polyline points="{coords}" fill="none" stroke="{stroke}" '
        'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>\n'
        '</svg>\n'
    ).format(w=width, h=height, coords=coords, stroke=stroke, sw=max(1, scale // 5))
    with open(filename, "w", encoding="utf-8") as handle:
        handle.write(svg)


def print_word_table(limit):
    """Show how the word lengths reproduce the Fibonacci numbers."""
    print(" n   len(S(n))   word (first 40 digits)")
    print("----------------------------------------")
    for n in range(limit + 1):
        word = fibonacci_word(n)
        preview = word if len(word) <= 40 else word[:40] + "..."
        print("{:>2}   {:>9}   {}".format(n, len(word), preview))
    print("\nThe lengths 1, 2, 3, 5, 8, 13, ... are the Fibonacci numbers --")
    print("the same sequence as Beginner project 21, now drawing a fractal.")


def _write_png(filename, width, height, pixels):
    """Write an 8-bit RGB PNG from a flat row-major list of (r, g, b) tuples."""

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    raw = bytearray()
    for rgb in pixels:
        raw.extend(rgb)
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


def save_png(points, filename, target_width=1000, stroke=2):
    """Rasterize the curve to a PNG with thin strokes so the fractal stays crisp."""
    min_x, min_y, max_x, max_y = path_bounds(points)
    span_x = max(1, max_x - min_x)
    span_y = max(1, max_y - min_y)
    scale = target_width / span_x
    pad = 20
    width = int(span_x * scale) + pad * 2
    height = int(span_y * scale) + pad * 2
    pixels = [(250, 250, 252)] * (width * height)

    def rect(x0, y0, x1, y1, color):
        for y in range(max(0, y0), min(height, y1)):
            for x in range(max(0, x0), min(width, x1)):
                pixels[y * width + x] = color

    def to_px(x, y):
        return (int(pad + (x - min_x) * scale), int(pad + (max_y - y) * scale))

    ink = (27, 42, 74)
    half = max(1, stroke // 2)
    for (ax, ay), (bx, by) in zip(points, points[1:]):
        x0, y0 = to_px(ax, ay)
        x1, y1 = to_px(bx, by)
        rect(min(x0, x1) - half, min(y0, y1) - half,
             max(x0, x1) + half + 1, max(y0, y1) + half + 1, ink)
    _write_png(filename, width, height, pixels)


def main():
    parser = argparse.ArgumentParser(
        description="Draw the Fibonacci word fractal in the terminal or as SVG."
    )
    parser.add_argument(
        "--iterations", type=int, default=None,
        help="word index to draw (default: largest that fits the preview box)",
    )
    parser.add_argument("--width", type=int, default=100, help="max preview width in characters (default: 100)")
    parser.add_argument("--height", type=int, default=40, help="max preview height in lines (default: 40)")
    parser.add_argument("--svg", metavar="FILE", help="also save the curve as an SVG image")
    parser.add_argument("--png", metavar="FILE", help="also save the curve as a PNG image")
    parser.add_argument("--stroke", type=int, default=2, help="PNG stroke width in pixels (default: 2)")
    parser.add_argument("--png-width", type=int, default=1000, help="target PNG width in pixels (default: 1000)")
    parser.add_argument("--plain", action="store_true", help="use '#' instead of block characters")
    parser.add_argument("--word", action="store_true", help="print the Fibonacci words and their lengths")
    args = parser.parse_args()

    if args.iterations is not None and args.iterations < 1:
        parser.error("--iterations must be at least 1")
    if args.width < 10 or args.height < 5:
        parser.error("--width must be >= 10 and --height must be >= 5")
    if args.stroke < 1:
        parser.error("--stroke must be at least 1")
    if args.png_width < 100:
        parser.error("--png-width must be at least 100")

    n = args.iterations if args.iterations is not None else choose_iterations(args.width, args.height)
    word = fibonacci_word(n)
    points = fractal_path(word)

    print("=== Fibonacci Word Fractal ===")
    print("S({}) has {} digits (a Fibonacci number!).".format(n, len(word)))
    print("Drawing rule: every digit steps forward; '0' turns (left on even")
    print("positions, right on odd), '1' goes straight.\n")

    if args.word:
        print_word_table(min(n, 12))
        print()

    min_x, min_y, max_x, max_y = path_bounds(points)
    print(
        "Curve bounds: {} x {} cells\n".format(max_x - min_x + 1, max_y - min_y + 1)
    )
    try:
        print(render_ascii(points, plain=args.plain))
    except UnicodeEncodeError:
        # Some legacy consoles cannot print block characters.
        print(render_ascii(points, plain=True))

    if args.svg:
        save_svg(points, args.svg)
        print("\nSaved vector image to {}".format(args.svg))
    if args.png:
        save_png(points, args.png, target_width=args.png_width, stroke=args.stroke)
        print("Saved PNG image to {}".format(args.png))
    if not args.svg and not args.png:
        print("\nTip: add --svg fibonacci.svg or --png fibonacci.png to save a crisp image.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
