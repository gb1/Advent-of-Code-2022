lines = [
    "2,2,2",
    "1,2,2",
    "3,2,2",
    "2,1,2",
    "2,3,2",
    "2,2,1",
    "2,2,3",
    "2,2,4",
    "2,2,6",
    "1,2,5",
    "3,2,5",
    "2,1,5",
    "2,3,5"
]

lines = [line.strip() for line in open('input.txt')]

points = []
for line in lines:
    x, y, z = line.split(",")
    points.append((int(x), int(y), int(z)))

neighbours = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]


def calculate_exposed(points):
    exposed = 0
    for x, y, z in points:
        exposed += 6
        for dx, dy, dz in neighbours:
            if (x + dx, y + dy, z + dz) in points:
                exposed -= 1
    return exposed


print(f"part 1: {calculate_exposed(points)}")

# Part 2

area = {(x, y, z) for x in range(22) for y in range(22) for z in range(22)}
empty_space = list(area - set(points))
air_pockets = []

while empty_space:
    to_check = [empty_space[0]]
    current_bubble = set()

    while len(to_check):
        next_air = to_check.pop()

        if next_air in empty_space:
            current_bubble.add(next_air)
            empty_space.remove(next_air)

            x, y, z = next_air
            for dx, dy, dz in neighbours:
                to_check.append((x + dx, y + dy, z + dz))

    if (0, 0, 0) not in current_bubble:
        air_pockets.append(current_bubble)



print(f"part 2: {calculate_exposed(points)- sum(calculate_exposed(pocket) for pocket in air_pockets)}")
