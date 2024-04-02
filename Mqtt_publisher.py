import paho.mqtt.client as mqtt
import json
import time

# MQTT settings
MQTT_Broker = "f2a8991d3b434c3db6649cbb939a45c6.s1.eu.hivemq.cloud"
MQTT_Port = 8883
Keep_Alive_Interval = 60
MQTT_Topic = "my_data_topic"

# Create MQTT client instance
mqttc = mqtt.Client()

# Connect to MQTT broker
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

# Function to read JSON data from file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Publish data
def publish_data(data):
    for item in data:
        mqttc.publish(MQTT_Topic, json.dumps(item))
        print(f"Published: {item}")

if __name__ == "__main__":
    file_path = "data.json"
    data = read_json_file(file_path)

    publish_data(data)
