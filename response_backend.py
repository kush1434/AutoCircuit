import sqlite3
import datetime

# Set up the response_log database if it doesn't exist
def init_db():
    conn = sqlite3.connect("response_log.db")
    cursor = conn.cursor()
    
    # Create the response_log table to track user evaluations
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS response_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            inputs INTEGER,
            behavior TEXT,
            sync INTEGER,
            response TEXT,
            accurate INTEGER
        )
    """)
    
    conn.commit()
    conn.close()

# Log data after each user interaction
def log_response(inputs, behavior, sync, response, accurate):
    conn = sqlite3.connect("response_log.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO response_log (timestamp, inputs, behavior, sync, response, accurate)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.datetime.now().isoformat(),
        inputs,
        behavior,
        int(sync),
        response,
        int(accurate)
    ))
    
    conn.commit()
    conn.close()

# Calculates the accuracy of the model based on the db
def get_accuracy():
    conn = sqlite3.connect("response_log.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM response_log")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM response_log WHERE accurate = 1")
    correct = cursor.fetchone()[0]

    conn.close()
    
    if total == 0:
        return 100.0
    return (correct / total) * 100
