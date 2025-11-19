import mysql.connector
import time
import os

# Wait for MySQL to be ready (simple but fine for a demo)
time.sleep(30)

DATA_DIR = "/app/data"
os.makedirs(DATA_DIR, exist_ok=True)

db = mysql.connector.connect(
    host="my-mysql",
    user="root",
    password="root",
    database="testdb",
    autocommit=True
)

cursor = db.cursor(dictionary=True)

last_id = 0  # track last processed id

while True:
    cursor.execute("SELECT * FROM logs WHERE id > %s ORDER BY id ASC", (last_id,))
    rows = cursor.fetchall()

    for row in rows:
        file_path = os.path.join(DATA_DIR, f"log_{row['id']}.txt")
        with open(file_path, "w") as f:
            f.write(row['message'])
        print("Created file:", file_path)
        last_id = row['id']

    time.sleep(5)