'''
Transit CLI (Version 0.1)
MIT License
'''

import ftp, sys, getpass, time, ftplib
from rich import print

showWelcome = True

if '-m' in sys.argv:
    mode = sys.argv[sys.argv.index('-s') + 1]
else:
    mode = 'ssh'

print(mode)

if mode == 'ssh' or mode == 'sftp':
    import sftp as ftp
elif mode == 'ftp':
    import ftp as ftp
else:
    raise ValueError

def ls():
    for item in ftp.ls():
        if len(str(item).split('.png')) > 1:
            print('[red] :sparkles: ' + item + '[/red]', end='  ')
        
        elif len(str(item).split('.py')) > 1:
            print('[red] :snake: ' + item + '[/red]', end='  ')
        
        elif len(str(item).split('.')) > 1:
            print('[red] :page_facing_up: ' + item + '[/red]', end='  ')
        
        else:
            print('[blue] :file_folder: ' + item + '[/blue]', end='  ')
    print()

def cd(dir):
    try:
        ftp.cd(dir=dir)
        ls()
    except ftplib.error_perm:
        print(':warning: Couldn\'t find path.')

def download(filename):
    print(':arrow_down_small: Downloading...', end='\r')
    ftp.download(filename=filename)
    print(':heavy_check_mark: Done!         ', end='\r')
    print()
#########################################################

if '-s' in sys.argv:
    server = sys.argv[sys.argv.index('-s') + 1]
else:
    server = input('Server: ')                # test.rebex.net

if '-u' in sys.argv:
    username = sys.argv[sys.argv.index('-u') + 1]
else:
    print(':wave: ', end='')
    username = input('Username: ')            # demo


print(':lock: ', end='')
password = getpass.getpass('Password: ')  # password

ftp.connect(server=server, username=username, password=password)

print(':heavy_check_mark: Connected to the server.')

if showWelcome:
    print(ftp.welcome())

time.sleep(0.5)
print()

while True:
    cmd = input('→ ')
    cmd = cmd.lower()

    if cmd.startswith('cd') or cmd.startswith('chdir'):
        cd(cmd.split(' ')[1])
    
    elif cmd.startswith('ls') or cmd.startswith('dir'):
        ls()

    elif cmd.startswith('exit') or cmd.startswith('bye'):
        print(':wave: Good bye!')
        try:
            ftp.bye()
        except:
            pass
        sys.exit()
    
    elif cmd.startswith('download') or cmd.startswith('get'):
        download(cmd.split(' ')[1])