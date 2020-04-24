
import wx
from minesweeper import Minesweeper
from minefieldPanel import MinefieldPanel
from gameInfoPanel import GameInfoPanel


class MinesweeperApp(wx.App):

    def __init__(self):
        super().__init__()

        frame = wx.Frame(None, title="Minesweeper",
                         pos=(30, 30), size=(800, 600))

        width = 10
        height = 10

        verticalContainer = wx.BoxSizer(wx.VERTICAL)

        minesweeper = Minesweeper(width, height, 15)

        gameInfo = GameInfoPanel(frame, minesweeper)
        gameInfo.updateLabel()
        verticalContainer.Add(gameInfo, proportion=0, flag=wx.EXPAND)

        mineField = MinefieldPanel(frame, minesweeper)
        verticalContainer.Add(mineField, proportion=1, flag=wx.EXPAND)

        frame.SetSizer(verticalContainer)

        frame.Show()
