import paramiko

def get_sftp_client(url, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(url, user, password)
    sftp = client.open_sftp()
    return sftp