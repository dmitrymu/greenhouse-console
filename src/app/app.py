from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from NodeModel import SystemModel
from MqttClient import MqttClient
from argparse import ArgumentParser
import qdarkstyle

# Only needed for access to command line arguments
import sys

parser = ArgumentParser(prog="Greenhouse console",
                        description="Display greenhouse sensors"\
                                    " received from MQTT broker")

parser.add_argument("-H", "--host",
                    default="localhost", help="MQTT broker host")
parser.add_argument("-p", "--port", type = int,
                    default=1883, help="MQTT broker port")
parser.add_argument("--font-size", type = int,
                    default=12, help="Application font size, pt")
args = parser.parse_args()

app = QApplication(sys.argv)

# Set dark theme and default font size
stylesheet = qdarkstyle.load_stylesheet_pyqt5();
stylesheet += f"QWidget {{font-size: {args.font_size}pt}}"
app.setStyleSheet(stylesheet)

model = SystemModel()
client = MqttClient(host = args.host, port = args.port, model = model)

window = MainWindow()
window.setFixedSize(1024, 600)  # Imitate kiosk screen size
window.show()  


model.setView(window.getSystemView())

# Start MQTT event loop.
client.run()

# Start QT event loop.
app.exec()
