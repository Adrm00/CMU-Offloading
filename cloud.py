import sys
import time

processing_power = 1.25

transmission_rate = 10 #bytes/segundo 

def process(n):

    time.sleep(n/transmission_rate)

    time.sleep(1/processing_power * n)

n = int(sys.argv[1])

start_time = time.time()
if n > 0:
    process(n)
end_time = time.time()
print("Offloading realizado na nuvem em %f segundos" %(end_time - start_time))
