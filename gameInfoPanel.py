
import wx
from minesweeper import Minesweeper


class GameInfoPanel(wx.Panel):
    """
    A class representing a frame which shows the players score, a timer, number of bombs and flags, and other general game info. 
    TODO: If someone could investigate a possibly more elegant way to do this, please let me know!
    """

    def __init__(self, parent, minesweeperInstance: Minesweeper):
        super().__init__(parent)

        self.minesweeperInstance = minesweeperInstance

        # Connect callback functions from Minesweeper to this class
        self.minesweeperInstance.onFlagPlaced(self.updateLabel)
        self.minesweeperInstance.onGameReset(self.updateLabel)
        self.minesweeperInstance.onFirstSpaceTouched(self.updateLabel)

        self.time = -1

        # Set up the graphical portion of the class
        horizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

        buttonFont = wx.Font(24, wx.FONTFAMILY_DEFAULT,
                             wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.statusLabel = wx.StaticText(self, label="--:-- ⏱ | 🚩 0/0")
        self.statusLabel.SetFont(buttonFont)

        horizontalSizer.AddStretchSpacer(1)
        horizontalSizer.Add(self.statusLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        horizontalSizer.AddStretchSpacer(1)

        self.SetSizer(horizontalSizer)

    def setTimerMode(self, timeLimit=-1):
        """
        Sets the mode for the timer to run with. 
        If timelimit > 0, the timer will be in countdown mode starting at that given time. 
        Otherwise, the timer will count up as the user plays. 
        The timer automatically starts/stops at the beginning and the end of a round.
        """

        if timeLimit > 0:
            self.timedMode = True
            self.time = timeLimit
        else:
            self.timedMode = False
            self.time = 0

    def updateLabel(self):
        """
        Updates game time and flag counter when called 
        This is automatically called by the setters in this function and the timer in this class
        """

        timeLabel = "--:--"

        # If we are keeping track of game time . . .
        if self.time != -1:

            timeLabel = ""

            # Make sure time has an added 0 before the minutes place if it's less than 10
            if int(self.time / 60) < 10:
                timeLabel = "0"

            timeLabel = timeLabel + str(int(self.time / 60)) + ":"

            # Ditto for minutes place
            if self.time % 60 < 10:
                timeLabel = timeLabel + "0"

            timeLabel = timeLabel + str(self.time % 60)

        numMines = self.minesweeperInstance.mineCount
        numFlags = self.minesweeperInstance.flagsUsed

        flagsLabel = str(numFlags) + "/" + str(numMines)

        self.statusLabel.SetLabel(timeLabel + " ⏱ | 🚩 " + flagsLabel)
