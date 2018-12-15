#/usr/bin/env python3
import re

def main():
    part1()
    # part2

def part1():
    with open('in.txt') as f:
        for line in f.readlines():
            vals = re.search(r'Step (?P<dep>\w{1}) must be finished before step (?P<node>\w{1}) can begin.', line)
            print(vals.group('dep'))
            print(vals.group('node'))

def part2():
    with open('in.txt') as f:
        polymer = f.read()
        best_result = len(polymer)
        best_result_unit = None
        for i in range(65, 91):
            polymer_test = polymer.replace(chr(i), '').replace(chr(i + 32), '')
            polymer_synth = synthesize(polymer_test)
            if (len(polymer_synth) < best_result):
                best_result = len(polymer_synth)
                best_result_unit = chr(i)
        print('Best result: ' + str(best_result) + ' with removed: ' + str(best_result_unit))

if __name__ == '__main__':
    main()
