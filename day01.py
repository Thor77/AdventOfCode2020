from itertools import permutations


def part1(report):
    for n1, n2 in permutations(report, 2):
        if (n1 + n2) == 2020:
            return n1 * n2


def part2(report):
    for n1, n2, n3 in permutations(report, 3):
        if (n1 + n2 + n3) == 2020:
            return n1 * n2 * n3


if __name__ == '__main__':
    report = []
    with open('inputs/01') as f:
        report = list(map(int, f.readlines()[:-1]))
    print('Part 1:', part1(report))
    print('Part 2:', part2(report))
