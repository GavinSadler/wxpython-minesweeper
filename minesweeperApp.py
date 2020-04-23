
import wx
from minesweeper import Minesweeper
from minefieldPanel import MinefieldPanel


class MinesweeperApp(wx.App):

    def __init__(self):
        super().__init__()

        self.frame = wx.Frame(None, title="Minesweeper",
                              pos=(30, 30), size=(800, 600))

        self.width = 15
        self.height = 15

        self.minesweeper = Minesweeper(self.width, self.height, 15)

        self.mineField = MinefieldPanel(self.frame, self.minesweeper)

        self.frame.Show()
