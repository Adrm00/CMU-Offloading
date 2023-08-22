import sys
import time

processing_power = 1.25

transmission_rate = 10 #bytes/segundo 

def process(n):

    time.sleep(n/transmission_rate)

    time.sleep(1/processing_power * n)

n = int(sys.argv[1])

if n > 0:
    process(n)

print("Esse codigo foi executado na nuvem")
