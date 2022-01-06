
if __name__ == '__main__':

    # Get input:
    output_lines = []
    input_lines = []
    with open('input.txt') as f:
        for line in f:
            output_lines.append(line.split()[-4:])
            input_lines.append(line.split()[:10])

    digit_length = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_digits = [digit_length[1], digit_length[4],
                     digit_length[7], digit_length[8]]

    # Part 1:

    output = [item for sublist in output_lines for item in sublist]

    counter = 0
    for string in output:
        if len(string) in unique_digits:
            counter += 1

    print(f'There are {counter} instances of the unique digits')

    # Part 2:

    number_codes = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
                    'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

    for input in input_lines:

        # Sort the input in order of increasing character size:
        input.sort(key=len)

        # Sort the input strings
        for ind in range(len(input)):
            input[ind] = ''.join(sorted(input[ind]))

        # Initialize the code that solves this input
        code = 'xxxxxxxxxx'
        slots = [[], [], [], [], [], [], [], [], [], []]

        # Find all the possible numbers and store them in the code
        for string in input:
            for loc, ind in enumerate(digit_length):
                if len(string) == ind:
                    slots[loc].append(string)

        # Slots contains the possible matches for every digit
        

        print(input)
        print(slots)
        sdfg

        print(input)
        dfg
