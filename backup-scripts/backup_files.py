from array_files import files
from decouple import config
import paramiko
from scp import SCPClient
from decouple import config

LOCAL_DIR = config("LOCAL_DIR")
REMOTE_DIR = config("REMOTE_DIR")

REMOTE_SERVER = config("REMOTE_SERVER")
REMOTE_PORT = config("REMOTE_PORT")
REMOTE_USER = config("REMOTE_USER")
REMOTE_PASSWORD = config("REMOTE_PASSWORD")

def createSSHClient(REMOTE_SERVER, REMOTE_PORT, REMOTE_USER, REMOTE_PASSWORD):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(REMOTE_SERVER, REMOTE_PORT, REMOTE_USER, REMOTE_PASSWORD)
    return client

ssh = createSSHClient(REMOTE_SERVER, REMOTE_PORT, REMOTE_USER, REMOTE_PASSWORD)
scp = SCPClient(ssh.get_transport())

for i in files:
    LOCAL_FILE = i
    LOCAL_FULL_PATH = LOCAL_DIR + '/' + LOCAL_FILE
    LOCAL_FULL_PATH = LOCAL_FULL_PATH.decode()

    print(LOCAL_FULL_PATH)
    scp.put(LOCAL_FULL_PATH, recursive=True, remote_path=REMOTE_DIR)

scp.close()


