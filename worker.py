import redis
from rq import SimpleWorker, Queue
# from rq.connections import Connection

# Connect to Redis
redis_conn = redis.from_url("redis://localhost:6379/0")
queue = Queue(connection=redis_conn)

if __name__ == "__main__":
    worker = SimpleWorker([queue], connection=redis_conn)
    worker.work()