# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb

host = "localhost"
port = 3306
username = "root"
password = "MYSQL2024@@-Hiba"
database = "hbtn_0e_0_usa"

connection = MySQLdb.connect(host=host, port=port, user=username, passwd=password, database=database)
cursor = connection.cursor()

cursor.execute("SELECT * FROM 'states'")
row = cursor.fetchone()

print(row)
