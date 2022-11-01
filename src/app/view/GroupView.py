from PyQt5.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QLabel
from .ChartView import ChartView
from types import SimpleNamespace as SN
import datetime as dt

class GroupView(QWidget):

    def __init__(self, *args, name = "???", **kwargs):
        super(GroupView, self).__init__(*args, **kwargs)
        self.setLayout(QHBoxLayout())
        self.valueGrid = QGridLayout()
        self.valueGrid.setColumnStretch(0, 1)
        self.valueGrid.setColumnStretch(1, 0)
        self.valueGrid.setColumnStretch(2, 0)
        self.layout().addLayout(self.valueGrid, stretch=1)
        self.chart = ChartView(name = name)
        self.layout().addWidget(self.chart, stretch=1)
        self.grid = {}

    def toStr(self, payload):
        return str(getattr(payload, "value", "???")) + " " + str(getattr(payload, "unit", "_"))

    def toFloat(self, payload):
        return float(getattr(payload, "value", float('nan')))

    def update(self, sensors):
        dataPoint = {}
        for key, value in sensors.items():
            if key not in self.grid:
                row = SN(index=len(self.grid),
                         label=QLabel(key),
                         value=QLabel("<?>"),
                         legend =QLabel("*"))
                color = self.chart.getPaletteColor(row.index)
                row.legend.setStyleSheet(
                    f"QLabel {{ color: {color}; background: {color}; }}"
                )
                self.valueGrid.addWidget(row.label, row.index, 0)
                self.valueGrid.addWidget(row.value, row.index, 1)
                self.valueGrid.addWidget(row.legend, row.index, 2)
                self.grid[key] = row
            self.grid[key].value.setText(self.toStr(value))
            dataPoint[key] = self.toFloat(value)
        time = dt.datetime.now()
        self.chart.addPoint(time.timestamp(), dataPoint)
