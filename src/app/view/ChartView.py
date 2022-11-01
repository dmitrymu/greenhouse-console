import pyqtgraph as pg
import datetime as dt
from PyQt5 import QtGui
from types import SimpleNamespace as SN

palette = ["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7"]

class ChartView(pg.PlotWidget):

    def __init__(self, *args, name = "???", **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.time = []
        self.series = {}
        axis = pg.DateAxisItem() 

        self.setAxisItems({'bottom': axis})
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getAxis("bottom").setStyle(tickFont = font)
        self.getAxis("left").setStyle(tickFont = font)

        self.window = dt.timedelta(hours=6)

    def setTimeWindow(self, window):
        self.window = dt.timedelta(window)

    def getPaletteColor(self, index):
        return palette[index % len(palette)]

    

    def addPoint(self, time, values):
        while len(self.time) > 0 and self.time[0] < (dt.datetime.fromtimestamp(time) - self.window).timestamp():
            self.time = self.time[1:]
            for _, item in self.series.items():
                item.data = item.data[1:]

        self.time.append(time)
        for key, value in values.items():
            if key in self.series:
                self.series[key].data.append(value)
                self.series[key].line.setData(self.time, self.series[key].data)
            else:
                v = [float('nan')] * (len(self.time) -1)
                v.append(value)
                self.series[key] = SN(data=v,
                                      line=self.plot(self.time,
                                                     v,
                                                     pen=pg.mkPen(
                                                         {'color': self.getPaletteColor(len(self.series)),
                                                          'width': 2})))

        for key, item in self.series.items():
            if key not in values:
                while len(item.data) < len(self.time):
                    item.data.append(float('nan'))
