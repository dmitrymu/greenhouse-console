from PyQt5.QtWidgets import QApplication, QWidget
from MainWindow import MainWindow
from NodeModel import SystemModel
from MqttClient import MqttClient
from argparse import ArgumentParser

# Only needed for access to command line arguments
import sys

parser = ArgumentParser(prog="Greenhouse console",
                        description="Display greeenhouse sensors received from MQTT broker")

parser.add_argument("-H", "--host",
                    default="localhost", help="MQTT broker host")
parser.add_argument("-p", "--port", type = int,
                    default=1883, help="MQTT broker port")
parser.add_argument("--font-size", type = int,
                    default=12, help="Application font size, pt")
args = parser.parse_args()
# if (args.help):
#     parser.print_help()
#     sys.exit(1)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

app.setStyleSheet(f"QWidget {{font-size: {args.font_size}pt}}")

model = SystemModel()
client = MqttClient(host = args.host, port = args.port, model = model)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.setFixedSize(1024, 600)  # !!!  for testing only
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
# window.showMaximized()

model.setView(window.getSystemView())

client.run()

# Start the event loop.
app.exec()
