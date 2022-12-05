score = 0

for line in open('.\\day2\\input.txt'):
    game = line.strip()
    if game == 'A X':
        score += 4
    if game == 'B Y':
        score += 5
    if game == 'C Z':
        score += 6

    if game == 'C X':
        score += 7
    if game == 'A Y':
        score += 8
    if game == 'B Z':
        score += 9

    if game == 'B X':
        score += 1
    if game == 'C Y':
        score += 2
    if game == 'A Z':
        score += 3

print(f'Part 1: {score}')

score = 0
for line in open('.\\day2\\input.txt'):
    game = line.strip()

    if game == 'A X':
        score += 3
    if game == 'A Y':
        score += 4
    if game == 'A Z':
        score += 8

    if game == 'B X':
        score += 1
    if game == 'B Y':
        score += 5
    if game == 'B Z':
        score += 9

    if game == 'C X':
        score += 2
    if game == 'C Y':
        score += 6
    if game == 'C Z':
        score += 7

print(f'Part 2: {score}')
