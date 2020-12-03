def part1(passwords):
    valid_passwords = 0
    for policy, password in passwords:
        password = password.rstrip('\n')
        min_max, char = policy.split(' ')
        min_c, max_c = min_max.split('-')
        if int(min_c) <= password.count(char) <= int(max_c):
            valid_passwords += 1
    return valid_passwords


def part2(passwords):
    valid_passwords = 0
    for policy, password in passwords:
        password = password.rstrip('\n')
        positions, char = policy.split(' ')
        pos1, pos2 = positions.split('-')
        if (password[int(pos1) - 1] == char) ^ (password[int(pos2) - 1] == char):
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    passwords = []
    with open('inputs/02') as f:
        passwords = list(map(lambda l: l.split(': '), f.readlines()))
    print(part1(passwords))
    print(part2(passwords))
