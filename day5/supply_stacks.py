"""AoC Day 5: Supply Stacks, Part 1"""

if __name__ == "__main__":

    with open("input.txt", "r", encoding="utf-8") as f:
        stacks = [[] for i in range(9)]
        for line_number, line in enumerate(f):
            line = line.strip().replace("[", "").replace("]", "").split(" ")
            if line_number < 8:
                stack, blanks = 0, 0
                for element in line:
                    if element:
                        stacks[stack].append(element)
                        stack += 1
                    else:
                        blanks += 1
                        if blanks == 4:
                            stack += 1
                            blanks = 0
            elif line_number == 8:
                continue
            elif line_number == 9:
                stacks = [stack[::-1] for stack in stacks]
            else:
                amount, from_, to = (int(x) for x in line[1::2])
                for _ in range(amount):
                    stacks[to - 1].append(stacks[from_ - 1].pop())
        print("".join(stack.pop() for stack in stacks))
