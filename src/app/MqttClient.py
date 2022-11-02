import json
from typing import TypeVar
from types import SimpleNamespace as SN
import paho.mqtt.client as mqtt
from NodeModel import SystemModel

# Encapsulate paho.mqtt client
TClient = TypeVar("TClient", bound="MqttClient")
class MqttClient(mqtt.Client):

    # Construct new client
    def __init__(self,
                 *args,
                 host: str = "127.0.0.1",
                 port: int = 1883,
                 timeout: int = 60,
                 model: SystemModel = None,
                 **kwargs):
        super(MqttClient, self).__init__(*args, **kwargs)
        self.client = mqtt.Client()
        self.client.user_data_set(model)
        self.client.on_connect = self.onConnect
        self.client.on_message = self.onMessage
        self.client.on_disconnect = self.onDisconnect
        self.client.connect(host, port, timeout)

    # Run MQTT event loop in a separate thread
    def run(self):
        self.client.loop_start()

    # decorator for callbacks
    def callbackMethod(function):
        def wrapper(self, *args, **kwargs):
            return function(self, *args, **kwargs)
        return wrapper

    # to be executed on connect
    @callbackMethod
    def onConnect(self: TClient,
                  client: mqtt.Client,
                  model: SystemModel,
                  flags,
                  rc):
        model.setConnectStatus(True, mqtt.error_string(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("nodes/#")

    # to be executed on disconnect
    @callbackMethod
    def onDisconnect(self: TClient,
                     client: mqtt.Client,
                     model: SystemModel,
                     rc):
        model.setConnectStatus(False, mqtt.error_string(rc))

    # to be executed on receiving message
    @callbackMethod
    def onMessage(self: TClient,
                  client: mqtt.Client,
                  model: SystemModel,
                  msg):
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
