

import random


class MineField():
    '''A class representing a 2d array mineField with a width given by the width parameter and a height given by the hight parameter.'''

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.mineField = []

        self.reset()  # Initializes the empty 2d array self.mineField

    def generateMines(self, x, y, mineCount):
        '''Generates mines on the mineField, avoiding a 3 by 3 area around the position (x, y). The number of mines generated is dictated by mineCount.'''

        mines = mineCount

        while mines:
            rx = random.randint(0, self.width - 1)
            ry = random.randint(0, self.height - 1)

            # Make sure there is no mine at the randomly selected location and that the mine is placed outside of the 3x3 location surrounding the first touche's location
            if self.mineField[rx][ry] == 0 and (rx > x + 1 or rx < x - 1) and (ry > y + 1 or ry < y - 1):

                # A value of -1 indicated a mine at this location
                self.mineField[rx][ry] = -1

                mines = mines - 1

    def get(self, x, y):
        '''Gets the number on the space of the mineField at position (x, y). -1 denotes a mine, and 0-8 denotes the amount of mines surrounding the space'''

        # Check to see if a mine is at this space
        if self.mineField[x][y] == -1:
            return -1

        # Otherwise, we need to count how many mines surround the space
        mineCount = 0

        # These for loops in conjunction will check the 3 by 3 area surrounding the space
        for a in range(-1, 2):
            for b in range(-1, 2):

                # Make sure that the spaces being checked are not outside the bounds of the mineField array
                if x + a >= 0 and x + a < 10 and y + b >= 0 and y + b < 10:

                    # Increase minecount if the given position is a mine
                    if self.mineField[x + a][y + b] == -1:
                        mineCount = mineCount + 1

        return mineCount

    def getMines(self):
        '''Returns a list of tuples of the positions of all the mines on the map'''

        output = []

        for x in range(0, self.width):
            for y in range(0, self.height):

                # Add the position to the tuple if the space is a mine
                if self.mineField[x][y] == -1:
                    output.append((x, y))

        return output

    def reset(self):
        '''Resets the mineField to have all empty spaces'''

        self.mineField = []

        for x in range(0, self.width):

            # Add a new row to the mineField array
            self.mineField.append([])

            for y in range(0, self.height):

                # Fill the mineField with empty spaces
                self.mineField[x].append(0)
