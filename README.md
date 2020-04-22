# wxpython-minesweeper

wxpython-minesweeper is an implementation of the Minesweeper game using Python and wxPython

This project is based on a video from [OneLoneCoder](https://github.com/OneLoneCoder) entitled [Cross Platform Graphical User Interfaces in C++](https://www.youtube.com/watch?v=FOIbK4bJKS8)

## Features

- A fixed 20 by 20 grid of buttons
- 30 mines to seek out
- A dynamically sized window

## Build Instructions

To package an executable of this Minesweeper game, execute the following command

`python -OO -m PyInstaller main.py --onefile --windowed --name Minesweeper`

This will then output an executable of the Minesweeper program. The executable can be found in `dist/Minesweeper.exe`

## Todo

- Add a settings menu with the ability to change the size of the grid and number of mines
- A timed mode
- Add a counter to count how many mines have been accounted for and how many mines remain
- A proper win state
