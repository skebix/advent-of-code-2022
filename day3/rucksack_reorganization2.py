"""AoC Day 3: Rucksack Reorganization, Part 2"""

if __name__ == "__main__":
    import string
    from itertools import islice

    priorities = dict(zip(string.ascii_letters, range(1, 53)))
    SUM_GROUP_PRIORITIES = 0
    with open("input.txt", "r", encoding="utf-8") as f:
        while True:
            try:
                rucksack1, rucksack2, rucksack3 = islice(f, 3)
            except ValueError:
                break
            badge = (
                set(rucksack1.strip()) & set(rucksack2.strip()) & set(rucksack3.strip())
            )
            SUM_GROUP_PRIORITIES += priorities[badge.pop()]
        print(SUM_GROUP_PRIORITIES)
