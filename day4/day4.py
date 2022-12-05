part1 = 0

lines = [line.strip() for line in open('day4/input.txt')]

# lines = ["2-8,3-7",
#          "6-6,4-6"]

for line in lines:
    elf1, elf2 = line.split(",")
    elf1_range = range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)
    elf2_range = range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)
    if elf1_range.start in elf2_range and elf1_range.stop - 1 in elf2_range:
        part1 += 1
    elif elf2_range.start in elf1_range and elf2_range.stop - 1 in elf1_range:
        part1 += 1


print(f"part 1: {part1}")

part2 = 0
for line in lines:
    elf1, elf2 = line.split(",")
    elf1_range = range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)
    elf2_range = range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)
    if elf1_range.start in elf2_range or elf1_range.stop - 1 in elf2_range:
        part2 += 1
    elif elf2_range.start in elf1_range or elf2_range.stop - 1 in elf1_range:
        part2 += 1


print(f"part 2: {part2}")
