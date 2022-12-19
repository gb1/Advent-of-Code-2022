from typing import NamedTuple, List, Dict, TypeVar

T = TypeVar('T')


class Valve(NamedTuple):
    flow_rate: int
    depth: int
    tunnels: List[str]


lines = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II"
]

valves: Dict[str, Valve] = {}

for line in lines:
    line = line.replace("leads", "lead")
    line = line.replace("valves", "valve")
    valve = line.split(" ")[1]
    flow_rate = line.split("=")[1].split(";")[0]
    tunnels = line.split("lead to valve ")[1].split(", ")
    valves[valve] = Valve(int(flow_rate), 0, tunnels)


def spelunk(minutes: int, start: str, valves: Dict[str, Valve]) -> int:

    for minute in range(minutes+1):
        print(f"== Minute {minute} ==")
    return 0


if __name__ == "__main__":
    print(spelunk(1, 'AA', valves))
