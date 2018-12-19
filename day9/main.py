#/usr/bin/env python3

def main():
    part1()
    part2()

def part1():
    num_players = 459
    num_marbles = 71320
    marbles = [0 for i in range(num_marbles)]
    scores = [0 for i in range(num_players)]
    curr_num_marbles = 1
    curr_player = 0
    curr_marble = 0
    with open('in.txt') as f:
        for i in range(1, num_marbles + 1):
            # Special case for 0/1
            if (i == 1):
                curr_marble = 1
            else:
                curr_marble = (curr_marble + 2) % curr_num_marbles

            if ((i % 23) != 0):
                curr_num_marbles += 1
                marbles.insert(curr_marble, i)
            else:
                scores[curr_player] += i
                cc_index = ((curr_marble - 7) % curr_num_marbles)
                scores[curr_player] += marbles[cc_index]
                marbles = marbles[:cc_index] + marbles[cc_index + 1:]
                curr_num_marbles -= 1
            curr_player = (curr_player + 1) % num_players

    score_max = 0
    for score in scores:
        if score > score_max:
            score_max = score
    print(score_max)


def part2():
    with open('in.txt') as f:
        pass

if __name__ == '__main__':
    main()
