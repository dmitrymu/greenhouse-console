from PyQt6.QtWidgets import QWidget, QMainWindow, QTabWidget
from PyQt6 import QtCore
from PyQt6 import QtGui
from types import SimpleNamespace
from NodeView import NodeView

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        # layout = QVBoxLayout()

        # layout.addWidget(Color('red'))

        self.widget = QTabWidget()
        # widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.tabs = {}
    
    def addTab(self, name):
        tabView = NodeView()
        n = self.widget.addTab(tabView, name)
        self.tabs[name] = SimpleNamespace(index = n, view = tabView)
        return SimpleNamespace(index = n, view = tabView)


    @QtCore.pyqtSlot(str, str, dict)
    def updateView(self, node, group, sensors):
        if node not in self.tabs:
            self.addTab(node)
        tabView = self.tabs[node].view 
        if group not in tabView.groups:
            tabView.addPane(group)
        groupView = tabView.groups[group].view
        groupView.update(sensors)
