# [T]     [Q]             [S]
# [R]     [M]             [L] [V] [G]
# [D] [V] [V]             [Q] [N] [C]
# [H] [T] [S] [C]         [V] [D] [Z]
# [Q] [J] [D] [M]     [Z] [C] [M] [F]
# [N] [B] [H] [N] [B] [W] [N] [J] [M]
# [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
# [B] [W] [N] [P] [D] [V] [G] [L] [T]
#  1   2   3   4   5   6   7   8   9

cranes = {}
cranes[1] = ["B", "P", "N", "Q", "H", "D", "R", "T"]
cranes[2] = ["W", "G", "B", "J", "T", "V"]
cranes[3] = ["N", "R", "H", "D", "S", "V", "M", "Q"]
cranes[4] = ["P", "Z", "N", "M", "C"]
cranes[5] = ["D", "Z", "B"]
cranes[6] = ["V", "C", "W", "Z"]
cranes[7] = ["G", "Z", "N", "C", "V", "Q", "L", "S"]
cranes[8] = ["L", "G", "J", "M", "D", "N", "V"]
cranes[9] = ["T", "P", "M", "F", "Z", "C", "G"]

# cranes[1] = ["Z", "N"]
# cranes[2] = ["M", "C", "D"]
# cranes[3] = ["P"]

lines = [line.strip() for line in open('day5/input.txt')]

# lines = [
#     "move 1 from 2 to 1",
#     "move 3 from 1 to 3",
#     "move 2 from 2 to 1",
#     "move 1 from 1 to 2"
# ]

for line in lines:
    [_, amount, _, source, _, dest] = line.split(" ")
    amount = int(amount)
    source = int(source)
    dest = int(dest)

    chunk = cranes[source][len(cranes[source])-amount:]
    chunk.reverse()
    cranes[source] = cranes[source][:len(cranes[source])-amount]
    cranes[dest] = cranes[dest] + chunk

part1 = ""
for crane in cranes:
    part1 = part1 + cranes[crane][-1]

print(f"part 1: {part1}")


# Part 2

cranes[1] = ["B", "P", "N", "Q", "H", "D", "R", "T"]
cranes[2] = ["W", "G", "B", "J", "T", "V"]
cranes[3] = ["N", "R", "H", "D", "S", "V", "M", "Q"]
cranes[4] = ["P", "Z", "N", "M", "C"]
cranes[5] = ["D", "Z", "B"]
cranes[6] = ["V", "C", "W", "Z"]
cranes[7] = ["G", "Z", "N", "C", "V", "Q", "L", "S"]
cranes[8] = ["L", "G", "J", "M", "D", "N", "V"]
cranes[9] = ["T", "P", "M", "F", "Z", "C", "G"]

for line in lines:
    [_, amount, _, source, _, dest] = line.split(" ")
    amount = int(amount)
    source = int(source)
    dest = int(dest)

    chunk = cranes[source][len(cranes[source])-amount:]
    cranes[source] = cranes[source][:len(cranes[source])-amount]
    cranes[dest] = cranes[dest] + chunk

part2 = ""
for crane in cranes:
    part2 = part2 + cranes[crane][-1]

print(f"part 2: {part2}")
