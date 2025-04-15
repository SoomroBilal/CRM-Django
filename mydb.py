import mysql.connector
import pymysql

database = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Pass@123'
)

print("Connecting With")
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE elderco")

print("All Done")