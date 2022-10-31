import paho.mqtt.client as mqtt
import json
from types import SimpleNamespace as SN

# Encapsulate paho.mqtt client
class MqttClient(mqtt.Client):

    # Construct new client
    def __init__(self, *args, host="127.0.0.1", port=1883, timeout=60, model=None, **kwargs):
        super(MqttClient, self).__init__(*args, **kwargs)
        # self.model = model
        self.client = mqtt.Client()
        self.client.user_data_set(model)
        self.client.on_connect = self.onConnect
        self.client.on_message = self.onMessage
        self.client.connect(host, port, timeout)

    # Run MQTT event loop in a separate thread
    def run(self):
        self.client.loop_start()

    # decorator for callbacks
    def callbackMethod(function):
        def wrapper(self, *args, **kwargs):
            return function(self, *args, **kwargs)
        return wrapper

    @callbackMethod
    def onConnect(self, client, model, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("nodes/#")


    @callbackMethod
    # The callback for when a PUBLISH message is received from the server.
    def onMessage(self, client, model, msg):
        def decodeJsonPayload(payload):
            try:
                return json.loads(payload.decode("utf-8"))
            except json.JSONDecodeError as err:
                return {"value": err.msg}
        tokens = msg.topic.split('/')
        payload = decodeJsonPayload(msg.payload)
        nodeName = tokens[1]
        node = model.updateNode(nodeName)
        group = node.updateGroup(tokens[2])
        group.updateSensor(name = tokens[3], value = SN(**payload))
