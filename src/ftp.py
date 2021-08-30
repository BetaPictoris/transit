import dearpygui.dearpygui as dpg
from ftplib import FTP

output_id = dpg.generate_uuid()
query_id = dpg.generate_uuid()

# Connect to a remote FTP server
def connect(server, username='anonymous', password=''):
    global ftp
    ftp = FTP(server)
    ftp.login(username, password)
    
    files = ftp.nlst()

    return(files)

server = input("Server: ")
username = input("Username: ")
password = input("Password: ")
connect(server, username, password)

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

def mainhandle():
    if str(dpg.get_value(query_id)) == "welcome":
        dpg.set_value(output_id, welcome())
    elif str(dpg.get_value(query_id)) == "ls":
        dpg.set_value(output_id, ls())
    elif "cd" in str(dpg.get_value(query_id)):
        uwu = dpg.get_value(query_id).replace("cd ", "")
        dpg.set_value(output_id, cd(uwu))
    elif str(dpg.get_value(query_id)) == "ls":
        bye()
    elif "download" in str(dpg.get_value(query_id)):
        cute = dpg.get_value(query_id).replace("cd ", "")
        dpg.set_value(output_id, download(cute))

with dpg.window(label="Input Window", width=500, height=350, no_resize=False, no_close=True):
    dpg.add_input_text(label="", width=500, on_enter=True, callback=mainhandle, id=query_id)
    dpg.add_button(label="Run", callback=mainhandle, width=500)

with dpg.window(label="Output Window", width=500, height=350, pos=[500,0], no_close=True):
    dpg.add_text("Output", id=output_id)

vp = dpg.create_viewport(title='FTP Manager', width=1000, height=350)
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(vp)
dpg.set_viewport_resizable(True)
dpg.start_dearpygui()