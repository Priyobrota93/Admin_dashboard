import psycopg2

def update_name_value(machine_id, new_name):
    try:
        # Connect to your database
        conn = psycopg2.connect("postgres://mqtt:QUfHMq15UqYIhsUXI6DkXW6na0A5155R@dpg-co3ef021hbls73f0enbg-a.singapore-postgres.render.com/mqttdevices")
        
        # Create a cursor object
        cur = conn.cursor()
        
        # SQL statement to update the Name column
        sql = "UPDATE mqtt_devices_two SET Name = %s WHERE machine_id = %s"
        cur.execute(sql, (new_name, machine_id))
        
        # Commit the changes to the database
        conn.commit()
        
        # Check if the update was successful
        if cur.rowcount > 0:
            print("Name updated successfully.")
        else:
            print("No record found to update.")
        
    except psycopg2.Error as e:
        print(f"Error updating Name value: {e}")
    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

# Example usage: Update the Name for machine_id 1 to 'New Device Name'
update_name_value("79.0","PetroBangla")

