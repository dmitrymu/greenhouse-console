from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QTableWidget
from types import SimpleNamespace

class GroupView(QTableWidget):

    def __init__(self):
        super(GroupView, self).__init__()
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Sensor", "Value"]) 

    def update(self, sensors):
            self.clearContents()
            self.setRowCount(len(sensors))
            self.setVerticalHeaderLabels(list(sensors.keys()))

class NodeView(QWidget):

    def __init__(self):
        super(NodeView, self).__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.groups = {}

    def addPane(self, name):
        pane = QGroupBox(name)
        pane.setLayout(QVBoxLayout())
        vlist = GroupView()
        pane.layout().addWidget(vlist)
        self.layout().addWidget(pane)
        self.groups[name] = SimpleNamespace(root = pane, view = vlist)
        #return SimpleNamespace(root = pane, view = vlist)
        