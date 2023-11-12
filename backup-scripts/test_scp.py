import paramiko
from scp import SCPClient
from decouple import config

LOCAL_DIR = '.'
LOCAL_FILE = 'count_files.py'
LOCAL_FULL_PATH = LOCAL_DIR + '/' + LOCAL_FILE
REMOTE_DIR = config("GZE_TO_DIR")

REMOTE_SERVER = config("REMOTE_SERVER")
REMOTE_PORT = config("REMOTE_PORT")
REMOTE_USER = config("REMOTE_USER")
REMOTE_PASSWORD = config("REMOTE_PASSWORD")

def createSSHClient(REMOTE_SERVER, REMOTE_PORT, REMOTE_USER, REMOTE_PASSWORD):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())

scp.put(LOCAL_FULL_PATH, recursive=True, remote_path=REMOTE_DIR)

scp.close()
