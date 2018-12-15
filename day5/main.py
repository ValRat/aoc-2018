#/usr/bin/env python3

def main():
    part1()
    part2()

def is_opposing_polarization(a, b):
    if ord(a) + 32 == ord(b):
        return True
    if ord(a) - 32 == ord(b):
        return True
    return False

def passthrough(polymer):
    if len(polymer) < 2:
        return polymer
    for i in range(len(polymer) - 1, -1, -1):
        if (i + 2) > len(polymer):
            continue
        if is_opposing_polarization(polymer[i], polymer[i+1]):
            polymer = polymer[0:i] + polymer[i+2:]
    return polymer


def synthesize(polymer):
    len_polymer = None
    while (len_polymer != len(polymer)):
        # When the polymer is not changed anymore
        len_polymer = len(polymer)
        polymer = passthrough(polymer)
    return polymer

        

def part1():
    with open('in.txt') as f:
        polymer = f.read()
        polymer = synthesize(polymer)
        print(len(polymer))


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
