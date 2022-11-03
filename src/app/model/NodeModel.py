from types import SimpleNamespace as SN
from threading import Timer
from PyQt5 import QtCore

class SensorGroup():

    def __init__(self, parent = None, name = "???"):
        self.parent = parent
        self.name = name
        self.sensors = {}
        self.timer = None
        
    def updateSensor(self, name, value):
        self.sensors[name] = value
        if self.timer != None:
            self.timer.cancel()
        # Wait for half second to accumulate more updates
        self.timer = Timer(.5, self.updateView)
        self.timer.start()
    
    def updateView(self):
        # Update view with all accumulated values
        self.parent.parent.updateSignal.emit(
            self.parent.name, self.name, self.sensors)
        self.timer = None

class NodeModel():

    def __init__(self, parent = None, name = "???"):
        self.parent = parent
        self.name = name
        self.groups = {}

    def updateGroup(self, name):
        if name in self.groups:
            return self.groups[name]
        else:
            group = SensorGroup(parent = self, name = name)
            self.groups[name] = group
            return group
