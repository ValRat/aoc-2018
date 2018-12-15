#/usr/bin/env python3
import re

def main():
    #part1()
    part2()

def find_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def part1():
    coords = []
    with open('in.txt') as f:
        for line in f.readlines():
            vals = re.search(r'(?P<x>\d+), (?P<y>\d+)', line)
            if (vals):
                coords.append((int(vals.group('x')), int(vals.group('y'))))
        
        max_x = 0
        max_y = 0
        for coord in coords:
            if (coord[0] > max_x):
                max_x = coord[0]
            if (coord[1] > max_y):
                max_y = coord[1]

        # Boundary conditions lol
        max_x += 1
        max_y += 1

        board = [[-1 for x in range(max_y)] for x in range(max_x)]
        print('Max x: ' + str(max_x) + ' Max y: ' + str(max_y))

        for i in range(max_x):
            for j in range(max_y):
                curr_min = max_x + max_y + 3
                for idx, c in enumerate(coords):
                    d = find_distance((i, j), c)
                    if d == curr_min:
                        board[i][j] = -1
                    if d < curr_min:
                        #print('x: ' + str(i) + ' y:' + str(j))
                        #print('{0} closer to {1},{2} with {3} < {4}'.format(c,i,j,d,curr_min))
                        curr_min = d
                        board[i][j] = idx

        # print(board)
        dq_coords = []
        for i in range(0, max_x):
            if board[i][0] not in dq_coords:
                dq_coords.append(board[i][0])
            if board[i][max_y - 1] not in dq_coords:
                dq_coords.append(board[i][max_y - 1])
        
        for i in range(0, max_y):
            if board[0][i] not in dq_coords:
                dq_coords.append(board[0][i])
            if board[max_x - 1][i] not in dq_coords:
                dq_coords.append(board[max_x - 1][i])
            
        max_area = 0
        max_coord = None
        for idx, c in enumerate(coords):
            curr_area = 0
            if idx in dq_coords:
                continue
            for i in range(max_x):
                for j in range(max_y):
                    if board[i][j] == idx:
                        curr_area += 1
            if (curr_area > max_area):
                max_area = curr_area
                max_coord = c
        print('Max area: ' + str(max_area) + ' with coordinates: ' + str(max_coord))
        print('With index ' + str(coords.index(max_coord)))


def part2():
    coords = []
    with open('in.txt') as f:
        for line in f.readlines():
            vals = re.search(r'(?P<x>\d+), (?P<y>\d+)', line)
            if (vals):
                coords.append((int(vals.group('x')), int(vals.group('y'))))
        
        max_x = 0
        max_y = 0
        for coord in coords:
            if (coord[0] > max_x):
                max_x = coord[0]
            if (coord[1] > max_y):
                max_y = coord[1]

        # Boundary conditions lol
        max_x += 1
        max_y += 1

        board = [[-1 for x in range(max_y)] for x in range(max_x)]
        print('Max x: ' + str(max_x) + ' Max y: ' + str(max_y))

        for i in range(max_x):
            for j in range(max_y):
                distance_sum = 0
                for idx, c in enumerate(coords):
                    d = find_distance((i, j), c)
                    distance_sum += d
                if (distance_sum < 10000):
                    board[i][j] = 1

        within_area = 0
        for i in range(max_x):
            for j in range(max_y):
                if board[i][j] == 1:
                    within_area += 1
        print('Max area: ' + str(within_area))


if __name__ == '__main__':
    main()
