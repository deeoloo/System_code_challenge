#!/usr/bin/env python3
"""
Initialize the SQLite database by creating all tables from schema.sql
"""

from lib.db.connection import get_connection

def initialize_database():
    """Create database tables using schema.sql"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Read and execute the schema file
        with open('lib/db/schema.sql', 'r') as schema_file:
            sql_commands = schema_file.read()
            cursor.executescript(sql_commands)
        
        print("✅ Database initialized successfully!")
        print("   Created tables: authors, magazines, articles")
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()