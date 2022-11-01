from PyQt5.QtWidgets import QMainWindow
from SysemView import SystemView

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.widget = SystemView()
        self.setCentralWidget(self.widget)

    def getSystemView(self):
        return self.widget
