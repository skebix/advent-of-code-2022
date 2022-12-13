"""AoC Day 6: Tuning Trouble, Part 2"""

from utils import read_char


if __name__ == "__main__":
    position = 0
    last_fourteen = ''
    for char in read_char("input.txt"):
        position += 1
        last_fourteen = last_fourteen[-13:] + char
        set_last_fourteen = set(last_fourteen)
        if len(set_last_fourteen) == 14:
            break
    print(position)
