"""AoC Day 6: Tuning Trouble, Part 1"""

from utils import read_char


if __name__ == "__main__":
    position = 0
    last_four = ''
    for char in read_char("input.txt"):
        position += 1
        last_four = last_four[-3:] + char
        set_last_fourteen = set(last_four)
        if len(set_last_fourteen) == 4:
            break
    print(position)
