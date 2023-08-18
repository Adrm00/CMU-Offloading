import sys
import time

processing_power = 1.25

def process(n):
    time.sleep(1/processing_power * n)

start_time = time.time()
process(int(sys.argv[1]))
end_time = time.time()

print((end_time - start_time))
