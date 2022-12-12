import math


class Monkey:
    def __init__(self, name: str, items: list, operation: str, test_divisor: int, target_monkey_true,
                 target_monkey_false, items_inspected: int = 0):
        self.name = name
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.target_monkey_true = target_monkey_true
        self.target_monkey_false = target_monkey_false
        self.items_inspected = items_inspected

    def __str__(self):
        return f'{self.name}: {", ".join(self.items)}'


if __name__ == "__main__":
    monkeys = [Monkey("Monkey 0", [79, 98], "old * 19", 23, 2, 3),
               Monkey("Monkey 1", [54, 65, 75, 74], "old + 6", 19, 2, 0),
               Monkey("Monkey 2", [79, 60, 97], "old * old", 13, 1, 3),
               Monkey("Monkey 3", [74], "old + 3", 17, 0, 1)]

    # monkeys = [Monkey("Monkey 0", [97, 81, 57, 57, 91, 61], "old * 7", 11, 5, 6),
    #            Monkey("Monkey 1", [88, 62, 68, 90], "old * 17", 19, 4, 2),
    #            Monkey("Monkey 2", [74, 87], "old + 2", 5, 7, 4),
    #            Monkey("Monkey 3", [53, 81, 60, 87, 90, 99, 75], "old + 1", 2, 2, 1),
    #            Monkey("Monkey 4", [57], "old + 6", 13, 7, 0),
    #            Monkey("Monkey 5", [54, 84, 91, 55, 59, 72, 75, 70], "old * old", 7, 6, 3),
    #            Monkey("Monkey 6", [95, 79, 79, 68, 78], "old + 3", 3, 1, 3),
    #            Monkey("Monkey 7", [61, 97, 67], "old + 4", 17, 0, 5)]

    for _ in range(1000):

        for monkey in monkeys:
            items = monkey.items.copy()

            for item in items:
                old = item
                worry = math.floor(eval(monkey.operation) / 3)
                monkey.items_inspected += 1
                if worry % monkey.test_divisor == 0:
                    monkey.items.remove(item)
                    monkeys[monkey.target_monkey_true].items.append(worry)
                else:
                    monkey.items.remove(item)
                    monkeys[monkey.target_monkey_false].items.append(worry)

    items_inspected = [monkey.items_inspected for monkey in monkeys]
    items_inspected.sort()

    last_two = items_inspected[-2:]
    print("part 1:", last_two[0] * last_two[1])
