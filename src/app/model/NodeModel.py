from types import SimpleNamespace as SN
from PyQt5 import QtCore

class SensorGroup():

    def __init__(self, parent = None, name = "???"):
        self.parent = parent
        self.name = name
        self.sensors = {}

    def updateSensor(self, name, value):
        self.sensors[name] = value
        self.parent.parent.updateSignal.emit(
            self.parent.name, self.name, self.sensors)

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
