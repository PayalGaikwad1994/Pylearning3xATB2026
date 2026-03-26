import time

def tame_taken_decorator(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("Time taken is",str(end_time-start_time))
    return wrapper

@tame_taken_decorator
def logs_func():
    time.sleep(5)
    print("Print the logs of time taken")


logs_func()