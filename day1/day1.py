
elves = []
total = 0

for line in open('input.txt'):
    if line.strip() != '':
        total += int(line.strip())
    else:
        elves.append(total)
        total = 0

print(f"part 1: {max(elves)}")
print(f"part 2: {sum(sorted(elves, reverse=True)[:3])}")
