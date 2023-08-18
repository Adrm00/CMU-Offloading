import sys
import time

def process(n):
    time.sleep(1 * n)

start_time = time.time()
process(int(sys.argv[1]))
end_time = time.time()

print((end_time - start_time))
