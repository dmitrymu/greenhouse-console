from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from types import SimpleNamespace as SN

class SensorGroup(QtCore.QObject):
    def __init__(self, *args, name = "???", **kwargs):
        super(SensorGroup, self).__init__(*args, **kwargs)
        self.name = name
        self.sensors = {}
        self.view = None

    def setView(self, view):
        self.view = view

    def updateSensor(self, name, value):
        self.sensors[name] = value
        if (self.view is not None):
            table = self.view.view
            table.clearContents()
            table.setRowCount(len(self.sensors))
            table.setVerticalHeaderLabels(list(self.sensors.keys()))

class SingleNode(QtCore.QObject):
    def __init__(self, *args, name = "???", **kwargs):
        super(SingleNode, self).__init__(*args, **kwargs)
        self.name = name
        self.groups = {}
        self.view = None

    def setView(self, view):
        self.view = view

    def updateGroup(self, name):
        if name in self.groups:
            return self.groups[name]
        else:
            group = SensorGroup(name = name)
            self.groups[name] = group
            if (self.view is not None):
                group.setView(self.view.view.addPane(name))
            return group

class NodeModel(QtCore.QObject):
    def __init__(self, *args, nodes=None, **kwargs):
        super(NodeModel, self).__init__(*args, **kwargs)
        self.nodes = nodes or {}
        self.view = None

    def setView(self, view):
        self.view = view

    def updateNode(self, name):
        if name in self.nodes:
            return self.nodes[name]
        else:
            node = SingleNode(name = name)
            if (self.view is not None):
                node.setView(self.view.addTab(name))
            self.nodes[name] = node
            return node

