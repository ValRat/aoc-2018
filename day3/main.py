#/usr/bin/env python3
import re

def parse_num(in_str):
    is_neg = -1 if (in_str[0] == '-') else 1
    num = 0
    for c in in_str[1:]:
        if (c == '\n'):
            break
        num = (num * 10) + int(c)
    return num * is_neg

def main():
    # part1()
    part2()

def part1():
    # 1000x1000 array
    cut_claim = [[0] * 2000 for i in range(2000)]
    with open('in.txt') as f:
        for line in f.readlines():
            vals = re.search(r'\#\d+ @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line)
            if (vals):
                x = int(vals.group('x'))
                y = int(vals.group('y'))
                w = int(vals.group('w'))
                h = int(vals.group('h'))
                for i in range(w):
                    for j in range(h):
                        cut_claim[x + i + 1][y + j + 1] += 1
        overlap = 0
        for i in range(2000):
            for j in range(2000):
                if cut_claim[i][j] > 1:
                    overlap += 1
        print(overlap)



def part2():
    # 1000x1000 array
    # These are gross solutions
    cut_claim = [[0] * 2000 for i in range(2000)]
    with open('in.txt') as f:
        lines = f.readlines()
        for line in lines:
            vals = re.search(r'\#\d+ @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line)
            if (vals):
                x = int(vals.group('x'))
                y = int(vals.group('y'))
                w = int(vals.group('w'))
                h = int(vals.group('h'))
                for i in range(w):
                    for j in range(h):
                        cut_claim[x + i + 1][y + j + 1] += 1
        for line in lines:
            vals = re.search(r'\#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line)
            if (vals):
                x = int(vals.group('x'))
                y = int(vals.group('y'))
                w = int(vals.group('w'))
                h = int(vals.group('h'))
                has_overlap = False
                for i in range(w):
                    if not has_overlap:
                        for j in range(h):
                            if (cut_claim[x + i + 1][y + j + 1] > 1):
                                has_overlap = True
                                break
                if not has_overlap:
                    print(vals.group('id'))
                    return



if __name__ == '__main__':
    main()
