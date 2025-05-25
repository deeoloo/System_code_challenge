# scripts/setup_db.py
import sqlite3
from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Read schema file
    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()
    
    # Execute schema
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database setup complete!")

if __name__ == '__main__':
    setup_database()