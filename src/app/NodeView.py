from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QGridLayout, QLabel, QTabWidget
from PyQt5 import QtCore
from PyQt5 import QtGui
from types import SimpleNamespace as SN

class GroupView(QWidget):

    def __init__(self):
        super(GroupView, self).__init__()
        self.setLayout(QGridLayout())
        self.grid = {}

    def toStr(self, payload):
        return str(getattr(payload, "value", "???")) + " " + str(getattr(payload, "unit", "_"))

    def update(self, sensors):
        for key, value in sensors.items():
            if key not in self.grid:
                row = SN(index=len(self.grid), label=QLabel(
                    key), value=QLabel("<?>"))
                self.layout().addWidget(row.label, row.index, 0)
                self.layout().addWidget(row.value, row.index, 1)
                self.grid[key] = row
            self.grid[key].value.setText(self.toStr(value))

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

class SystemView(QTabWidget):

    def __init__(self):
        super(SystemView, self).__init__()
        self.tabs = {}
    
    def addNodeTab(self, name):
        tabView = NodeView()
        n = self.addTab(tabView, name)
        self.tabs[name] = SN(index = n, view = tabView)
        return self.tabs[name]


    @QtCore.pyqtSlot(str, str, dict)
    def updateView(self, node, group, sensors):
        if node not in self.tabs:
            self.addNodeTab(node)
        tabView = self.tabs[node].view 
        if group not in tabView.groups:
            tabView.addPane(group)
        groupView = tabView.groups[group].view
        groupView.update(sensors)
        