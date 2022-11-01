from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from types import SimpleNamespace as SN

class GroupView(QWidget):

    def __init__(self):
        super(GroupView, self).__init__()
        self.valueGrid = QGridLayout()
        self.setLayout(self.valueGrid)
        self.grid = {}

    def toStr(self, payload):
        return str(getattr(payload, "value", "???")) + " " + str(getattr(payload, "unit", "_"))

    def update(self, sensors):
        for key, value in sensors.items():
            if key not in self.grid:
                row = SN(index=len(self.grid),
                         label=QLabel(key),
                         value=QLabel("<?>"))
                self.valueGrid.addWidget(row.label, row.index, 0)
                self.valueGrid.addWidget(row.value, row.index, 1)
                self.grid[key] = row
            self.grid[key].value.setText(self.toStr(value))
