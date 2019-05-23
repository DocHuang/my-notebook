"""
继承界面文件 MainWin.py

Version：0.1
Author：D.H.
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.MainWin import *


class NoteMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(NoteMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    noteWin = NoteMainWindow()
    noteWin.show()
    sys.exit(app.exec_())
