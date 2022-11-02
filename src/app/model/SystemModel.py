from PyQt5 import QtCore
from .NodeModel import NodeModel

class SystemModel(QtCore.QObject):
    updateSignal = QtCore.pyqtSignal(str, str, dict)
    connectSignal = QtCore.pyqtSignal(bool, str)

    def __init__(self, *args, **kwargs):
        super(SystemModel, self).__init__(*args, **kwargs)
        self.nodes = {}
        self.view = None

    def setConnectStatus(self,
                         isConnected,
                         msg):
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

