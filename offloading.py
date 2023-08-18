import time
import paramiko

processing_power = 1.00


# Separar bem cada tempo de execucao (latencia, transmissao, processamento)

# Generalizar pra simular um middleware na verdade, e nao uma aplicacao especifica
# Ou seja, passar parametros como: 
## Processing power
## Tamanho da mensagem (simular quantidade de bits enviados de alguma forma)
## Quantidade de chamadas
## Latencia
## Taxa de transmissao

def measure_local_execution_time(n):
    local_processing_time = 1

    print("PROCESSAMENTO LOCAL")
    print("Tempo de processamento para n = %d: %f" %(n, (local_processing_time * n)))
    print("Tempo total: %f\n" %(local_processing_time * n))

    return(local_processing_time * n)

def measure_cloud_execution_time(n):
    cloud_processing_time = 0.8
    
    start_time = time.time()
    cloud_process(0)
    end_time = time.time()

    connection_time = end_time - start_time

    print("PROCESSAMENTO REMOTO")
    print("Tempo de conexao: %f" %connection_time)
    print("Tempo de processamento para n = %d: %f" %(n, (cloud_processing_time * n)))
    print("Tempo total: %f\n" %(connection_time + (cloud_processing_time * n)))

    return(connection_time + (cloud_processing_time * n))

def calculate_offloading_need(n):
    if measure_cloud_execution_time(n) < measure_local_execution_time(n):
        return True
    return False

def cloud_process(n):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    private_key = paramiko.RSAKey.from_private_key_file('CMU-2023-1-keypair.pem')

    # Depois tem que automatizar pegar esse IP, usando boto3 (se o ID da instancia nao mudar)
    ssh.connect(hostname='3.83.246.122', username='ubuntu', pkey=private_key)

    # Executar o comando na instância e obter a saída.
    stdin, stdout, stderr = ssh.exec_command('cd CMU-Offloading; python3 cloud.py %s' %n)

    # Ler a saída do comando.
    output = stdout.read().decode('utf-8')
    print(f'Resultado do comando: {output}')

    return float(output)

def local_process(n):
    time.sleep(1/processing_power * n)

def process(n):
    if calculate_offloading_need(n) == True:
        cloud_process(n)
        print("O processamento foi feito na nuvem.")
    else:
        local_process(n)
        print("O processamento foi feito localmente.")

print(measure_local_execution_time(3))
print(measure_cloud_execution_time(3))

process(3)