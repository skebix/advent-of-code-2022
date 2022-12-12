"""AoC Day 3: Rucksack Reorganization, Part 1"""

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        import string

        priorities = dict(zip(string.ascii_letters, range(1, 53)))
        SUM_PRIORITIES_BOTH_CONTAINERS = 0
        for line in f:
            line = line.strip()
            compartment1, compartment2 = line[: len(line) // 2], line[len(line) // 2 :]
            in_both_compartments = (
                set(compartment1).intersection(set(compartment2)).pop()
            )
            SUM_PRIORITIES_BOTH_CONTAINERS += priorities[in_both_compartments]
        print(SUM_PRIORITIES_BOTH_CONTAINERS)
