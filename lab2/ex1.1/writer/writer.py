import os
import time
import mysql.connector

# Wait for MySQL to be ready (simple but fine for a demo)
time.sleep(20)
print("Starting writer service...", flush=True)

# Read connection info from environment, with simple defaults
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "root")
DB_NAME = os.getenv("DB_NAME", "testdb")

print(f"Connecting to MySQL at {DB_HOST}, database {DB_NAME}...", flush=True)

db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME,
)

print("Connected to MySQL.", flush=True)

cursor = db.cursor()

# Simple table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255)
)
""")
db.commit()
print("Table 'messages' is ready.", flush=True)

counter = 1

while True:
    text = f"Hello from writer! #{counter}"
    cursor.execute("INSERT INTO messages (text) VALUES (%s)", (text,))
    db.commit()

    print(f"Inserted row {counter}: {text}", flush=True)
    counter += 1

    time.sleep(5)