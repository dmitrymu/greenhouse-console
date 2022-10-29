from PyQt6.QtWidgets import QWidget, QMainWindow, QTabWidget
from types import SimpleNamespace

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # layout = QVBoxLayout()

        # layout.addWidget(Color('red'))

        self.widget = QTabWidget()
        # widget.setLayout(layout)
        self.setCentralWidget(self.widget)
    
    def addTab(self, name, data):
        tabView = QWidget()
        n = self.widget.addTab(tabView, name)
        return SimpleNamespace(index = n, view = tabView)

