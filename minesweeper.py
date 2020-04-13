
import wx
import random


class App(wx.App):
    def __init__(self):
        super().__init__()

        frame = wx.Frame(None, title="My List App", pos=(30, 30), size=(800, 600))
        panel = wx.Panel(frame)

        # Grid sizer which will automatically size all of the buttons in the frame
        self.grid = wx.GridSizer(10, 10, 3, 3)

        # Empty 2d array to store buttons
        self.buttons = []

        # The font instance which will be used for the button labels
        buttonFont = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        # Empty 2d array to store the mines in the game
        # We start off empty since we want to initialize our mine field after the user clicks one time, otherwise their first click may be a mine and the player will lose without a chance to play :(
        self.mineField = []
        self.firstClick = True

        for x in range(0, 10):
            # This will add a new column to the lists buttons, minefield, and gamefield
            self.buttons.append([])
            self.mineField.append([])

            for y in range(0, 10):
                # This will add a new button to the same list
                self.buttons[x].append(wx.Button(panel, 10000 + (y * 10 + x)))

                # This will actually add the new button to the sizer
                self.grid.Add(self.buttons[x][y], 0, wx.EXPAND)

                # This will bind our button to a function and give it a font
                self.buttons[x][y].Bind(wx.EVT_BUTTON, self.onButtonClicked)
                self.buttons[x][y].SetFont(buttonFont)

                # This will initialize our minefield and gamefield to be empty at first
                self.mineField[x].append(0)

        panel.SetSizer(self.grid)

        frame.Show()

    def onButtonClicked(self, event):
        x = int((event.GetId() - 10000) % 10)
        y = int((event.GetId() - 10000) / 10)

        if self.firstClick:
            mines = 30

            while mines:
                rx = random.randint(0, 9)
                ry = random.randint(0, 9)

                if self.mineField[rx][ry] == 0 and rx != x and ry != y:

                    # A value of -1 indicated a mine at this location
                    self.mineField[rx][ry] = -1

                    mines = mines - 1

            # Now that the mines have been placed, we need to make sure they are not generated again
            self.firstClick = False

        if self.mineField[x][y] == -1:

            for a in range(0, 10):
                for b in range(0, 10):
                    if self.mineField[a][b] == -1:
                        self.buttons[a][b].SetLabel("💣")

            wx.MessageBox("Kaboom! You stepped on a mine! Game over!")

            # Reset first click to generate new mines
            self.firstClick = True

            # Reset the mine field
            for a in range(0, 10):
                for b in range(0, 10):
                    self.mineField[a][b] = 0
                    self.buttons[a][b].SetLabel("")
                    self.buttons[a][b].Enable(True)

        else:
            mineCount = 0

            for a in range(-1, 2):
                for b in range(-1, 2):
                    if x + a >= 0 and  x + a < 10 and y + b >= 0 and y + b < 10:
                        if self.mineField[x + a][y + b] == -1:
                            mineCount = mineCount + 1

            self.buttons[x][y].SetLabel(str(mineCount) if mineCount > 0 else "")
            self.buttons[x][y].Enable(False)
        
        event.Skip()




if __name__ == "__main__":
    app = App()
    app.MainLoop()
