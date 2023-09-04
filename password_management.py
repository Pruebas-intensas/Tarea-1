import os
from cryptography.fernet import Fernet
import base64
import bcrypt
import logging

def store_user_password(password):
    try:    
        if not os.path.isfile('user_key.txt'):
            with open('user_key.txt', 'wb') as f:
                pass
        else:
            os.remove('user_key.txt')
            with open('user_key.txt', 'wb') as f:
                pass
        # store the hashed password in the file
        with open('user_key.txt', 'ab') as f:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            f.write(hashed_password)
        
        logging.info('Contraseña guardada')
        return 'Password stored'
    except:
        logging.warning('Error al guardar la contraseña')
        return -1


def validate_user_password(password):
    try:
        if not os.path.isfile('user_key.txt'):
            with open('user_key.txt', 'wb') as f:
                pass
        with open('user_key.txt', 'rb') as f:
            for line in f:
                hashed_password = line
                if bcrypt.checkpw(password.encode(), hashed_password):
                    logging.info('Contraseña validada correctamente')
                    return True
        return False
    except:
        return -1


def encrypt(word, master_key):
    try: 
        fernet = Fernet(base64.urlsafe_b64encode(master_key.encode().ljust(32)))
        encrypted_word = fernet.encrypt(word.encode())
        return encrypted_word
    except:
        return -1


def decrypt(word, master_key):
    try:
        fernet = Fernet(base64.urlsafe_b64encode(master_key.encode().ljust(32)))
        decrypted_word = fernet.decrypt(word).decode()
        return decrypted_word
    except:
        return -1


def get_information(word, master_key):
    try:
        if validate_user_password(master_key) == False:
            return 'Wrong password'
        if not os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'wb') as f:
                pass
        with open('passwords.txt', 'rb') as f:
            for line in f:
                decrypted_data = decrypt(line, master_key)
                decrypted_data = decrypted_data.split('_')
                if decrypted_data[2] == word or decrypted_data[0] == word:
                    return decrypted_data[0] + ' ' + decrypted_data[1]
        return 'Not found'
    except:
        return -1


def store_information(account, password, keyword, master_key):
    try:
        if validate_user_password(master_key) == False:
            return 'Wrong password'
        if not os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'wb') as f:
                pass
        with open('passwords.txt', 'rb') as f:
            for line in f:
                decrypted_data = decrypt(line, master_key)
                decrypted_data = decrypted_data.split('_')
                if decrypted_data[2] == keyword or decrypted_data[0] == account:
                    return 'Keyword or account already exists' # esto deberia ser un error
        # if not, store information
        with open('passwords.txt', 'ab') as f:
            encrypted_data = encrypt(account + '_' + password + '_' + keyword, master_key)
            f.write(encrypted_data + b'\n')
        return 'Information stored'
    except:
        return -1

        
def update_information(word, new_password, master_key):
    try:
        if validate_user_password(master_key) == False:
            return 'Wrong password'
        if not os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'wb') as f:
                pass
        with open('passwords.txt', 'rb') as f:
            for line in f:
                decrypted_data = decrypt(line, master_key)
                decrypted_data = decrypted_data.split('_')
                if decrypted_data[2] == word or decrypted_data[0] == word:
                    account = decrypted_data[0]
                    keyword = decrypted_data[2]
                    print(delete_information(word, master_key))
                    print(store_information(account, new_password, keyword, master_key))
                    return 'Information updated'
        return 'Keyword or Account not found' # esto deberia ser un error
    except:
        return -1

def delete_information(word, master_key):
    try:
        lista_aux = []
        flag_found = False
        if validate_user_password(master_key) == False:
            return 'Wrong password'
        if not os.path.isfile('passwords.txt'):
            with open('passwords.txt', 'wb') as f:
                pass
        with open('passwords.txt', 'rb') as f:
            for line in f:
                decrypted_data = decrypt(line, master_key)
                decrypted_data = decrypted_data.split('_')
                if decrypted_data[2] != word and decrypted_data[0] != word:
                    lista_aux.append(line)
                else:
                    flag_found = True
        if flag_found == False:
            return 'Keyword or Account not found'
        with open('passwords.txt', 'wb') as f:
            for line in lista_aux:
                f.write(line)  
        return 'Information deleted'
    except:
        return -1


#print(store_information('facebook', '123456', 'face', '123456'))
#store_information('instagram', '123456', 'insta')
#store_information('twitter', '123456', 'X')
#print(get_information('twitter'))
#print(get_information('face', '123456'))
