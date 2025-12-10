import mysql.connector
mydatabase = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'shobanashree',
)
print(mydatabase)
