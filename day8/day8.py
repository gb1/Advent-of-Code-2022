# lines = [
#     "30373",
#     "25512",
#     "65332",
#     "33549",
#     "35390"
# ]

lines = [line.strip() for line in open('input.txt')]

size = len(list(lines[0]))

trees = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        trees[(x, y)] = int(char)


def check_tree_row(tree) -> bool:
    (tree_x, tree_y) = tree
    if tree_x == 0 or tree_x == size - 1 or tree_y == 0 or tree_y == size - 1:
        return True

    height = trees[tree]
    left_trees = [tree for tree in trees if tree[0] < tree_x and tree[1] == tree_y and trees[tree] >= height]
    right_trees = [tree for tree in trees if tree[0] > tree_x and tree[1] == tree_y and trees[tree] >= height]

    if len(left_trees) > 0 and len(right_trees) > 0:
        return False
    return True


def check_tree_col(tree) -> bool:
    (tree_x, tree_y) = tree
    if tree_x == 0 or tree_x == size - 1 or tree_y == 0 or tree_y == size - 1:
        return True

    height = trees[tree]
    higher_trees = [tree for tree in trees if tree[1] < tree_y and tree[0] == tree_x and trees[tree] >= height]
    lower_trees = [tree for tree in trees if tree[1] > tree_y and tree[0] == tree_x and trees[tree] >= height]

    if len(higher_trees) > 0 and len(lower_trees) > 0:
        return False
    return True


tall_trees = [tree for tree in trees if check_tree_row(tree) or check_tree_col(tree)]

print(f"part1: {len(set(tall_trees))}")


# Part 2

def score_tree(tree) -> int:
    (tree_x, tree_y) = tree
    height = trees[tree]

    left_score = 0
    right_score = 0
    higher_score = 0
    lower_score = 0

    for tx in range(tree_x - 1, -1, -1):
        if trees[(tx, tree_y)] < height:
            left_score += 1
        else:
            left_score += 1
            break

    for tx in range(tree_x + 1, size):
        if trees[(tx, tree_y)] < height:
            right_score += 1
        else:
            right_score += 1
            break

    for ty in range(tree_y - 1, -1, -1):
        if trees[(tree_x, ty)] < height:
            higher_score += 1
        else:
            higher_score += 1
            break

    for ty in range(tree_y + 1, size):
        if trees[(tree_x, ty)] < height:
            lower_score += 1
        else:
            lower_score += 1
            break

    return left_score * right_score * higher_score * lower_score


# print(score_tree((2, 3)))

scores = [score_tree(tree) for tree in trees]
print(f"part2: {max(scores)}")
