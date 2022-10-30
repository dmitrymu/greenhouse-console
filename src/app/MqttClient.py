import paho.mqtt.client as mqtt
import json
from types import SimpleNamespace as SN

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("nodes/#")

def decodeJsonPayload(payload):
    try:
        return json.loads(payload.decode("utf-8"))
    except json.JSONDecodeError as err:
        return {"value": err.msg}

# The callback for when a PUBLISH message is received from the server.
def on_message(client, model, msg):
    tokens = msg.topic.split('/')
    # print(tokens)
    payload = decodeJsonPayload(msg.payload)
    nodeName = tokens[1]
    node = model.updateNode(nodeName)
    group = node.updateGroup(tokens[2])
    group.updateSensor(name = tokens[3], value = SN(**payload))


def CreateMqttClient(host, port = 1883):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    #client.loop_forever()
    return client