import numpy as np

if __name__ == '__main__':

    # Get input:
    og_bins = []
    with open('crab_positions_real.txt') as f:
        crab_positions = f.read().split(',')

    crab_positions = np.array([int(f) for f in crab_positions])

    # Part 1:

    min_fuel = float('inf')
    fuel_cost = 0

    for aligned_pos in range(max(crab_positions)+1):
        fuel_cost = sum(abs(crab_positions - aligned_pos))
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost

    print(f'Min Fuel is {min_fuel}')

    # Part 2:
