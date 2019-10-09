# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: World Series Batting Averages
# Peter Mitzel, Austin Hull
# Last Modified: 11/21/17
# -------------------------------------------------
# This program will take a file with names and stats
# and give you their batting average as well as name
# and position. It will also give you their total
# hits and at bats.
#--------------------------------------------------

import numpy as np

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

class Batter(Person):
    def __init__(self, first_name, last_name, position, at_bats=0, hits=0):
        super().__init__(first_name, last_name)
        self.position = position
        self.at_bats = 0
        self.hits = 0

    def get_position(self):
        return self.position

    def get_at_bats(self):
        return self.at_bats

    def get_hits(self):
        return self.hits

    def get_batting_average(self):
        if self.at_bats == 0:
            return 0.0
        return self.hits / self.at_bats

    def add_hits(self, extra):
        self.hits += extra

    def add_at_bats(self, extra):
        self.at_bats += extra

class All_Batters:
    def __init__(self, players, file):
        self.players = players
        self.batters = np.ndarray([players], dtype=Batter)
        for i in range(players):
           batter = file.readline().split(',')
           b1 = Batter(batter[0], batter[1], batter[2])
           self.batters[i] = b1
    def print_information(self):
        print('Player'.ljust(25) + 'Batting Average')
        print('----------------------------------------')
        for i in range(0, self.players):
            print((self.batters[i].first_name + ' ' + self.batters[i].last_name +
              '(' + self.batters[i].position.strip() + ')').ljust(25) +
                  '{:.3f}'.format(self.batters[i].get_batting_average()) + ' ' + '(' +
                  str(self.batters[i].get_hits()) + ' ' 'for' + ' ' +
                  str(self.batters[i].get_at_bats()) + ')')

    def update_batters(self, stats):
        for items in self.batters:
            if items.get_first_name() == stats[0]:
                if items.get_last_name() == stats[1]:
                    items.add_hits(int(stats[4]))
                    items.add_at_bats(int(stats[3]))
                    items.get_batting_average()
                

def main(some_file):
    file = open(some_file, 'r')
    players = file.readline()
    players = int(players)
    temp = All_Batters(players, file)
    temp.print_information()
    for items in file:
        stats = items.strip().split(',')
        temp.update_batters(stats)
    print()
    temp.print_information()


main('batting.txt')
