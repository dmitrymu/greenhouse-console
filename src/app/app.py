from PyQt6.QtWidgets import QApplication, QWidget
from MainWindow import MainWindow
from NodeModel import NodeModel
from MqttClient import CreateMqttClient

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

model = NodeModel()
client = CreateMqttClient("localhost")
client.user_data_set(model)

# Create a Qt widget, which will be our window.
window = MainWindow()
model.setView(window)
window.showMaximized()  # IMPORTANT!!!!! Windows are hidden by default.

client.loop_start()

# Start the event loop.
app.exec()
