from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTabWidget
from .NodeView import NodeView
from types import SimpleNamespace as SN

class SystemView(QWidget):

    def __init__(self):
        super(SystemView, self).__init__()
        self.nodes = QTabWidget()
        self.status = QLabel("???")
        self.status.setStyleSheet(self.status.styleSheet()
                                  + "QLabel { font-weight: bold; }")
        layout = QVBoxLayout()
        layout.addWidget(self.nodes, stretch=1)
        layout.addStretch()
        layout.addWidget(self.status, stretch=0)
        self.setLayout(layout)
        self.tabs = {}
    
    def addNodeTab(self, name):
        tabView = NodeView()
        n = self.nodes.addTab(tabView, name)
        self.tabs[name] = SN(index = n, view = tabView)
        return self.tabs[name]

    @QtCore.pyqtSlot(bool, str)
    def updateConnectionStatus(self, isConnect, msg):
        self.status.setText(msg)
        self.status.setStyleSheet(
            self.status.styleSheet() +
            ("QLabel { color: green; }" if isConnect else "QLabel { color: red; }"))


    @QtCore.pyqtSlot(str, str, dict)
    def updateView(self, node, group, sensors):
        if node not in self.tabs:
            self.addNodeTab(node)
        tabView = self.tabs[node].view 
        if group not in tabView.groups:
            tabView.addPane(group)
        groupView = tabView.groups[group].view
        groupView.update(sensors)
        