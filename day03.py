def part1(tree_map):
    trees = 0
    i = 0
    for line in tree_map:
        if line[i % len(line)] == '#':
            trees += 1
        i += 3
    return trees


def part2(tree_map):
    trees_result = 0
    for slope in (1, 3, 5, 7):
        trees = 0
        i = 0
        for line in tree_map:
            if line[i % len(line)] == '#':
                trees += 1
            i += slope
        if trees_result == 0:
            trees_result = trees
        else:
            trees_result *= trees
    skip = False
    i = 0
    trees = 0
    for line in tree_map:
        if not skip:
            skip = True
        else:
            skip = False
            continue
        if line[i % len(line)] == '#':
            trees += 1
        i += 1
    return trees * trees_result


if __name__ == "__main__":
    tree_map = []
    with open('inputs/03') as f:
        tree_map = list(map(lambda l: l.rstrip('\n'), f.readlines()))
    print(part1(tree_map))
    print(part2(tree_map))
