"""AoC Day 1: Calorie Counting, Part 2"""

if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as f:
        max_calories = [0, 0, 0]
        CALORIES = 0
        for line in f:
            if line != "\n":
                CALORIES += int(line)
            else:
                if CALORIES > max_calories[0]:
                    max_calories[0] = CALORIES
                    max_calories.sort()
                CALORIES = 0
        print(sum(max_calories))
