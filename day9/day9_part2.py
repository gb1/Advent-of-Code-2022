tail_positions = {(0, 0)}


def rope_map(head, tails: list, size):
    rope = []
    line = []
    for y in range(-size, size):
        for x in range(-size, size):
            if head == (x, y):
                line.append("H")
            elif (x, y) in tails:
                line.append(str(tails.index((x, y)) + 1))
            elif x == 0 and y == 0:
                line.append("S")
            elif (x, y) in tail_positions:
                line.append("#")
            else:
                line += ["."]
        rope.append(line)
        line = []
    rope.reverse()
    return rope


def move_head_up(h, t: list, moves) -> tuple:
    (x, y) = h

    for i in range(moves):
        y += 1
        h = (x, y)
        t = move_tails(h, t)

    return h, t


def move_head_down(h, t: list, moves) -> tuple:
    (x, y) = h

    for i in range(moves):
        y -= 1
        h = (x, y)
        t = move_tails(h, t)

    return h, t


def move_head_right(h, t: list, moves) -> tuple:
    (x, y) = h

    for i in range(moves):
        x += 1
        h = (x, y)
        t = move_tails(h, t)

    return h, t


def move_head_left(h, t: list, moves) -> tuple:
    (x, y) = h

    for i in range(moves):
        x -= 1
        h = (x, y)
        t = move_tails(h, t)

    return h, t


def move_tails(h, t: list) -> list:
    new_tails = []
    for tail in t:
        new_tails.append(move_tail(h, tail))
        h = new_tails[-1]

    tail_positions.add(new_tails[8])

    return new_tails


def move_tail(h, tail) -> tuple:
    (tailx, taily) = tail
    (headx, heady) = h

    # manhattan distance
    manhattan = abs(tailx - headx) + abs(taily - heady)

    if tailx != headx and taily != heady and manhattan > 2:
        if tailx < headx:
            tailx += 1
        if tailx > headx:
            tailx -= 1
        if taily < heady:
            taily += 1
        if taily > heady:
            taily -= 1

        return tailx, taily

    # tail to the left of head
    if tailx < headx - 1:
        return tailx + 1, taily

    # tail to the right of head
    if tailx > headx + 1:
        return tailx - 1, taily

    # tail above head
    if taily < heady - 1:
        return tailx, taily + 1

    # tail below head
    if taily > heady + 1:
        return tailx, taily - 1

    return tail


if __name__ == "__main__":
    lines = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20"
    ]

    head = (0, 0)
    tails = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    size = 100

    lines = [line.strip() for line in open('input.txt')]

    for line in lines:
        (move, steps) = line.split(" ")
        if move == "R":
            head, tails = move_head_right(head, tails, int(steps))
        elif move == "L":
            head, tails = move_head_left(head, tails, int(steps))
        elif move == "U":
            head, tails = move_head_up(head, tails, int(steps))
        elif move == "D":
            head, tails = move_head_down(head, tails, int(steps))

    for map_line in rope_map(head, tails, size):
        print("".join(map_line))


    print(len(tail_positions))
