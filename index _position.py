import psycopg2

def get_mqtt_devices_column_positions():
    # Replace these variables with your actual database connection info
    connection_string = "postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices"
    
    try:
        connection = psycopg2.connect(connection_string)
        cursor = connection.cursor()
        
        # Assuming your table name is 'mqtt_devices' and it's in the 'public' schema
        query = """
        SELECT column_name, data_type 
        FROM information_schema.columns
        WHERE table_name = %s ;
        """


        cursor.execute(query, ('mqtt_devices',))
        
        print("Column Positions in 'mqtt_devices' Table:")
        for column in cursor.fetchall():
            print(f"Column: {column[0]}, Position: {column[1]}")
    
    except psycopg2.Error as e:
        print(f"Error fetching column positions: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

get_mqtt_devices_column_positions()
