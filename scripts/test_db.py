from dotenv import load_dotenv; load_dotenv(dotenv_path=".env")

import psycopg2, os
DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Connected to Postgres!")
    conn.close()
except Exception as e:
    print("❌ Postgres connection failed:", e)
