from PyQt5 import QtCore
from types import SimpleNamespace as SN

class SensorGroup(QtCore.QObject):
    def __init__(self, *args, parent = None, name = "???", **kwargs):
        super(SensorGroup, self).__init__(*args, **kwargs)
        self.parent = parent
        self.name = name
        self.sensors = {}

    def updateSensor(self, name, value):
        self.sensors[name] = value
        self.parent.parent.updateSignal.emit(
            self.parent.name, self.name, self.sensors)

class NodeModel(QtCore.QObject):
    def __init__(self, *args, parent = None, name = "???", **kwargs):
        super(NodeModel, self).__init__(*args, **kwargs)
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

class SystemModel(QtCore.QObject):
    updateSignal = QtCore.pyqtSignal(str, str, dict)
    connectSignal = QtCore.pyqtSignal(bool, str)

    def __init__(self, *args, nodes=None, **kwargs):
        super(SystemModel, self).__init__(*args, **kwargs)
        self.nodes = nodes or {}
        self.view = None

    def setConnectStatus(self, isConnected, msg):
        self.connectSignal.emit(isConnected, msg)

    def setView(self, view):
        self.view = view
        self.updateSignal.connect(self.view.updateView)
        self.connectSignal.connect(self.view.updateConnectionStatus)

    def updateNode(self, name):
        if name in self.nodes:
            return self.nodes[name]
        else:
            node = NodeModel(parent = self, name = name)
            self.nodes[name] = node
            return node

