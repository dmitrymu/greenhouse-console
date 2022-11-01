from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QGridLayout, QLabel, QTabWidget, QSizePolicy
from .GroupView import GroupView
from types import SimpleNamespace as SN


class NodeView(QWidget):

    def __init__(self):
        super(NodeView, self).__init__()

        layout = QVBoxLayout()
        layout.addStretch()
        self.setLayout(layout)
        self.groups = {}

    def addPane(self, name):
        pane = QGroupBox(name)
        pane.setLayout(QVBoxLayout())
        vlist = GroupView()
        pane.layout().addWidget(vlist)
        self.layout().insertWidget(self.layout().count() - 1, pane)
        self.groups[name] = SN(root = pane, view = vlist)
