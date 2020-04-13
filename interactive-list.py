
import wx


class App(wx.App):
    def __init__(self):
        super().__init__()

        frame = wx.Frame(None, title="My List App", pos=(30, 30), size=(800, 600))
        panel = wx.Panel(frame)

        self.button = wx.Button(panel, label="Add to the list", pos=(10, 10), size=(150, 50))
        self.textBox = wx.TextCtrl(panel, pos=(10, 70), size=(300, 30))
        self.listBox = wx.ListBox(panel, pos=(10, 110), size=(300, 300))

        self.button.Bind(wx.EVT_BUTTON, self.onButtonClicked)

        frame.Show()

    def onButtonClicked(self, event):
        self.listBox.Append(self.textBox.GetLineText(0))


if __name__ == "__main__":
    app = App()
    app.MainLoop()
