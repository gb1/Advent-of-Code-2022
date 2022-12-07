# Linked list type of thing to hold the directories and their parent
from typing import List


class Dir:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []


# List to hold the directories (dir names are not unique!)
dirs = []
current_dir = None

lines = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k"
]


lines = [line.strip() for line in open('day7/input.txt')]

# parse the input into dirs with the base level sizes
for line in lines:
    if line == "$ cd /":
        dir = Dir(name="/", parent=None)
        dirs.append(dir)
        current_dir = dir
    elif line == "$ cd ..":
        current_dir = current_dir.parent
    elif line.startswith("$ cd "):
        dir = Dir(name=line.replace("$ cd ", ""), parent=current_dir)
        dirs.append(dir)
        if dir not in current_dir.children:
            current_dir.children.append(dir)
        current_dir = dir
    elif line.split(" ")[0].isdigit():
        current_dir.size += int(line.split(" ")[0])

# find the lowest level directories
lowest_level = [dir for dir in dirs if len(dir.children) == 0]


# add the sizes of the lowest level directories to their parents
for dir in lowest_level:
    while dir.parent is not None:
        dir.parent.size += dir.size
        dir = dir.parent

small_dirs = [dir for dir in dirs if dir.size <= 100000]

part1 = 0

for dir in small_dirs:
    part1 += dir.size

print(f"part 1: {part1}")

# # Part 2


lines = [line.strip() for line in open('day7/input.txt')]


paths = {}
current_path = []


def path_to_string(path):
    return "/".join(path)


# Store full path for this one, much better idea
for line in lines:
    if line == "$ cd /":
        current_path = ["root"]
        paths[path_to_string(current_path)] = 0
    elif line == "$ cd ..":
        current_path.pop()
    elif line.startswith("$ cd "):
        current_path += [line.replace("$ cd ", "")]
        paths[path_to_string(current_path)] = 0
    elif line.split(" ")[0].isdigit():
        paths[path_to_string(current_path)] += int(line.split(" ")[0])

paths = dict(sorted(paths.items()))

# for each paths, find all the paths that have it as a subpath
# Then sum up the file sizes
for path in paths:
    for other in paths:
        if other.startswith(path) and other != path:
            paths[path] += paths[other]

# sort the values and start with the smallest to get the one to delete
values = list(paths.values())
values.sort()

total = paths["root"]
free_space = 70000000 - total
target = 30000000 - free_space

for value in values:
    if value >= target:
        print(f"part 2: {value}")
        break
