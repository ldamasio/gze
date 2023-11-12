import paramiko
from scp import SCPClient

server = '158.220.104.74'
port = '22'
user = 'root'
password = 'dD4fLD622ijNe8KEir'

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())

scp.put('count_files.py', recursive=True, remote_path='/backup')

scp.close()
