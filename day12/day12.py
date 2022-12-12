# lines = [
#     "Sabqponm",
#     "abcryxxl",
#     "accszExk",
#     "acctuvwj",
#     "abdefghi"
# ]

lines = [line.strip() for line in open('input.txt')]

heights = {}
adjacents = {}
start = None
goal = None

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        heights[(x, y)] = ord(char)
        if char == "S":
            start = (x, y)
        if char == "E":
            goal = (x, y)

heights[start] = 97
heights[goal] = 122

for height in heights:
    adjacents[height] = []

    (x, y) = height
    for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        neighbour = (x + dx, y + dy)
        if neighbour in heights:
            neighbour_height = heights[neighbour]
            height_diff = heights[height] - neighbour_height
            if height_diff > -2:
                adjacents[(x, y)].append(neighbour)


# print(start)
# print(goal)

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path

            # mark node as explored
            explored.append(node)


path = bfs_shortest_path(adjacents, start, goal)
print(f"part 1: {len(path) - 1}")  # remove 1 for start node

# Part 2

start_candidates = [height for height in heights if heights[height] == 97]

paths = []

for start in start_candidates:
    path = bfs_shortest_path(adjacents, start, goal)
    if path:
        paths.append(path)

shortest_path = min(paths, key=len)
print(f"part 2: {len(shortest_path) - 1}")  # remove 1 for start node
