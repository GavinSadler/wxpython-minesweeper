
import wx
from minefield import MineField


class App(wx.App):

    def __init__(self):

        super().__init__()

        frame = wx.Frame(None, title="Minesweeper",
                         pos=(30, 30), size=(800, 600))
        panel = wx.Panel(frame)

        # Grid sizer which will automatically size all of the buttons in the frame
        self.grid = wx.GridSizer(10, 10, 3, 3)

        # Empty 2d array to store buttons
        self.buttons = []

        # The font instance which will be used for the button labels
        buttonFont = wx.Font(24, wx.FONTFAMILY_DEFAULT,
                             wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.mineField = MineField(10, 10)
        self.firstClick = True

        for x in range(0, 10):
            # This will add a new column to the lists buttons, minefield, and gamefield
            self.buttons.append([])

            for y in range(0, 10):
                # This will add a new button to the same list
                self.buttons[x].append(wx.Button(panel, 10000 + (y * 10 + x)))

                # This will actually add the new button to the sizer
                self.grid.Add(self.buttons[x][y], 0, wx.EXPAND)

                # This will bind our button to a function and give it a font
                self.buttons[x][y].Bind(wx.EVT_BUTTON, self.onButtonClicked)
                self.buttons[x][y].Bind(wx.EVT_RIGHT_UP, self.onRightClicked)
                self.buttons[x][y].SetFont(buttonFont)

        panel.SetSizer(self.grid)

        frame.Show()

    def onButtonClicked(self, event):

        x = int((event.GetId() - 10000) % 10)
        y = int((event.GetId() - 10000) / 10)

        # If there is a flag on the space, we don't want to be able to step on that mine
        if self.buttons[x][y].GetLabel() != "🚩":

            # We need to randomly spread bombs across the minefield when the user first clicks
            if self.firstClick:

                self.mineField.generateMines(x, y, 30)

                # Now that the mines have been placed, we need to make sure they are not generated again
                self.firstClick = False

            # When the user clicks on a mine . . .
            if self.mineField.get(x, y) == -1:

                # Grab each position from the mines returned by getMines and set the button labels to be bomb emojis
                for mine in self.mineField.getMines():
                    self.buttons[mine[0]][mine[1]].SetLabel("💣")

                wx.MessageBox("Kaboom! You stepped on a mine! Game over!")

                # Reset first click to generate new mines
                self.firstClick = True

                # Reset the mine field
                self.mineField.reset()

            else:

                number = self.mineField.get(x, y)

                self.buttons[x][y].SetLabel(str(number) if number > 0 else "")
                self.buttons[x][y].Enable(False)

        event.Skip()

    def onRightClicked(self, event):

        x = int((event.GetId() - 10000) % 10)
        y = int((event.GetId() - 10000) / 10)

        if self.buttons[x][y].GetLabel() == "🚩":
            self.buttons[x][y].SetLabel("")
        else:
            self.buttons[x][y].SetLabel("🚩")

        event.Skip()


if __name__ == "__main__":
    app = App()
    app.MainLoop()
