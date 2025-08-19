import redis, time
from rq import Queue
from rq.job import Job
from app.jobs import background_job

# Connect to Redis
redis_conn = redis.from_url("redis://localhost:6379/0")
queue = Queue(connection=redis_conn)

# Enqueue job
job = queue.enqueue(background_job, 3, 4)
print("Job queued:", job.get_id())

# Poll until job finishes
while True:
    job.refresh()
    print("Job status:", job.get_status())
    if job.is_finished:
        print("✅ Job result:", job.result)
        break
    elif job.is_failed:
        print("❌ Job failed")
        break
    time.sleep(1)
