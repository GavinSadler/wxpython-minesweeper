
import wx


class SettingsDialog(wx.Dialog):
    """
    A class representing the settings menu where the player can edit settings for the game. 
    I unfortunately succumbed to the lustful ways of wxFormBuilder. It is an awesome tool but beware of what lies below . . .
    """

    def __init__(self):
        super().__init__(None, title="Game options",
                         style=wx.STAY_ON_TOP | wx.DEFAULT_DIALOG_STYLE, size=wx.Size(200, 400))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        difficultyModeChoices = [u"Easy", u"Medium", u"Hard", u"Custom"]
        self.difficultyMode = wx.RadioBox(self, wx.ID_ANY, u"Game Difficulty", wx.DefaultPosition,
                                          wx.Size(-1, -1), difficultyModeChoices, 1, wx.RA_SPECIFY_COLS)
        self.difficultyMode.SetSelection(1)
        bSizer7.Add(self.difficultyMode, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 20)

        gSizer1 = wx.GridSizer(3, 2, 5, 0)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"Width", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.Enable(False)

        gSizer1.Add(self.m_staticText3, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 0)

        self.width = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            80, -1), wx.SP_ARROW_KEYS, 5, 45, 15)
        self.width.Enable(False)

        gSizer1.Add(self.width, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_staticText31 = wx.StaticText(
            self, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)

        self.m_staticText31.Enable(False)

        gSizer1.Add(self.m_staticText31, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 0)

        self.height = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            80, -1), wx.SP_ARROW_KEYS, 5, 45, 15)
        self.height.Enable(False)

        gSizer1.Add(self.height, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        self.m_staticText32 = wx.StaticText(
            self, wx.ID_ANY, u"Mines", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.Enable(False)

        gSizer1.Add(self.m_staticText32, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 0)

        self.bombs = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            80, -1), wx.SP_ARROW_KEYS, 0, 100, 20)
        self.bombs.Enable(False)

        gSizer1.Add(self.bombs, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 0)

        bSizer7.Add(gSizer1, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer4.Add(self.m_staticline1, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        timerModeChoices = [u"Countdown", u"Stopwatch"]
        self.timerMode = wx.RadioBox(self, wx.ID_ANY, u"Timer Mode", wx.DefaultPosition,
                                     wx.DefaultSize, timerModeChoices, 1, wx.RA_SPECIFY_COLS)
        self.timerMode.SetSelection(0)
        bSizer11.Add(self.timerMode, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL, 20)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, u"Time Limit", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.Enable(False)

        bSizer3.Add(self.m_staticText4, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 5)

        self.timeLimit = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            80, -1), wx.SP_ARROW_KEYS, 0, 100, 5.000000, 1)
        self.timeLimit.SetDigits(0)
        self.timeLimit.Enable(False)

        bSizer3.Add(self.timeLimit, 0, wx.ALL |
                    wx.ALIGN_CENTER_VERTICAL, 20)

        bSizer11.Add(bSizer3, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.m_staticline11 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer4.Add(self.m_staticline11, 0, wx.EXPAND | wx.ALL, 5)

        self.submitButton = wx.Button(
            self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.submitButton, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        self.SetSizerAndFit(bSizer4)

        self.ShowModal()
