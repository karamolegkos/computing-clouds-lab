import mysql.connector
import time

# Wait for MySQL to be ready (simple but fine for a demo)
time.sleep(20)

db = mysql.connector.connect(
    host="my-mysql",
    user="root",
    password="root",
    database="testdb"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))")

i = 0

while True:
    i += 1
    msg = f"Hello entry {i}"
    cursor.execute("INSERT INTO logs (message) VALUES (%s)", (msg,))
    db.commit()
    print("Inserted:", msg)
    time.sleep(3)