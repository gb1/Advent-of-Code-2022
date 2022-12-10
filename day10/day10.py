import math

if __name__ == "__main__":
    instructions = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop"
    ]

    instructions = [line.strip() for line in open('input.txt')]

    register = 1
    value = 0
    buffer = []
    instruction = ""
    instructions.reverse()
    signal_strength = 0

    for cycle in range(1, 221):

        if cycle == 20:
            signal_strength += cycle * register
        if cycle == 60:
            signal_strength += cycle * register
        if cycle == 100:
            signal_strength += cycle * register
        if cycle == 140:
            signal_strength += cycle * register
        if cycle == 180:
            signal_strength += cycle * register
        if cycle == 220:
            signal_strength += cycle * register

        if buffer:
            register += buffer.pop()
        else:
            if instructions:
                instruction = instructions.pop()

            if instruction.startswith("addx"):
                value = int(instruction.split(" ")[1])
                buffer.append(value)

    print(f"part 1: {signal_strength}")

    # Part 2

    rows = [[], [], [], [], [], []]
    current_row = 0

    instructions = [line.strip() for line in open('input.txt')]

    register = 1
    value = 0
    buffer = []
    instruction = ""
    instructions.reverse()

    for cycle in range(0, 240):

        current_row = math.ceil((cycle + 1) / 40)
        cycle_row = cycle - (40 * (current_row - 1))
        sprite = [cycle_row -1, cycle_row, cycle_row + 1]

        if register in sprite:
            rows[current_row - 1].append("#")
        else:
            rows[current_row - 1].append(".")

        if buffer:
            register += buffer.pop()
        else:
            if instructions:
                instruction = instructions.pop()

            if instruction.startswith("addx"):
                value = int(instruction.split(" ")[1])
                buffer.append(value)

    for row in rows:
        print("".join(row))
