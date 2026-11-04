"""Generate a random maze, then solve it with BFS, DFS, and A*.

The maze is a "perfect" maze (exactly one path between any two cells),
carved with the recursive backtracker algorithm. Three classic graph
searches then race to find the exit:

* BFS -- breadth-first search, guarantees a shortest path
* DFS -- depth-first search, finds *a* path (often a long, winding one)
* A*  -- best-first search with a Manhattan-distance heuristic,
         shortest path like BFS but usually exploring far fewer cells

Run with:
    python Intermediate/20_maze_generator_solver.py
    python Intermediate/20_maze_generator_solver.py --width 20 --height 10 --seed 7
    python Intermediate/20_maze_generator_solver.py --algorithm astar
    python Intermediate/20_maze_generator_solver.py --test

Legend: '#' wall, '.' solution path, 'S' start, 'E' exit.
Only the Python standard library is used.
"""

import argparse
import heapq
import random
import sys
import time
from collections import deque

WALL = "#"
OPEN = " "
PATH = "."
START = "S"
END = "E"


# ---------------------------------------------------------------------------
# Maze generation (recursive backtracker, written with an explicit stack)
# ---------------------------------------------------------------------------

def generate_maze(cols, rows, rng):
    """Carve a perfect maze of cols x rows cells.

    Cells live at odd grid coordinates with walls between them, so the
    returned grid has (2*rows + 1) lines of (2*cols + 1) characters.
    An explicit stack is used instead of recursion so huge mazes cannot
    overflow Python's call stack.
    """
    grid = [[WALL] * (2 * cols + 1) for _ in range(2 * rows + 1)]
    visited = {(0, 0)}
    stack = [(0, 0)]
    grid[1][1] = OPEN

    while stack:
        cx, cy = stack[-1]
        neighbors = [
            (cx + dx, cy + dy)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if 0 <= cx + dx < cols
            and 0 <= cy + dy < rows
            and (cx + dx, cy + dy) not in visited
        ]
        if not neighbors:
            stack.pop()
            continue

        nx, ny = rng.choice(neighbors)
        visited.add((nx, ny))
        # Open the new cell and knock down the wall between the two cells.
        grid[2 * ny + 1][2 * nx + 1] = OPEN
        grid[cy + ny + 1][cx + nx + 1] = OPEN
        stack.append((nx, ny))

    return grid


def open_neighbors(grid, pos):
    """Yield walkable grid neighbors of (row, col), ignoring walls."""
    row, col = pos
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != WALL:
            yield (nr, nc)


def reconstruct_path(parent, end):
    """Walk the parent map backwards from end to start."""
    if end not in parent:
        return None
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


# ---------------------------------------------------------------------------
# Solvers. Each returns (path, explored_count).
# ---------------------------------------------------------------------------

def solve_bfs(grid, start, end):
    """Breadth-first search: a queue explores cells in rings of distance."""
    queue = deque([start])
    parent = {start: None}
    explored = 0
    while queue:
        pos = queue.popleft()
        explored += 1
        if pos == end:
            break
        for neighbor in open_neighbors(grid, pos):
            if neighbor not in parent:
                parent[neighbor] = pos
                queue.append(neighbor)
    return reconstruct_path(parent, end), explored


def solve_dfs(grid, start, end):
    """Depth-first search: a stack dives as deep as possible first."""
    stack = [start]
    parent = {start: None}
    explored = 0
    while stack:
        pos = stack.pop()
        explored += 1
        if pos == end:
            break
        for neighbor in open_neighbors(grid, pos):
            if neighbor not in parent:
                parent[neighbor] = pos
                stack.append(neighbor)
    return reconstruct_path(parent, end), explored


def solve_astar(grid, start, end):
    """A* search: order the frontier by (distance so far + heuristic).

    The Manhattan distance never overestimates the remaining walk, so
    A* is guaranteed to find a shortest path while typically expanding
    far fewer cells than BFS.
    """

    def heuristic(pos):
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    frontier = [(heuristic(start), 0, start)]
    cost_so_far = {start: 0}
    parent = {start: None}
    closed = set()
    explored = 0

    while frontier:
        _, cost, pos = heapq.heappop(frontier)
        if pos in closed:
            continue  # stale heap entry for an already-settled cell
        closed.add(pos)
        explored += 1
        if pos == end:
            break
        for neighbor in open_neighbors(grid, pos):
            new_cost = cost + 1
            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = pos
                heapq.heappush(
                    frontier, (new_cost + heuristic(neighbor), new_cost, neighbor)
                )
    return reconstruct_path(parent, end), explored


