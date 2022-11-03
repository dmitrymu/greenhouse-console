from PyQt5.QtWidgets import QMainWindow
from view.SysemView import SystemView

# Main application window displaying system view.
class MainWindow(QMainWindow):

    # Constructor.
    def __init__(self):
        super(MainWindow, self).__init__()
        # Invisible in kiosk mode anyway.
        self.setWindowTitle("greenhouse-console")
        self.widget = SystemView()
        self.setCentralWidget(self.widget)

    # Return system view widget.
    def getSystemView(self):
        return self.widget
