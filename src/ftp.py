from ftplib import FTP

# Connect to a remote FTP server
def connect(server, username='anonymous', password=''):
    global ftp
    ftp = FTP(server)
    ftp.login(username, password)
    
    welcome = ftp.getwelcome()
    files = ftp.nlst()

    return(files)

# Get welcome message from FTP server
def welcome():
    welcome = ftp.getwelcome()
    return(welcome)

# Get file listing from FTP server
def ls():
    files = ftp.nlst()

    return(files)

# Change remote dir 
def cd(dir):
    ftp.cwd(str(dir))
    
    return(ls())

# Quit connection
def bye():
    ftp.quit()

# Download file from remote FTP server.
def download(filename):
    with open(str(filename), 'wb') as fp:
        ftp.retrbinary('RETR ' + str(filename), fp.write)
