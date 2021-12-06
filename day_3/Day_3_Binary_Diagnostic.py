# Day 3, Binary Diagnostic

def bin_to_dec(bin):

    dec = 0
    for it, digit in enumerate(bin[::-1]):
        dec = dec+(2**it)*int(digit)

    return dec


if __name__ == '__main__':

    og_bins = []
    with open('numbers.txt', 'r') as f:
        for line in f:
            og_bins.append(line.split()[0])

    bins = list(map(list, zip(*og_bins)))
    bins = [[int(i) for i in column] for column in bins]

    # Part 1:
    gamma = []
    epsilon = []
    for column in bins:
        if sum(column) > 0.5*len(column):
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    gamma = bin_to_dec(gamma)
    epsilon = bin_to_dec(epsilon)

    print(f'Gamma = {gamma}')
    print(f'Epsilon = {epsilon}')
    print(f'Power Consumption = {gamma*epsilon}')

    # Part 2:

    remains = og_bins
    counter = 0
    while len(remains) > 1:

        # Update cols
        bins = list(map(list, zip(*remains)))
        bins = [[int(i) for i in column] for column in bins]
        col = bins[counter]

        # Update remaining bins
        cond = 1 if sum(bins[counter]) >= 0.5*len(bins[counter]) else 0
        inds = [i for i in range(len(col)) if col[i] == cond]
        remains = [remains[ind] for ind in inds]
        counter += 1

    oxgen_rating = bin_to_dec(remains[0])
    print(f'Oxygen generator rating = {oxgen_rating}')

    remains = og_bins
    counter = 0
    while len(remains) > 1:

        # Update cols
        bins = list(map(list, zip(*remains)))
        bins = [[int(i) for i in column] for column in bins]
        col = bins[counter]

        # Update remaining bins
        cond = 0 if sum(bins[counter]) >= 0.5*len(bins[counter]) else 1
        inds = [i for i in range(len(col)) if col[i] == cond]
        remains = [remains[ind] for ind in inds]
        counter += 1

    co2scrubber_rating = bin_to_dec(remains[0])
    print(f'C02 scrubber rating = {co2scrubber_rating}')

    print(f'Life Support Rating = {oxgen_rating*co2scrubber_rating}')
