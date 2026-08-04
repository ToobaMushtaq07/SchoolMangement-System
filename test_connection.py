from package.db import get_connection

print("Connecting to PostgreSQL...")

conn = get_connection()

if conn:
    print("✅ Connection Successful!")
    cursor = conn.cursor()
    cursor.execute("SELECT current_database();")
    print("Connected to:", cursor.fetchone()[0])
    cursor.close()
    conn.close()
else:
    print("❌ Connection Failed.")