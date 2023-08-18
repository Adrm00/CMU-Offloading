import sys
import time

processing_power = 1.25

def process(n):
    time.sleep(1/processing_power * n)
    print('Processamento na nuvem realizado em %f segundos' %(1/processing_power * n))

process(int(sys.argv[1]))

