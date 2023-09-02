import os
from cryptography.fernet import Fernet
import base64

def create_master_key():
    file_name = 'secret.txt'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    master_key = base64.urlsafe_b64encode(os.urandom(32))
    with open(file_name, "wb") as keyfile:
        keyfile.write(master_key)
    return master_key
    
def get_master_key():
    file_name = 'secret.txt'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isfile(file_name):
        with open(file_name, "rb") as keyfile:
            master_key = keyfile.read()
            return master_key
    else:
        master_key = create_master_key()
    return master_key

def encrypt(word):
    master_key = get_master_key()
    fernet = Fernet(master_key)
    encrypted_word = fernet.encrypt(word.encode())
    return encrypted_word

def decrypt(word):
    master_key = get_master_key()
    fernet = Fernet(master_key)
    decrypted_word = fernet.decrypt(word).decode()
    return decrypted_word


def get_information(word):
    # if the file passwords.txt doesn't exist, create it
    if not os.path.isfile('passwords.txt'):
        with open('passwords.txt', 'wb') as f:
            pass
    with open('passwords.txt', 'rb') as f:
        for line in f:
            decrypted_data = decrypt(line)
            decrypted_data = decrypted_data.split('_')
            if decrypted_data[2] == word or decrypted_data[0] == word:
                return decrypted_data[0] + ' ' + decrypted_data[1]
    return 'Keyword not found'


def store_information(account, password, keyword):
    if not os.path.isfile('passwords.txt'):
        with open('passwords.txt', 'wb') as f:
            pass
    with open('passwords.txt', 'rb') as f:
        for line in f:
            decrypted_data = decrypt(line)
            decrypted_data = decrypted_data.split('_')
            if decrypted_data[2] == keyword or decrypted_data[0] == account:
                return 'Keyword or account already exists' # esto deberia ser un error
    # if not, store information
    with open('passwords.txt', 'ab') as f:
        encrypted_data = encrypt(account + '_' + password + '_' + keyword)
        f.write(encrypted_data + b'\n')
    return 'Information stored'

        
def update_information(word, new_password):
    if not os.path.isfile('passwords.txt'):
        with open('passwords.txt', 'wb') as f:
            pass
    with open('passwords.txt', 'rb') as f:
        for line in f:
            decrypted_data = decrypt(line)
            decrypted_data = decrypted_data.split('_')
            if decrypted_data[2] == word or decrypted_data[0] == word:
                account = decrypted_data[0]
                keyword = decrypted_data[2]
                store_information(account, new_password, keyword)
                return 'Information updated'
    return 'Keyword or Account not found' # esto deberia ser un error

def delete_information(word):
    if not os.path.isfile('passwords.txt'):
        with open('passwords.txt', 'wb') as f:
            pass
    with open('passwords.txt', 'rb') as f:
        for line in f:
            decrypted_data = decrypt(line)
            decrypted_data = decrypted_data.split('_')
            if decrypted_data[2] == word or decrypted_data[0] == word:
                line = line.replace(line, b'')
                return 'Information deleted'
    return 'Keyword or Account not found' # esto deberia ser un error

store_information('facebook', '123456', 'face')
store_information('instagram', '123456', 'insta')
store_information('twitter', '123456', 'X')
#print(get_information('twitter'))