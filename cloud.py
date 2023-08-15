import sys
import time

def process(n):
    for i in range(n):
        time.sleep(1)

process(sys.argv[0])

print("Completed cloud processing")
