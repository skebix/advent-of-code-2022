"""AoC Day 1: Calorie Counting, Part 1"""

if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as f:
        CALORIES, MAX_CALORIES = 0, 0
        for line in f:
            if line != "\n":
                CALORIES += int(line)
            else:
                if CALORIES > MAX_CALORIES:
                    MAX_CALORIES = CALORIES
                CALORIES = 0
        print(MAX_CALORIES)
