#/usr/bin/env python3

def parse_num(in_str):
    is_neg = -1 if (in_str[0] == '-') else 1
    num = 0
    for c in in_str[1:]:
        if (c == '\n'):
            break
        num = (num * 10) + int(c)
    return num * is_neg

def main():
    part1()
    part2()

def part1():
    with open('in.txt') as f:
        freq = 0
        for line in f.readlines():
            freq += parse_num(line)
    print(freq)

def part2():
    freq_visited = set()
    freq = 0
    with open('in.txt') as f:
        lines = f.readlines()
        while (freq not in freq_visited):
            for line in lines:
                freq_visited.add(freq)
                freq += parse_num(line)
                if (freq in freq_visited):
                    print(freq)
                    break


if __name__ == '__main__':
    main()