SOLVERS = {
    "bfs": ("Breadth-First Search", solve_bfs),
    "dfs": ("Depth-First Search", solve_dfs),
    "astar": ("A* Search", solve_astar),
}


# ---------------------------------------------------------------------------
# Rendering and reporting
# ---------------------------------------------------------------------------

def render_maze(grid, path=None):
    """Return the maze as text, optionally drawing a solution path."""
    cells = [list(row) for row in grid]
    if path:
        for row, col in path:
            cells[row][col] = PATH
    cells[1][1] = START
    cells[-2][-2] = END
    return "\n".join("".join(row) for row in cells)


def run_self_test():
    """Verify maze structure and solver guarantees on several mazes."""
    rng = random.Random(2024)
    for cols, rows in ((1, 1), (2, 3), (8, 5), (15, 9)):
        grid = generate_maze(cols, rows, rng)
        assert len(grid) == 2 * rows + 1
        assert all(len(row) == 2 * cols + 1 for row in grid)

        start, end = (1, 1), (2 * rows - 1, 2 * cols - 1)
        assert grid[start[0]][start[1]] == OPEN
        assert grid[end[0]][end[1]] == OPEN

        # A perfect maze connects every open cell to the start.
        open_cells = sum(row.count(OPEN) for row in grid)
        reached = set()
        queue = deque([start])
        while queue:
            pos = queue.popleft()
            if pos in reached:
                continue
            reached.add(pos)
            queue.extend(open_neighbors(grid, pos))
        assert len(reached) == open_cells, "maze is not fully connected"

        lengths = {}
        for key, (_, solver) in SOLVERS.items():
            path, explored = solver(grid, start, end)
            assert path is not None, "{} found no path".format(key)
            assert path[0] == start and path[-1] == end
            assert explored > 0
            for (r1, c1), (r2, c2) in zip(path, path[1:]):
                assert abs(r1 - r2) + abs(c1 - c2) == 1, "path jumps"
                assert grid[r2][c2] != WALL, "path crosses a wall"
            lengths[key] = len(path)

        # BFS and A* must agree on the shortest length; DFS may be longer.
        assert lengths["bfs"] == lengths["astar"]
        assert lengths["dfs"] >= lengths["bfs"]

    print("All self-tests passed (generation + 3 solvers).")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a random maze and solve it with BFS, DFS, and A*."
    )
    parser.add_argument("--width", type=int, default=15, help="maze width in cells (default: 15)")
    parser.add_argument("--height", type=int, default=8, help="maze height in cells (default: 8)")
    parser.add_argument("--seed", type=int, default=None, help="random seed for a reproducible maze")
    parser.add_argument(
        "--algorithm", choices=sorted(SOLVERS) + ["all"], default="all",
        help="which solver to run (default: all)",
    )
    parser.add_argument("--test", action="store_true", help="run correctness self-tests and exit")
    args = parser.parse_args()

    if args.test:
        run_self_test()
        return 0
    if args.width < 1 or args.height < 1:
        parser.error("--width and --height must be at least 1")

    rng = random.Random(args.seed)
    grid = generate_maze(args.width, args.height, rng)
    start, end = (1, 1), (2 * args.height - 1, 2 * args.width - 1)
    names = sorted(SOLVERS) if args.algorithm == "all" else [args.algorithm]

    print("Maze: {} x {} cells (seed: {})".format(args.width, args.height, args.seed))
    results = []
    for key in names:
        title, solver = SOLVERS[key]
        begin = time.perf_counter()
        path, explored = solver(grid, start, end)
        elapsed_ms = (time.perf_counter() - begin) * 1000.0
        if path is None:
            print("\n{}: no path found!".format(title))
            continue
        print("\n--- {} ---".format(title))
        print(render_maze(grid, path))
        print(
            "Path length: {} steps | Cells explored: {} | Time: {:.2f} ms".format(
                len(path) - 1, explored, elapsed_ms
            )
        )
        results.append((title, len(path) - 1, explored))

    if len(results) > 1:
        print("\n--- Comparison ---")
        for title, length, explored in results:
            print("{:<22} path {:>4} steps, explored {:>4} cells".format(title, length, explored))
        shortest = min(length for _, length, _ in results)
        print("Shortest possible path: {} steps (BFS and A* always find it).".format(shortest))
        print(
            "Note: a perfect maze has exactly one route between any two cells, so all\n"
            "three solvers find the same path -- compare the cells explored instead."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
