from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QTableWidget
from types import SimpleNamespace

class NodeView(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

    def addPane(self, name):
        pane = QGroupBox(name)
        pane.setLayout(QVBoxLayout())
        vlist = QTableWidget()
        vlist.setColumnCount(2)
        vlist.setHorizontalHeaderLabels(["Sensor", "Value"]) 
        pane.layout().addWidget(vlist)
        self.layout().addWidget(pane)
        return SimpleNamespace(root = pane, view = vlist)
        