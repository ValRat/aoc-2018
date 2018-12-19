#/usr/bin/env python3

def main():
    # part1()
    part2()

class Node:

    def __init__(self):
        self.children = []
        self.metadata = []
    
    def __str__(self):
        return '(*)'
    
    def get_tree_string(self, level = 0):
        tree_str = ''
        for i in range(level):
            tree_str += '\t'
        tree_str += str(self)
        tree_str += '\n'
        for child in self.children:
            tree_str += child.get_tree_string(level + 1)
        return tree_str
    
    def get_sum(self):
        my_sum = 0
        for num in self.metadata:
            my_sum += num
        for child in self.children:
            my_sum += child.get_sum()
        return my_sum

    def get_sum_part_2(self):
        my_sum = 0
        # Base case, no children
        # Return value of metadata
        if (len(self.children) == 0):
            for num in self.metadata:
                my_sum += num
            return my_sum

        for idx in self.metadata:
            if (idx > len(self.children)):
                continue
            my_sum += self.children[idx - 1].get_sum_part_2()
        return my_sum

def parse_node(license_file, index):
    node = Node()
    children_count = license_file[index]
    metadata_count = license_file[index + 1]
    curr_index = index + 2
    for i in range(children_count):
        child, curr_index = parse_node(license_file, curr_index)
        node.children.append(child)
    for i in range(metadata_count):
        node.metadata.append(license_file[curr_index + i])
    return node, curr_index + metadata_count

def sanitize_input(string_input):
    license_file = []
    for i in string_input.split(' '):
        license_file.append(int(i))
    return license_file

def print_tree(root):
    print(root.get_tree_string(0))

def part1():
    with open('in.txt') as f:
        license_file = sanitize_input(f.readline())
        tree, _ = parse_node(license_file, 0)
        print(tree.get_sum())


def part2():
    with open('in.txt') as f:
        license_file = sanitize_input(f.readline())
        tree, _ = parse_node(license_file, 0)
        print(tree.get_sum_part_2())

if __name__ == '__main__':
    main()
