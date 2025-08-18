from dotenv import load_dotenv; load_dotenv()

import redis, os
REDIS_URL = os.environ.get("REDIS_URL")

try:
    r = redis.Redis.from_url(REDIS_URL)
    r.set("health", "ok")
    print("✅ Redis set:", r.get("health"))
except Exception as e:
    print("❌ Redis connection failed:", e)
