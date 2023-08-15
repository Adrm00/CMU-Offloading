import time
import paramiko

start_time = time.time()
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

private_key = paramiko.RSAKey.from_private_key_file('CMU-2023-1-keypair.pem')

# Depois tem que automatizar pegar esse IP, usando boto3 (se o ID da instancia nao mudar)
ssh.connect(hostname='3.92.199.132', username='ubuntu', pkey=private_key)

# Executar o comando na instância e obter a saída.
stdin, stdout, stderr = ssh.exec_command('cd CMU-Offloading; python3 cloud.py 2')

# Ler a saída do comando.
output = stdout.read().decode('utf-8')
print(f'Resultado do comando: {output}')
end_time = time.time()
print(end_time - start_time)

#battery = 1.00

# EU PASSARIA UM PARAMETRO DE TAMANHO QUE DEPENDENDO SERIA MELHOR RODAR LOCAL OU REMOTAMENTE (pode ate ser o valor do sleep).
# Utilizar sleep() pra simular processamento: menor local e maior na cloud (parametro + ou * algo)
# medir o tempo executa as funcoes (ruim?)
# deixar ja conectado com a instancia talvez(?) (acho que nao na vdd, conectar na shell se precisar, rodar e depois fechar)
# poderia utilizar um parametro ficticio de bateria para levar mais um fator em consideracao e alterar a execucao de alguma forma

# Depois calcular o tempo de rodar a funcao com um sleep menor na cloud vs rodar localmente com sleep maior
# Primeiro testar com o mesmo sleep pra ver a diferenca

def measure_local_execution_time():
    start_time = time.time()
    process()
    end_time = time.time()
    return(end_time - start_time)

def measure_cloud_execution_time():
    start_time = time.time()
    #offload_process()
    end_time = time.time()
    return(end_time - start_time)

def calculate_offloading_need():
    if measure_cloud_execution_time() < measure_local_execution_time():
        return True
    return False

def process():
    print("Operaçao custosa!")
    time.sleep(5)