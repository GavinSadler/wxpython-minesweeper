
import wx
from minesweeper import Minesweeper


class MinefieldPanel(wx.Panel):
    """
    A class representing a frame of buttons where the minefield for the minesweeper program is located
    This class handles all of the button presses
    """

    def __init__(self, parent, minesweeperInstance: Minesweeper):
        super().__init__(parent)

        self.mineField = minesweeperInstance
        self.width = self.mineField.width
        self.height = self.mineField.height

        # Grid sizer which will automatically size all of the buttons in the frame
        self.grid = wx.GridSizer(self.width, self.height, 0, 0)

        # Empty 2d array to store buttons
        self.buttons = []

        # The font instance which will be used for the button labels
        buttonFont = wx.Font(24, wx.FONTFAMILY_DEFAULT,
                             wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        for x in range(0, self.width):
            # This will add a new column to the lists buttons, minefield, and gamefield
            self.buttons.append([])

            for y in range(0, self.height):
                # This will add a new button to the same list
                self.buttons[x].append(
                    wx.Button(self, 10000 + (y * self.width + x)))

                # This will actually add the new button to the sizer
                self.grid.Add(self.buttons[x][y], 0, wx.EXPAND)

                # This will bind our button to a function and give it a font
                self.buttons[x][y].Bind(wx.EVT_BUTTON, self.onButtonClicked)
                self.buttons[x][y].Bind(wx.EVT_RIGHT_UP, self.onRightClicked)
                self.buttons[x][y].SetFont(buttonFont)

        self.SetSizer(self.grid)

    def touchSpace(self, x, y):
        """
        A wrapper for the touchSpace function in MineField which will update all the button labels
        in this panel's context upon touching a space and its resulting recursive search
        """

        spacesToUpdate = self.mineField.touchSpace(x, y)

        # Update all the buttons which were recusively searched
        for space in spacesToUpdate:

            nx = space[0]
            ny = space[1]

            value = self.mineField.uncoverSpace(nx, ny)

            self.buttons[nx][ny].SetLabel(str(value) if value > 0 else "")
            self.buttons[nx][ny].Enable(False)

    def onButtonClicked(self, event):

        x = int((event.GetId() - 10000) % self.width)
        y = int((event.GetId() - 10000) / self.height)

        # Previously used to debug what space on the minefield that was touched
        #print(str(x) + "\t" + str(y))

        # When the user clicks on a mine . . .
        if self.mineField.uncoverSpace(x, y) == -3:

            # Grab each mine position returned by getMinePositions and set the button labels to be bomb emojis
            for mine in self.mineField.getMinePositions():
                self.buttons[mine[0]][mine[1]].SetLabel("💣")

            wx.MessageBox("Kaboom! You stepped on a mine! Game over!")

            # Reset all the buttons in the GUI
            for buttonGroup in self.buttons:
                for button in buttonGroup:
                    button.SetLabel("")
                    button.Enable(True)

            # Reset the mine field
            self.mineField.reset()

        # Every other space can try a recursive search, since it will just end the search at the first space
        else:

            self.touchSpace(x, y)

        event.Skip()

    def onRightClicked(self, event):

        x = int((event.GetId() - 10000) % self.width)
        y = int((event.GetId() - 10000) / self.height)

        self.mineField.toggleFlag(x, y)

        value = self.mineField.uncoverSpace(x, y)

        if value == -2 or value == -1:
            self.buttons[x][y].SetLabel("🚩")
        else:
            self.buttons[x][y].SetLabel("")

        event.Skip()
