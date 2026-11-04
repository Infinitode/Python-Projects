"""Advanced sorting algorithms with a built-in benchmark and self-test.

Complements 4_sorting_algorithms.py (bubble/selection/insertion) with the
O(n log n) workhorses plus one non-comparison sort:

* Merge sort    -- stable, O(n log n) time, O(n) extra space
* Quick sort    -- in-place, O(n log n) average, O(log n) call stack
* Heap sort     -- in-place, O(n log n) worst case
* Counting sort -- O(n + k) for non-negative integer keys in a small range

Run with:
    python Intermediate/18_advanced_sorting_algorithms.py
    python Intermediate/18_advanced_sorting_algorithms.py --sizes 100 1000 10000
    python Intermediate/18_advanced_sorting_algorithms.py --algorithms merge quick
    python Intermediate/18_advanced_sorting_algorithms.py --test

Only the Python standard library is used.
"""

import argparse
import random
import sys
import time


class CountedInt(int):
    """An integer that counts every '<' comparison made against it.

    Wrapping the benchmark data in this class lets us measure how many
    element comparisons each algorithm performs without touching the
    sorting code itself.
    """

    comparisons = 0

    def __lt__(self, other):
        CountedInt.comparisons += 1
        return int(self) < int(other)


def merge_sort(arr):
    """Sort arr in place with merge sort (stable, O(n log n)).

    The list is split in half, each half is sorted recursively, and the
    two sorted halves are merged back into arr. Ties take the left element
    first, which is what makes the sort stable.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    for k in range(len(arr)):
        # Take from the left half unless the right element is strictly
        # smaller (taking left on ties preserves the original order).
        if j >= len(right) or (i < len(left) and not right[j] < left[i]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    return arr


def quick_sort(arr):
    """Sort arr in place with quick sort (Hoare partition, median-of-three).

    Two classic safeguards keep the worst case away on typical data:
    * the pivot is the median of the first, middle, and last elements,
      so already-sorted input does not degrade to O(n^2);
    * recursion always descends into the smaller partition while the
      larger one is handled by the loop, bounding the stack to O(log n).
    """

    def partition(lo, hi):
        mid = (lo + hi) // 2
        # Order arr[lo] <= arr[mid] <= arr[hi] and pivot on the median.
        if arr[mid] < arr[lo]:
            arr[mid], arr[lo] = arr[lo], arr[mid]
        if arr[hi] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]
        if arr[hi] < arr[mid]:
            arr[hi], arr[mid] = arr[mid], arr[hi]
        pivot = arr[mid]

        # Hoare partition: two scanners walk toward each other, swapping
        # out-of-place pairs until they cross.
        i, j = lo - 1, hi + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while pivot < arr[j]:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def sort_range(lo, hi):
        while lo < hi:
            p = partition(lo, hi)
            if p - lo < hi - p:
                sort_range(lo, p)
                lo = p + 1
            else:
                sort_range(p + 1, hi)
                hi = p

    sort_range(0, len(arr) - 1)
    return arr


def heap_sort(arr):
    """Sort arr in place with heap sort (O(n log n) worst case).

    Phase 1 rearranges arr into a max-heap with sift-down. Phase 2
    repeatedly swaps the largest element to the end and repairs the
    shrinking heap.
    """
    n = len(arr)

    def sift_down(root, end):
        """Push arr[root] down until the max-heap property holds again."""
        while True:
            child = 2 * root + 1
            if child > end:
                break
            # Point at the larger of the two children.
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    # Build the max-heap bottom-up (leaves are already valid heaps).
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n - 1)

    # Extract the maximum n - 1 times.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end - 1)
    return arr


def counting_sort(arr):
    """Sort arr in place with counting sort (non-negative integers only).

    Instead of comparing elements, each value is used as an index into a
    tally array. This runs in O(n + k) for keys 0..k, which beats every
    comparison sort when k is small -- but it needs O(k) memory, so it is
    the wrong tool for sparse or huge keys.
    """
    if not arr:
        return arr
    if any(not isinstance(value, int) or value < 0 for value in arr):
        raise ValueError("counting sort requires non-negative integers")

    high = max(arr)
    counts = [0] * (high + 1)
    for value in arr:
        counts[value] += 1

    index = 0
    for value, count in enumerate(counts):
        for _ in range(count):
            arr[index] = value
            index += 1
    return arr


ALGORITHMS = {
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "counting": counting_sort,
}


def run_self_test():
    """Check every algorithm against sorted() on a set of edge cases."""
    rng = random.Random(1234)
    cases = [
        [],
        [1],
        [2, 1],
        [7, 7, 7, 7],
        [3, -1, 0, -5, 9, 2],
        list(range(50)),
        list(range(50))[::-1],
        [rng.randrange(100) for _ in range(200)],
    ]
    # Counting sort only accepts non-negative integers.
    counting_cases = [[v for v in case if v >= 0] for case in cases]

    for name, sort_func in ALGORITHMS.items():
        test_cases = counting_cases if name == "counting" else cases
        for case in test_cases:
            result = sort_func(list(case))
            assert result == sorted(case), "{} failed on {!r}".format(name, case)

    # Merge sort must be stable: equal keys keep their original order.
    tagged = [(1, "a"), (0, "b"), (1, "c"), (0, "d"), (1, "e")]
    assert merge_sort(list(tagged)) == [(0, "b"), (0, "d"), (1, "a"), (1, "c"), (1, "e")]

    # Counting sort must reject invalid keys.
    try:
        counting_sort([1, -2, 3])
    except ValueError:
        pass
    else:
        raise AssertionError("counting sort accepted a negative key")

    print("All self-tests passed ({} algorithms).".format(len(ALGORITHMS)))


def run_demo():
    """Show each algorithm sorting the same small list."""
    data = [38, 27, 43, 3, 9, 82, 10, 27, 1, 56]
    print("--- Advanced Sorting Algorithms demo ---")
    print("Original list: {}\n".format(data))
    for name, sort_func in ALGORITHMS.items():
        result = sort_func(list(data))
        print("{:>9} sort: {}".format(name.capitalize(), result))
    print()


def run_benchmark(sizes, seed, names):
    """Time each algorithm and count its element comparisons."""
    rng = random.Random(seed)
    print("--- Benchmark (random integers 0..9999) ---")
    header = "{:>6}  {:>9}  {:>12}  {:>12}  {:>8}".format(
        "n", "algorithm", "time (ms)", "comparisons", "correct"
    )
    print(header)
    print("-" * len(header))

    for size in sizes:
        data = [rng.randrange(10000) for _ in range(size)]
        expected = sorted(data)
        for name in names:
            counted = [CountedInt(value) for value in data]
            CountedInt.comparisons = 0
            start = time.perf_counter()
            result = ALGORITHMS[name](counted)
            elapsed_ms = (time.perf_counter() - start) * 1000.0
            correct = "yes" if list(result) == expected else "NO!"
            # Counting sort never compares two elements; it uses keys as
            # array indices, so a comparison count is not meaningful.
            comparisons = (
                "n/a" if name == "counting" else str(CountedInt.comparisons)
            )
            print(
                "{:>6}  {:>9}  {:>12.2f}  {:>12}  {:>8}".format(
                    size, name, elapsed_ms, comparisons, correct
                )
            )
        print()
    print("Tip: compare these numbers with the O(n^2) sorts in 4_sorting_algorithms.py.")


def main():
    parser = argparse.ArgumentParser(
        description="Advanced sorting algorithms with benchmarking and self-tests."
    )
    parser.add_argument(
        "--sizes", nargs="+", type=int, default=[100, 1000, 5000],
        help="list sizes for the benchmark (default: 100 1000 5000)",
    )
    parser.add_argument(
        "--algorithms", nargs="+", choices=sorted(ALGORITHMS),
        default=sorted(ALGORITHMS),
        help="which algorithms to run (default: all)",
    )
    parser.add_argument("--seed", type=int, default=None, help="random seed for reproducible benchmarks")
    parser.add_argument("--test", action="store_true", help="run correctness self-tests and exit")
    parser.add_argument("--no-demo", action="store_true", help="skip the small worked example")
    args = parser.parse_args()

    if args.test:
        run_self_test()
        return 0

    if any(size < 0 for size in args.sizes):
        parser.error("--sizes values must be non-negative")

    if not args.no_demo:
        run_demo()
    run_benchmark(args.sizes, args.seed, args.algorithms)
    return 0


if __name__ == "__main__":
    sys.exit(main())
