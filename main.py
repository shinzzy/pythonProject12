import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox, QApplication
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore
from PyQt5 import uic

ui_form = uic.loadUiType("main.ui")[0]

print("qqqqq")
a = input()

print(a)



class ChatWindow(QMainWindow, ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




if __name__ == "__main__":
    if a == "1":
        app = QApplication(sys.argv)
        myWindow = ChatWindow()
        myWindow.show()
        app.exec_()