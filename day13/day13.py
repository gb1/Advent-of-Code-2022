def right_order(left, right) -> str:
    if left == right:
        print(f"Compare {left} and {right}, equal!")
        return "equal"

    if isinstance(left, int) and isinstance(right, int):
        print(f"Compare {left} and {right}")
        if left < right:
            print(f"Left {left} is smaller than right {right}")
            return "right!"
        if left > right:
            print(f"Left {left} is bigger than right {right}")
            return "wrong!"

    if isinstance(left, int) and isinstance(right, list):
        print(f"Compare {left} and {right}")
        return right_order([left], right)

    if isinstance(left, list) and isinstance(right, int):
        print(f"Compare {left} and {right}")
        return right_order(left, [right])

    if left and right:
        result = right_order(left[0], right[0])
        if result == "equal":
            return right_order(left[1:], right[1:])
        else:
            return result
    if left:
        return "wrong!"
    else:
        return "right!"


def pairs(lines):
    for i in range(0, len(lines), 2):
        yield lines[i:i + 2]


if __name__ == "__main__":

    right_order(eval("[1,1,3,1,1]"), eval("[[5,5],4,4,4]"))

    # lines = [
    #     "[1,1,3,1,1]", "[1,1,5,1,1]",
    #     "[[1], [2, 3, 4]]", "[[1], 4]",
    #     "[9]", "[[8, 7, 6]]",
    #     "[[4, 4], 4, 4]", "[[4, 4], 4, 4, 4]",
    #     "[7, 7, 7, 7]", "[7, 7, 7]",
    #     "[]", "[3]",
    #     "[[[]]]", "[[]]",
    #     "[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]", "[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]"
    # ]

    lines = [line.strip() for line in open('input.txt')]

    lines = list(filter(None, lines))

    pair_index = 1
    answer = 0

    for index, pair in enumerate(pairs(lines)):

        print(f"\n== Pair {pair_index} ==")

        if right_order(eval(pair[0]), eval(pair[1])) == "right!":
            answer += pair_index
            print("right!")
        else:
            print("wrong!")
        pair_index += 1

    print(f"part 1: {answer}")

    # Part 2

    lines = [line.strip() for line in open('input.txt')]
    lines = list(filter(None, lines))

    packets = []

    for line in lines:
        packets.append(eval(line))
    packets = packets + [eval("[[2]]"), eval("[[6]]")]

    print("done")

    # Bubble sort
    for i in range(len(packets)):
        for j in range(len(packets) - i - 1):
            if right_order(packets[j], packets[j + 1]) == "wrong!":
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    divider1 = 0
    divider2 = 0

    for index, packet in enumerate(packets):
        if packet == [[2]]:
            # print(index)
            divider1 = index + 1
        if packet == [[6]]:
            # print(index)
            divider2 = index + 1

    print(f"part 2: {divider1 * divider2}")