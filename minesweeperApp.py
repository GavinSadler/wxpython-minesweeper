
import wx
from minesweeper import Minesweeper
from minefieldPanel import MinefieldPanel
from gameInfoPanel import GameInfoPanel
from settingsDialog import SettingsDialog


class MinesweeperApp(wx.App):

    def __init__(self):
        super().__init__()

        frame = wx.Frame(None, title="Minesweeper",
                         pos=(30, 30), size=(800, 600))

        gameWidth = 10
        gameHeight = 10
        numMines = 15

        self.resetButtonId = 100
        self.settingsMenuId = 200

        # Menu bar definitions
        menuBar = wx.MenuBar()

        menu = wx.Menu()

        resetGame = wx.MenuItem(menu, self.resetButtonId, "Reset")
        menu.Append(resetGame)

        openOptions = wx.MenuItem(menu, self.settingsMenuId, "Options")
        menu.Append(openOptions)

        menuBar.Append(menu, "Game")

        frame.SetMenuBar(menuBar)
        frame.Bind(wx.EVT_MENU, self.menuHandler)

        # Start of program body definitions
        verticalContainer = wx.BoxSizer(wx.VERTICAL)

        self.minesweeper = Minesweeper(gameWidth, gameHeight, numMines)

        gameInfo = GameInfoPanel(frame, self.minesweeper)
        gameInfo.updateLabel()  # Make sure the label is updated when the game starts
        verticalContainer.Add(gameInfo, proportion=0, flag=wx.EXPAND)

        mineField = MinefieldPanel(frame, self.minesweeper)
        verticalContainer.Add(mineField, proportion=1, flag=wx.EXPAND)

        frame.SetSizer(verticalContainer)

        # Make sure application actually closes when user exits
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        frame.Show()

    def menuHandler(self, event):

        if event.GetId() == self.resetButtonId:
            self.minesweeper.reset()
        elif event.GetId() == self.settingsMenuId:
            SettingsDialog()
