import time

def background_job(x, y):
    print("Job started...")
    time.sleep(5)
    return x + y
