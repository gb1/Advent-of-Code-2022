
def common(rucksack):
    contents = list(rucksack)

    first = contents[0:int(len(contents)/2)]
    second = contents[int(len(contents)/2):]

    return list((set(first) & set(second)))[0]


def score(item):
    if (item.isupper()):
        return ord(item) - 38
    return ord(item) - 96


part1 = 0
for line in open('day3/input.txt'):
    part1 += score(common(line.strip()))

print(f"part 1: {part1}")


lines = [line.strip() for line in open('day3/input.txt')]


def groups(lines):
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]


def common_group(group):
    return list(set(list(group[0])) & set(list(group[1])) & set(list(group[2])))[0]


part2 = 0
for group in groups(lines):
    part2 += score(common_group(group))


print(f"part 2: {part2}")
