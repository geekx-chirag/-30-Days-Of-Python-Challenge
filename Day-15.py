import time
from time import perf_counter as p

def log_time(func):
    def wrapper():
        t = p(); func(); print(f"Took {p() - t:.2f}s")
    return wrapper
@log_time
def lift_Stormbreaker():
    time.sleep(1)
    print("Thor's Axe lifted!")

lift_Stormbreaker()
