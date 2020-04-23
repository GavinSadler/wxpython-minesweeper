
import wx


class GameInfoFrame(wx.Frame):
    """
    A class representing a frame which shows the players score, a timer, number of bombs and flags,
    and other general game info, also having basic functionality to restart the game and access the settings menu
    """

    def __init__(self):
        super().__init__()
