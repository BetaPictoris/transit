import paramiko

def connect(server, username='anonymous', password=''):
    global ftp
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=password)

    ftp = ssh.open_sftp()
    
    return(ls())

def welcome() -> None:
    return None

def ls() -> list:
    files = ftp.listdir()
    return(files)

def cd(dir:str) -> list:
    ftp.chdir(dir)
    return(ls())

def bye() -> None:
    ftp.close()
    return None

def download(filename:str) -> None:
    ftp.get(filename, filename)