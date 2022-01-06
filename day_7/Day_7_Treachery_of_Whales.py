import numpy as np

if __name__ == '__main__':

    # Get input:
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

    print(f'Part 1 Min Fuel is {min_fuel}')

    # Part 2:

    min_fuel = float('inf')
    fuel_cost = 0

    for aligned_pos in range(max(crab_positions)+1):
        difference = abs(crab_positions - aligned_pos)
        fuel_cost = sum((1 + d)*d/2 for d in difference)

        if fuel_cost < min_fuel:
            min_fuel = fuel_cost

    print(f'Part 2 Min Fuel is {min_fuel}')
