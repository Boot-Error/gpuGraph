import paramiko
import getpass


def setup_ssh(username, host, port):

    transport = paramiko.Transport((host, port))

    password = getpass.getpass("Password for " + username + "@" + host + ": ")
    transport.connect(username = username, password = password)

    sftp = paramiko.SFTPClient.from_transport(transport)

    return sftp

def get_gpu_load(sftp):

    with sftp.open('/sys/devices/gpu.0/load') as f:
        return f.read()

def kill_conn(sftp):

    sftp.close()
    transport.close()
