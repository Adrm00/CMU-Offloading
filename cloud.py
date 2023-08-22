import sys
import time

processing_power = 1.25

transmission_rate = 10 #bytes/segundo 

def process(n):

    time.sleep(n/transmission_rate)

    time.sleep(1/processing_power * n)
    
    print('Mensagem transmitida em %f segundos' %(n/transmission_rate))
    print('Processamento na nuvem realizado em %f segundos' %(1/processing_power * n))

process(int(sys.argv[1]))

