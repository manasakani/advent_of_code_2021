# Day 2, Dive!

def move(direc, num):

    global horizontal
    global depth

    if direc == 'forward':
        horizontal += num
    elif direc == 'down':
        depth += num
    elif direc == 'up':
        depth += -num
    else:
        pass


def move_aim(direc, num):

    global horizontal
    global depth
    global aim

    if direc == 'forward':
        horizontal += num
        depth += aim*num
    elif direc == 'down':
        aim += num
    elif direc == 'up':
        aim += -num
    else:
        pass


if __name__ == '__main__':

    direcs = []
    nums = []

    with open('commands.txt', 'r') as f:
        for line in f:
            direcs.append(line.split()[0])
            nums.append(int(line.split()[1]))

    # Part 1:
    horizontal = 0
    depth = 0
    aim = 0
    for direc, num in zip(direcs, nums):
        move(direc, num)

    print(f'Horizontal Position times depth = {horizontal*depth}')

    # Part 2:
    horizontal = 0
    depth = 0
    aim = 0

    for direc, num in zip(direcs, nums):
        move_aim(direc, num)

    print(f'Horizontal Position times depth = {horizontal*depth}')
