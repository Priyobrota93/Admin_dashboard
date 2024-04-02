import psycopg2
import json
import random
from datetime import datetime

# def create_database():
#     try:
#         psycopg2_connection = psycopg2.connect(user='root', password='', host="localhost")
#         cursor = psycopg2_connection.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS irrigation_monitoring_system")
#         # print("Database created successfully.")
#     except psycopg2.Error as err:
#         print(f"Error creating database: {err}")
#     finally:
#         cursor.close()
#         psycopg2_connection.close()


def create_tables():
    try:
        psycopg2_connection = psycopg2.connect("postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices")
        cursor = psycopg2_connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_post (machine_id SERIAL PRIMARY KEY, Name VARCHAR(255), test_v FLOAT, test_p FLOAT, test_at FLOAT, updated_at TIMESTAMP)")
        psycopg2_connection.commit()
        # print("Table created successfully.")
    except psycopg2.Error as err:
        print(f"Error creating table: {err}")
    finally:
        if cursor:
            cursor.close()
        if psycopg2_connection:
            psycopg2_connection.close()


# def insert_random_data():
#     try:
#         psycopg2_connection = psycopg2.connect(user='root', password='', host="localhost", database='irrigation_monitoring_system')
#         cursor = psycopg2_connection.cursor()

#         for _ in range(1):  
#             machine_id = random.randint(1, 1000)  # Generate a random machine_id
#             v = random.uniform(0, 200)
#             p = random.uniform(0, 200)
#             at = random.uniform(0, 200)
#             reading_time = datetime.now()

            


#             data = {
#                 "v": v,"c": c,"p": p,"tt": tt,"at": at,"l": l
#             }
#             data1 = machine_id
#             print("Machine id:",data1)
#             print(json.dumps(data, indent=4))  # Print the data in JSON format

#             sql = "INSERT INTO tr_machine (machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Reading_Time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#             val = (machine_id, v, c, p, tt, at, tr_l_value, reading_time)  # Use tr_l_value instead of l
#             cursor.execute(sql, val)
#             psycopg2_connection.commit()
#             print(cursor.rowcount, "record inserted.")

#     except psycopg2.Error as err:
#         print(f"Error connecting to MySQL database: {err}")
#     finally:
#         cursor.close()
#         psycopg2_connection.close()
#         cursor.close()
#         psycopg2_connection.close()
        
# def fetch_data(machine_id):

#     try:
#         psycopg2_connection = psycopg2.connect(user='root', password='', host="localhost", database='irrigation_monitoring_system')
#         cursor = psycopg2_connection.cursor()
#         sql = "SELECT tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Reading_Time FROM tr_machine WHERE machine_id = %s"
#         cursor.execute(sql, (machine_id,))
#         # cursor.execute("SELECT machine_id, tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l FROM tr_machine")
#         row = cursor.fetchone()  # Fetch only one row


# #         if row is not None:
# #             data = {
# #                 "v": row[0],
# #                 "c": row[1],
# #                 "p": row[2],
# #                 "tt": row[3],
# #                 "at": row[4],
# #                 "l": row[5],
# #                 "Reading_Time": row[6].isoformat()  # Convert datetime object to ISO format string
# #             }
# #             print("Data for machine_id:", machine_id)
# #             print(json.dumps(data, indent=4))
# #         else:
# #             print(f"No data found for machine_id: {machine_id}")



#         if row is not None:
#             # machine_id = row[0]
#             data = {
#                 "v": row[0],
#                 "c": row[1],
#                 "p": row[2],
#                 "tt": row[3],
#                 "at": row[4],
#                 "l": row[5],
#                 "Reading_Time": row[6].isoformat()  # Convert datetime object to ISO format string
#                 }
#             # data = {
#             #     "v": row[1],
#             #     "c": row[2],
#             #     "p": row[3],
#             #     "tt": row[4],
#             #     "at": row[5],
#             #     "l": row[6]
#             # }
#             print("machine_id:", machine_id)
#             print(json.dumps(data, indent=4))
#         else:
#             print(f"No data found for machine_id: {machine_id}")
#         # rows = cursor.fetchall()

#         # for row in rows:
#         #     machine_id = row[0]
#         #     data = {"v": row[1],"c": row[2],"p": row[3],"tt": row[4],"at": row[5],"l": row[6]}
#         #     print("machine_id:", machine_id)
#         #     print(json.dumps(data, indent=4))


#     except psycopg2.Error as err:
#         print(f"Error fetching data from MySQL database: {err}")
#     finally:
#         cursor.close()
#         psycopg2_connection.close()

# def fetch_specific_data(machine_id):
#     try:
#         psycopg2_connection = psycopg2.connect(user='root', password='', host="localhost", database='irrigation_monitoring_system')
#         cursor = psycopg2_connection.cursor()

#         # Execute the SQL query with a WHERE clause to fetch data for a specific machine_id
#         sql = "SELECT tr_v, tr_c, tr_p, tr_tt, tr_at, tr_l, Reading_Time FROM tr_machine WHERE machine_id = %s"
#         cursor.execute(sql, (machine_id,))
        
#         row = cursor.fetchone()  # Fetch the first row

#         if row is not None:
#             data = {
#                 "v": row[0],
#                 "c": row[1],
#                 "p": row[2],
#                 "tt": row[3],
#                 "at": row[4],
#                 "l": row[5],
#                 "Reading_Time": row[6].isoformat()  # Convert datetime object to ISO format string
#             }
#             print("Data for machine_id:", machine_id)
#             print(json.dumps(data, indent=4))
#         else:
#             print(f"No data found for machine_id: {machine_id}")

#     except psycopg2.Error as err:
#         print(f"Error fetching data from MySQL database: {err}")
#     finally:
#         cursor.close()
#         psycopg2_connection.close()

# Specify the machine_id for which you want to fetch the data
# machine_id_to_fetch = 989
# fetch_specific_data(machine_id_to_fetch)


# fetch_data(machine_id_to_fetch)
# create_database()
create_tables()
# insert_random_data()

