"""AoC Day 2: Rock Paper Scissors, Part 1"""

if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as f:
        # round_score + shape_score
        round_result = {
            ("A", "Z"): 0 + 3,
            ("B", "X"): 0 + 1,
            ("C", "Y"): 0 + 2,
            ("A", "X"): 3 + 1,
            ("B", "Y"): 3 + 2,
            ("C", "Z"): 3 + 3,
            ("A", "Y"): 6 + 2,
            ("B", "Z"): 6 + 3,
            ("C", "X"): 6 + 1,
        }
        TOTAL_SCORE = 0
        for line in f:
            opponent_choice, my_choice = line.strip().split(" ")
            TOTAL_SCORE += round_result[(opponent_choice, my_choice)]
        print(TOTAL_SCORE)
