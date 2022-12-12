import os
import time


def clear():
    time.sleep(0.05)
    os.system('clear')


lines = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2"]

tail_positions = [(0, 0)]


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
            else:
                line += ["."]
        rope.append(line)
        line = []
    rope.reverse()
    return rope


def move_head_up(head, tails: list, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        y += 1
        head = (x, y)
        tails = move_tails(head, tails)

    return head, tails


def move_head_down(head, tails: list, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        y -= 1
        head = (x, y)
        tails = move_tails(head, tails)

    return head, tails


def move_head_right(head, tails: list, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        x += 1
        head = (x, y)
        tails = move_tails(head, tails)

    return head, tails


def move_head_left(head, tails: list, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        x -= 1
        head = (x, y)
        tails = move_tails(head, tails)

    return head, tails


def move_tails(h, tails: list) -> list:
    new_tails = []
    for tail in tails:
        new_tails.append(move_tail(h, tail))
        h = new_tails[-1]

    return new_tails


def move_tail(head, tail) -> tuple:
    (tailx, taily) = tail
    (headx, heady) = head
    tail_positions.append(tail)
    # tail below head and to the left (going up)
    if tailx < headx and taily < heady - 1:
        return headx, heady - 1

    # tail below head and to the right (going up)
    if tailx > headx and taily < heady - 1:
        return headx, heady - 1

    # tail above head and to the left (going down)
    if tailx < headx and taily > heady + 1:
        return headx, heady + 1

    # tail above head and to the right (going down)
    if tailx > headx and taily > heady + 1:
        return headx, heady + 1

    # tail below head and to the left (going right)
    if tailx < headx - 1 and taily < heady:
        return headx - 1, heady

    # tail above head and to the left (going right)
    if tailx < headx - 1 and taily > heady:
        return headx - 1, heady

    # tail below head and to the right (going left)
    if tailx > headx + 1 and taily < heady:
        return headx + 1, heady

    # tail below head and to the left (going left)
    if tailx > headx + 1 and taily > heady:
        return headx + 1, heady

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
        "R 4",
        "U 3",
        "U 1"
    ]

    head = (0, 0)
    tails = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    size = 20

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
