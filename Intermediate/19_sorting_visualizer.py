"""Watch sorting algorithms work as an animated bar chart in the terminal.

Each sorting algorithm is written as a *generator*: it mutates the list
and yields the indices it just touched, pausing after every step. The
animation loop simply renders one frame per yield, which keeps the
sorting logic completely separate from the drawing code.

Run with:
    python Intermediate/19_sorting_visualizer.py
    python Intermediate/19_sorting_visualizer.py --algorithm quick --size 40
    python Intermediate/19_sorting_visualizer.py --algorithm merge --delay 0.01
    python Intermediate/19_sorting_visualizer.py --list

Animation needs a real terminal (ANSI escape codes, supported by Linux,
macOS, and Windows 10+). When output is redirected to a file or pipe, the
script prints a static final chart and step counts instead.

Only the Python standard library is used.
"""

import argparse
import os
import random
import sys
import time

BAR = "██"
RESET = "\x1b[0m"
YELLOW = "\x1b[33m"
GREEN = "\x1b[32m"
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
HOME = "\x1b[H"
CLEAR_BELOW = "\x1b[J"


# ---------------------------------------------------------------------------
# Sorting algorithms as step generators.
# Each generator sorts `arr` in place and yields the indices it just touched.
# ---------------------------------------------------------------------------

def bubble_sort_steps(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield (j, j + 1)
        if not swapped:
            break


def insertion_sort_steps(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            yield (j + 1, j + 2)
        arr[j + 1] = key
        yield (j + 1,)


def selection_sort_steps(arr):
    n = len(arr)
    for i in range(n):
        best = i
        for j in range(i + 1, n):
            if arr[j] < arr[best]:
                best = j
                yield (best, i)
        if best != i:
            arr[i], arr[best] = arr[best], arr[i]
            yield (i, best)


def quick_sort_steps(arr):
    """Lomuto quick sort: the last element is the pivot each round."""

    def sort_range(lo, hi):
        if lo >= hi:
            return
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield (i, j)
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        yield (i, hi)
        # `yield from` forwards every step of the recursive calls.
        yield from sort_range(lo, i - 1)
        yield from sort_range(i + 1, hi)

    yield from sort_range(0, len(arr) - 1)


def merge_sort_steps(arr):
    """Top-down merge sort that reports every write back into arr."""

    def sort_range(lo, hi):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        yield from sort_range(lo, mid)
        yield from sort_range(mid, hi)

        left = arr[lo:mid]
        right = arr[mid:hi]
        i = j = 0
        for k in range(lo, hi):
            if j >= len(right) or (i < len(left) and not right[j] < left[i]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            yield (k,)

    yield from sort_range(0, len(arr))


ALGORITHMS = {
    "bubble": bubble_sort_steps,
    "insertion": insertion_sort_steps,
    "selection": selection_sort_steps,
    "quick": quick_sort_steps,
    "merge": merge_sort_steps,
}


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_frame(arr, highlights, height, step, name, color, highlight_color=YELLOW):
    """Build one full frame of the bar chart as a single string."""
    peak = max(arr) if arr else 1
    lines = ["{} -- step {}".format(name.capitalize(), step)]
    for row in range(height, 0, -1):
        cells = []
        for index, value in enumerate(arr):
            bar_height = max(1, round(value * height / peak)) if value > 0 else 0
            if bar_height >= row:
                cell = BAR
                if color and index in highlights:
                    cell = highlight_color + BAR + RESET
            else:
                cell = "  "
            cells.append(cell)
        lines.append("".join(cells))
    return "\n".join(lines)


def animate(arr, algorithm, name, delay, height, color):
    """Run the generator, drawing one frame per yielded step."""
    steps = ALGORITHMS[algorithm](arr)
    # Clear the screen once and hide the cursor for flicker-free frames.
    sys.stdout.write("\x1b[2J" + HIDE_CURSOR)
    step = 0
    try:
        for highlights in steps:
            step += 1
            frame = render_frame(arr, highlights, height, step, name, color)
            # HOME + frame + CLEAR_BELOW redraws in place without flicker.
            sys.stdout.write(HOME + frame + CLEAR_BELOW)
            sys.stdout.flush()
            time.sleep(delay)
        # Final frame: everything green to signal "sorted".
        frame = render_frame(
            arr, set(range(len(arr))), height, step, name, color, GREEN
        )
        sys.stdout.write(HOME + frame + CLEAR_BELOW + "\n")
        sys.stdout.flush()
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()
    return step


def static_report(arr, algorithm, name):
    """Fallback for non-terminal output: run to completion, print a summary."""
    steps = 0
    for _ in ALGORITHMS[algorithm](arr):
        steps += 1
    print("{} sort finished in {} steps.".format(name.capitalize(), steps))
    print("Sorted values: {}".format(arr))
    print("(Run in a real terminal to watch the animation.)")
    return steps


def main():
    parser = argparse.ArgumentParser(
        description="Animated terminal visualizer for classic sorting algorithms."
    )
    parser.add_argument(
        "--algorithm", choices=sorted(ALGORITHMS), default="bubble",
        help="algorithm to animate (default: bubble)",
    )
    parser.add_argument("--size", type=int, default=30, help="number of bars (default: 30)")
    parser.add_argument("--height", type=int, default=14, help="chart height in rows (default: 14)")
    parser.add_argument("--delay", type=float, default=0.03, help="seconds between frames (default: 0.03)")
    parser.add_argument("--seed", type=int, default=None, help="random seed for a reproducible shuffle")
    parser.add_argument("--no-color", action="store_true", help="disable ANSI colors")
    parser.add_argument("--list", action="store_true", help="list available algorithms and exit")
    args = parser.parse_args()

    if args.list:
        print("Available algorithms: {}".format(", ".join(sorted(ALGORITHMS))))
        return 0
    if args.size < 2:
        parser.error("--size must be at least 2")
    if args.height < 3:
        parser.error("--height must be at least 3")
    if args.delay < 0:
        parser.error("--delay cannot be negative")

    rng = random.Random(args.seed)
    arr = list(range(1, args.size + 1))
    rng.shuffle(arr)

    # On Windows, this no-op system call enables ANSI escape processing
    # in the classic console.
    if os.name == "nt":
        os.system("")

    interactive = sys.stdout.isatty()
    color = interactive and not args.no_color

    try:
        if interactive:
            animate(arr, args.algorithm, args.algorithm, args.delay, args.height, color)
            print("Sorted {} values with {} sort.".format(args.size, args.algorithm))
        else:
            static_report(arr, args.algorithm, args.algorithm)
    except KeyboardInterrupt:
        sys.stdout.write(SHOW_CURSOR + "\n")
        print("Interrupted -- animation stopped.")
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
