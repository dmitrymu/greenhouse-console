from types import SimpleNamespace as SN
from typing import Dict
from PyQt5 import QtCore
from view.SysemView import SystemView

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
    nodes: Dict[str, NodeModel]
    view: SystemView

    def __init__(self, *args, **kwargs):
        super(SystemModel, self).__init__(*args, **kwargs)
        self.nodes = {}
        self.view = None

    def setConnectStatus(self,
                         isConnected: bool,
                         msg: str) -> None:
        self.connectSignal.emit(isConnected, msg)

    def setView(self, view: SystemView):
        self.view = view
        self.updateSignal.connect(self.view.updateView)
        self.connectSignal.connect(self.view.updateConnectionStatus)

    def updateNode(self, name: str) -> NodeModel:
        if name in self.nodes:
            return self.nodes[name]
        else:
            node = NodeModel(parent = self, name = name)
            self.nodes[name] = node
            return node

