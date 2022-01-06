class Fish():

    def __init__(self, timer=8):
        self.timer = timer

    def get_older(self):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer += -1


if __name__ == '__main__':

    # Get input:
    og_bins = []
    with open('fish.txt') as f:
        fish_timers = f.read().split(',')

    fish_timers = [int(f) for f in fish_timers]

    # Initialize the school:
    school = []
    for time in fish_timers:
        school.append(Fish(time))

    # Iterate through time
    day = 0
    while day < 80:
        day += 1

        new_fish = []
        for fish in school:
            if fish.timer == 0:
                new_fish.append(Fish())
            fish.get_older()

        # Add the new fish to the school
        school += new_fish

    print(f'There are {len(school)} fish in the school!')
