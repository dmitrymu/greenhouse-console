from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QGridLayout, QLabel
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
        #return SimpleNamespace(root = pane, view = vlist)
        