
import paho.mqtt.client as mqtt
import json
import logging
import mysql.connector as mariadb

# Configure logging
logging.basicConfig(level=logging.ERROR)


# # MySQL Connection
# mariadb_connection = mariadb.connect(
#     user='root',
#     password='',
#     host='localhost',
#     database='irrigation_monitoring_system'
# )
# cursor = mariadb_connection.cursor()



# # MQTT settings
# MQTT_Broker = "103.109.52.15"
# MQTT_Port = 1883
# Keep_Alive_Interval = 60
# MQTT_Topic = "beta/#"


# Callback functions for MQTT
def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_Topic,0)
    logging.info("Connected to MQTT broker")

def on_message(client, userdata, msg):
    try:
        # Decode JSON payload from MQTT message
        data = json.loads(msg.payload.decode("utf-8"))

        # Extract relevant fields from the JSON data
        machine_id =data.get("machine_id")
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

        data = {
                "v": tr_v ,"c": tr_c,"p": tr_p,"tt": tr_tt,"at": tr_at,"l": tr_l
            }
        data1 = machine_id
        print("Machine id:",data1)
        print(json.dumps(data, indent=4))  # Print the data in JSON format

        # Insert data into MySQL table
        sql = "INSERT INTO tr_machine (tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Reading_Time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, reading_time)
        cursor.execute(sql, val)
        mariadb_connection.commit()
        logging.info(f"{cursor.rowcount} record inserted into MySQL")
    except ValueError:
        logging.error("Error decoding JSON")
    except mariadb.Error as e:
        logging.error(f"MySQL Error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def on_subscribe(client, userdata, mid, granted_qos):
    pass

# MQTT client setup
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

# Connect to MQTT broker
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

# Start MQTT loop
mqttc.loop_forever()















