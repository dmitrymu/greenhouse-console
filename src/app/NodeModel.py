from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from types import SimpleNamespace

class NodeModel(QtCore.QObject):
    def __init__(self, *args, nodes=None, **kwargs):
        super(NodeModel, self).__init__(*args, **kwargs)
        self.nodes = nodes or []

    def setView(self, view):
        self.view = view

    def addNode(self, name, data):
        self.nodes.append(SimpleNamespace(name = name, data = data))
        if (self.view is not None):
            self.nodes[-1].view = self.view.addTab(name, data)

