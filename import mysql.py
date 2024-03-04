import mysql.connector

try:
    # Replace 'your_database', 'your_username', and 'your_password' with your actual database details
    connection = mysql.connector.connect(
        host='141.209.241.81',       # Or your database server IP
        database='bis698_S24_w200',
        user='grp2w200',
        password='passinit'
    )
    
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except mysql.connector.Error as error:
    print("Failed to connect to MySQL: {}".format(error))


#finally:
#   if connection.is_connected():
#       cursor.close()
#       connection.close()
#       print("MySQL connection is closed")

