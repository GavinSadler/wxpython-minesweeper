
import wx
from minesweeper import Minesweeper


class GameInfoPanel(wx.Panel):
    """
    A class representing a frame which shows the players score, a timer, number of bombs and flags, and other general game info
    """

    def __init__(self, parent, minesweeperInstance: Minesweeper):
        super().__init__(parent)

        self.totalFlags = 0
        self.usedFlags = 0

        self.time = -1

        horizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

        buttonFont = wx.Font(24, wx.FONTFAMILY_DEFAULT,
                             wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        timeLabel = wx.StaticText(self, label="--:-- ⏱ | 🚩 0/0")
        timeLabel.SetFont(buttonFont)

        horizontalSizer.AddStretchSpacer(1)
        horizontalSizer.Add(timeLabel, 0, wx.ALIGN_CENTER_VERTICAL)
        horizontalSizer.AddStretchSpacer(1)

        self.SetSizer(horizontalSizer)
