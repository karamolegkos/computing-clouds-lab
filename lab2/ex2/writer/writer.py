import os
import time
import mysql.connector

time.sleep(8)  # περιμένουμε να σηκωθεί η MySQL

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255)
)
""")

cursor.execute("INSERT INTO messages (text) VALUES (%s)", ("Hello from writer!",))
db.commit()

print("✔ Inserted row successfully!")