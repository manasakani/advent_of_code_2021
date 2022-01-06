
if __name__ == '__main__':

    # Get input:
    output_lines = []
    with open('input.txt') as f:
        for line in f:
            output_lines.append(line.split()[-4:])

    digit_length = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unique_digits = [digit_length[1], digit_length[4],
                     digit_length[7], digit_length[8]]

    output = [item for sublist in output_lines for item in sublist]

    # Part 1:
    
    counter = 0
    for string in output:
        if len(string) in unique_digits:
            counter += 1

    print(f'There are {counter} instances of the unique digits')
