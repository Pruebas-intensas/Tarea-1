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


def store_information(account, password, keyword):
    data = account+"_"+password+"_"+keyword
    encrypted_data = encrypt(data)
    with open('passwords.txt', 'ab') as f:
        f.write(encrypted_data)
        f.write(b'\n')

        
def get_information(keyword):
    with open('passwords.txt', 'rb') as f:
        for line in f:
            decrypted_data = decrypt(line)
            decrypted_data = decrypted_data.split('_')
            if decrypted_data[2] == keyword:
                return decrypted_data[0] + ' ' + decrypted_data[1]
    return 'Keyword not found'

#store_information('facebook', '123456', 'facebook')
#store_information('instagram', '123456', 'instagram')
#store_information('twitter', '123456', 'twitter')
#print(get_information('twitter'))