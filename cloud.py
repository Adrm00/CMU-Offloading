import sys
import time

def process(n):
    time.sleep(1 * n)

start_time = time.time()
process(int(sys.argv[1]))
end_time = time.time()

print("Completed cloud processing in %f seconds" %(end_time - start_time))
