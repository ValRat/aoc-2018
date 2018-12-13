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
    # part1()
    part2()

def part1():
    twos = 0
    threes = 0
    with open('in.txt') as f:
        for line in f.readlines():
            stores = dict()
            for c in line:
                if (c != '\n'):
                    if c in stores:
                        stores[c] += 1
                    else:
                        stores[c] = 1

            has_three = False
            has_two = False
            for k in stores:
                if stores[k] == 3 and not has_three:
                    threes += 1
                    has_three = True
                if stores[k] == 2 and not has_two:
                    twos += 1
                    has_two = True

        print(twos * threes)

def part2():
    with open('in.txt') as f:
        lines = f.readlines()
        for line in lines:
            for line_comp in lines:
                if (line == line_comp):
                    break
                num_diff = 0
                for i, c in enumerate(line):
                    if c != line_comp[i]:
                        num_diff += 1
                if num_diff == 1:
                    print('Solution found: ')
                    print(line)
                    print(line_comp)

                    final_id  = ''
                    for i, c in enumerate(line):
                        if c == line_comp[i]:
                            final_id += c
                    print(final_id)


                


if __name__ == '__main__':
    main()
