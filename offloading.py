import time
import paramiko

#battery = 1.00

# EU PASSARIA UM PARAMETRO DE TAMANHO QUE DEPENDENDO SERIA MELHOR RODAR LOCAL OU REMOTAMENTE (pode ate ser o valor do sleep).
# Utilizar sleep() pra simular processamento: menor local e maior na cloud (parametro + ou * algo)
# medir o tempo executa as funcoes (ruim?)
# deixar ja conectado com a instancia talvez(?) (acho que nao na vdd, conectar na shell se precisar, rodar e depois fechar)
# poderia utilizar um parametro ficticio de bateria para levar mais um fator em consideracao e alterar a execucao de alguma forma

# Depois calcular o tempo de rodar a funcao com um sleep menor na cloud vs rodar localmente com sleep maior
# Primeiro testar com o mesmo sleep pra ver a diferenca

def measure_local_execution_time(n):
    start_time = time.time()
    local_process(1)
    end_time = time.time()
    total_time = end_time - start_time
    return(total_time * n)

def measure_cloud_execution_time(n):
    start_time = time.time()
    cloud_process_time = cloud_process(1)
    end_time = time.time()
    total_time = end_time - start_time
    return(total_time + (cloud_process_time * n))

def calculate_offloading_need(n):
    if measure_cloud_execution_time(n) < measure_local_execution_time(n):
        return True
    return False

def cloud_process(n):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    private_key = paramiko.RSAKey.from_private_key_file('CMU-2023-1-keypair.pem')

    # Depois tem que automatizar pegar esse IP, usando boto3 (se o ID da instancia nao mudar)
    ssh.connect(hostname='18.233.101.60', username='ubuntu', pkey=private_key)

    # Executar o comando na instância e obter a saída.
    stdin, stdout, stderr = ssh.exec_command('cd CMU-Offloading; python3 cloud.py %s' %n)

    # Ler a saída do comando.
    output = stdout.read().decode('utf-8')
    print(f'Resultado do comando: {output}')

    return float(output)

def local_process(n):
    time.sleep(3 * n)

def process(n):
    if calculate_offloading_need(n) == True:
        cloud_process(n)
    else:
        local_process(n)

print(measure_local_execution_time(100))
print(measure_cloud_execution_time(100))