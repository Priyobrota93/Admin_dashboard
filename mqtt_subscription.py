import paho.mqtt.client as mqtt
import json
import logging
import mysql.connector as mariadb

# Configure logging
logging.basicConfig(level=logging.ERROR)

# MySQL Connection
mariadb_connection = mariadb.connect(
    user='root',
    password='',
    host='localhost',
    database='irrigation_monitoring_system'
)
cursor = mariadb_connection.cursor()

# MQTT settings
MQTT_Broker = "103.109.52.15"
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "beta/#"


machine_id =57

print("connection")
# Callback functions for MQTT
def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_Topic, 0)
    logging.info("Connected to MQTT broker")
print("on-connect")
def on_message(client, userdata, msg):
    try:


        print("Topic",msg.topic + "\nMessage:" + str(msg.payload))
        print("Topic", msg.topic + "\nMessage:" + (msg.payload.decode("utf-8")))
        topic=msg.topic.split("/")
        print(topic)
        topic, recv, machine_id = msg.topic.split('/')
        # print("Device Name: ")
        print(machine_id)


        # Decode JSON payload from MQTT message
        data = json.loads(msg.payload.decode("utf-8"))

        # Extract relevant fields from the JSON data
        machine_id = data.get("machine_id")
        tr_v = data.get("tr_v")
        tr_c = data.get("tr_c")
        tr_p = data.get("tr_p")
        tr_tt = data.get("tr_tt")
        tr_at = data.get("tr_at")
        tr_l = data.get("tr_l")
        reading_time = data.get("reading_time")  # Assuming this field is present in your MQTT payload

       # Set tr_l_value based on condition
        if (tr_l > 40):
            tr_l_value = 1
        else:
            tr_l_value = 0 


        # Insert data into MySQL table
        sql = "INSERT INTO tr_machine (machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Reading_Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l_value, reading_time)
        cursor.execute(sql, val)
        mariadb_connection.commit()
        logging.info(f"{cursor.rowcount} record inserted into MySQL")
    except ValueError:
        logging.error("Error decoding JSON")
    except mariadb.Error as e:
        logging.error(f"MySQL Error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
print("on- message")
def on_subscribe(client, userdata, mid, granted_qos):
    pass
print("on-supbscribe")
# MQTT client setup
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
print("mqtt_on_connect")
mqttc.on_subscribe = on_subscribe
print("mqtt_on-supbscribe")
mqttc.on_message = on_message
print("mqtt_on_message")

# Connect to MQTT broker
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

# Start MQTT loop
mqttc.loop_forever()
print("end")