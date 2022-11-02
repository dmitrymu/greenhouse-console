from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QApplication

class StatusView(QWidget):
    def __init__(self):
        super(StatusView, self).__init__()
        self.setLayout(QHBoxLayout())
        self.connection = QLabel("*")
        self.layout().addWidget(self.connection, stretch=0)
        self.node = QLabel()
        self.layout().addWidget(self.node, stretch=1)

    def setStatus(self, success: bool, msg: str):
        self.connection.setToolTip(msg)
        self.connection.setStyleSheet(
            self.connection.styleSheet()
            + f"QToolTip {{font-size: {12}pt}}")
        self.connection.setStyleSheet(
            self.connection.styleSheet()
            + ("QLabel { color: green;  background: green; }"
                if success
                else "QLabel { color: red; background: red; }"))
