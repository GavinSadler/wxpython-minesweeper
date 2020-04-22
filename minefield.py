
import random


class MineField():
    """ A class representing a 2d array mineField with a width given by the width parameter and a height given by the hight parameter.
        Each space in the minefield can take on any of the following values:
             -4 : untouched space
             -3 : bomb
             -2 : flag on untouched space
             -1 : flag on bomb
              0 : clear space (0 surrounding mines)
            1-8 : indicates the number of surrounding mines
    """


    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.mineField = []

        self.reset()  # Initializes the empty 2d array self.mineField


    def generateMines(self, x, y, mineCount):
        ''' Generates mines on the mineField, avoiding a 3 by 3 area around the position (x, y). The number of mines generated is dictated by mineCount '''

        mines = mineCount

        while mines:
            rx = random.randint(0, self.width - 1)
            ry = random.randint(0, self.height - 1)

            # Make sure there is no mine at the randomly selected location and that the mine is placed outside of the 3x3 location surrounding the first touche's location
            if self.mineField[rx][ry] == -4 and (rx > x + 1 or rx < x - 1) and (ry > y + 1 or ry < y - 1):

                # A value of -1 indicated a mine at this location
                self.mineField[rx][ry] = -3

                mines = mines - 1


    def getValue(self, x, y):
        """ Gets the value on the space of the mineField at position (x, y) denoting the number of surrounding mines
            If the space is still a hidden space (with a value of -4) it will be unconvered and assigned the number of surrounding mines
            If the space is a special space (Anything less than 0) then it will just be returned"""

        # Check to see if this space has been uncovered yet or if it's a special space, since we wouldn't have to do calculations
        if self.mineField[x][y] != -4:
            return self.mineField[x][y]

        # Otherwise, we need to count how many mines surround the space
        mineCount = 0

        # These for loops in conjunction will check the 3 by 3 area surrounding the space
        for a in range(-1, 2):
            for b in range(-1, 2):

                # Translate our starting position to get to the next adjacent position
                nx = x + a
                ny = y + b

                # Make sure that the spaces being checked are not outside the bounds of the mineField array
                if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height:

                    # Increase minecount if the given position is a mine
                    if self.mineField[nx][ny] == -3 or self.mineField[nx][ny] == -1:
                        mineCount = mineCount + 1

        # We want to add the new uncovered value to the minefield
        self.mineField[x][y] = mineCount

        return mineCount


    def toggleFlag(self, x, y):
        ''' Toggles a flag on a given location on the minefield. If a flag cannot be toggled (Its an uncovered space), nothing will change '''

        spaceValue = self.mineField[x][y]

        # Flags must be placed untouched spaces or bombs
        if spaceValue == -4 or spaceValue == -3:
            
            # Flag spaces are 2 values more from their corresponding spaces, so add 2
            self.mineField[x][y] = self.mineField[x][y] + 2

        # If there is already a flag on those spaces . . .
        elif spaceValue == -2 or spaceValue == -1:

            # Nonflag spaces are 2 more than flag space, so subtract 2
            self.mineField[x][y] = self.mineField[x][y] - 2


    def getMinePositions(self):
        ''' Returns a list of tuples of the positions of all the mines on the map, used to display where mines were at the end of a game '''

        output = []

        for x in range(0, self.width):
            for y in range(0, self.height):

                # Add the position to the tuple if the space is a mine
                if self.mineField[x][y] == -3:
                    output.append((x, y))

        return output


    def recursiveSearch(self, x, y):
        """ Recusively searches the minefield starting at a given position (x, y), which must be an untouched space with 0 mines surrounding it
            For every space which is a 0 mines untouched space, it then recusively searches that space with this same function
            This method should clear out spaces which are obviously not mines
            Returns a list of tuples of the positions of all of the recursively cleared spaces """
    
        firstSpaceValue = self.getValue(x, y)

        # If the given space is not a space with no surrounding mines (There is a number on the space),
        # then we just return the one position of the space. This allows us to use this function whenever
        # we need to check a space
        if firstSpaceValue != 0:
            return [(x, y)]

        touchedSpaces = []

        # This part of the code is isolated into its own function since it needs to be recursively called
        def search(x, y):

            # These for loops in conjunction will check the 3 by 3 area surrounding the space
            for a in range(-1, 2):
                for b in range(-1, 2):

                    # Translate our starting position to get to the next adjacent position
                    nx = x + a
                    ny = y + b

                    # Make sure that the spaces being checked are not outside the bounds of the mineField array
                    if nx >= 0 and nx < self.width and ny >= 0 and ny < self.height:

                        touchedSpaces.append((nx, ny))

                        # If the space has not been uncovered and has no surrounding mines, then we can just clear its adjacent spaces as well
                        # This is where recursion takes place, since we are doing the same process
                        if (self.mineField[nx][ny] == -4 or self.mineField[nx][ny] == -2) and self.getValue(nx, ny) == 0:
                            search(nx, ny)

        search(x, y)

        # When all is said and done, we now have an array with every mine we touched so the front end can update its new state
        return touchedSpaces


    def reset(self):
        ''' Resets the mineField to have all empty spaces '''

        self.mineField = []

        for x in range(0, self.width):

            # Add a new row to the mineField array
            self.mineField.append([])

            for y in range(0, self.height):

                # Fill the mineField with empty spaces
                self.mineField[x].append(-4)
