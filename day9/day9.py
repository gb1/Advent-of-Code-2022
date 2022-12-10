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


def rope_map(head, tail, size):
    rope = []
    line = []
    for y in range(-size, size):
        for x in range(-size, size):
            if head == (x, y):
                line.append("H")
            elif tail == (x, y):
                line.append("T")
            elif x == 0 and y == 0:
                line.append("S")
            else:
                line += ["."]
        rope.append(line)
        line = []
    rope.reverse()
    return rope


def move_head_up(head, tail, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        print("\n\n")
        clear()
        print("movin' up")
        y += 1
        head = (x, y)
        tail = move_tail(head, tail)
        rope = rope_map(head, tail, size)
        for line in rope:
            print("".join(line))

    return head, tail


def move_head_down(head, tail, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        print("\n\n")
        clear()
        print("movin' down")
        y -= 1
        head = (x, y)
        tail = move_tail(head, tail)
        rope = rope_map(head, tail, size)
        for line in rope:
            print("".join(line))

    return head, tail


def move_head_right(head, tail, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        print("\n\n")
        clear()
        print("movin' right")
        x += 1
        head = (x, y)
        tail = move_tail(head, tail)
        rope = rope_map(head, tail, size)
        for line in rope:
            print("".join(line))

    return head, tail


def move_head_left(head, tail, moves) -> tuple:
    (x, y) = head

    for i in range(moves):
        print("\n\n")
        clear()
        print("movin' left")
        x -= 1
        head = (x, y)
        tail = move_tail(head, tail)
        rope = rope_map(head, tail, size)
        for line in rope:
            print("".join(line))

    return head, tail


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

    head = (0, 0)
    tail = (0, 0)
    size = 50

    rope = rope_map(head, tail, size)
    for line in rope:
        print("".join(line))

    # print("\nR 4")
    # head, tail = move_head_right(head, tail, 4)
    # print("\nU 4")
    # head, tail = move_head_up(head, tail, 4)
    # print("\nL 3")
    # head, tail = move_head_left(head, tail, 3)
    # print("\nD 1")
    # head, tail = move_head_down(head, tail, 1)
    # print("\nR 4")
    # head, tail = move_head_right(head, tail, 4)
    # print("\nD 1")
    # head, tail = move_head_down(head, tail, 1)
    # print("\nL 5")
    # head, tail = move_head_left(head, tail, 5)
    # print("\nR 2")
    # head, tail = move_head_right(head, tail, 2)

    lines = [line.strip() for line in open('input.txt')]

    for line in lines:
        (move, steps) = line.split(" ")

        if move == "R":
            head, tail = move_head_right(head, tail, int(steps))
        elif move == "L":
            head, tail = move_head_left(head, tail, int(steps))
        elif move == "U":
            head, tail = move_head_up(head, tail, int(steps))
        elif move == "D":
            head, tail = move_head_down(head, tail, int(steps))

    print(len(set(tail_positions)))
