# Day 1, Sonar Sweep

m = []
with open('measurements.txt', 'r') as f:
    for line in f:
        m.append(int(line))


def goes_up(m):
    diffs = [j-i for i, j in zip(m[1:], m[:-1])]
    count = len([1 for diff in diffs if diff < 0])
    return count


if __name__ == '__main__':

    print(f'Part 1: There are {goes_up(m)} measurements')

    windows = [i+j+k for i, j, k in zip(m[:-2], m[1:-1], m[2:])]
    print(f'Part 2: There are {goes_up(windows)} measurements')
