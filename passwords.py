import password_management
import generador
import os
import logging

logging.basicConfig(
    filename='DEBUG.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S'
)

logging.debug('Start of program')

fin = False #por si acaso se sale en otro lado
password = ""

if not os.path.isfile('user_key.txt'):
    print("Bienvenido a Password Manager. Debes crear una contraseña para continuar")
    logging.info('user_key.txt no encontrado')
    while True:
        password = input("Ingresa una contraseña: ")
        password_confirmation = input("Confirma tu contraseña: ")
        if password == password_confirmation:
            print(password_management.store_user_password(password))
            logging.info('Contraseña creada')
            break
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo")
            logging.info('Contraseñas no coinciden')
    
print("Bienvenido a Password Manager. Ingresa tu contraseña para continuar")
while True:
    password = input("Ingresa tu contraseña: ")
    if password_management.validate_user_password(password):
        logging.info('Usuario loggeado')
        break
    else:
        print("Contraseña incorrecta. Intenta de nuevo")
        logging.info('Usuario ingresó contraseña incorrecta')

while not fin:
    comando = input("Ingresa un comando (agregar, borrar, actualizar, recuperar, generar o fin): ")
    if comando.lower() == "fin":
        print("Saliendo del programa...")
        logging.info("Saliendo del programa...")
        break
    elif comando.lower() == "agregar":
        print("Agregando...")
        nombre = input("Ingresa el login de la cuenta (email o username): ")
        contraseña = input("Ingresa la contraseña: ")
        palabra_clave = input("Ingresa una palabra clave (enter para dejar vacio): ")
        if palabra_clave == "":
            palabra_clave = None
        if password_management.store_information(nombre, contraseña, palabra_clave, password)== "Keyword or account already exists":
            print("La cuenta ya existe")
            logging.info("[Agregar] - La cuenta ya existe")
        else:
            print("Cuenta agregada exitosamente!")
            logging.info("[Agregar] - Cuenta agregada exitosamente")
    elif comando.lower() == "borrar":
        print("Borrando...")
        nombre = input("Ingresa el login o keyword de la cuenta a borrar: ") #o palabra clave?
        print(password_management.delete_information(nombre, password))
    elif comando.lower() == "actualizar":
        print("Actualizando...")
        nombre = input("Ingresa el login o keyword de la cuenta a actualizar: ")
        new_pass = input("Ingresa la nueva contraseña: ")
        print(password_management.update_information(nombre, new_pass, password))
    elif comando.lower() == "recuperar":
        print("Recuperando...")
        nombre = input("Ingresa el login o keyword de la cuenta a recuperar: ")
        print(password_management.get_information(nombre, password))
    elif comando.lower() == "generar":
        try:
            largo = int(input("Ingresa el largo de la contraseña: "))
            symb = input("Incluir simbolos? (s/n): ")
            if symb.lower() == "s" or symb.lower() == "si":
                symb = True
            else:
                symb = False
            mayus = input("Incluir mayusculas? (s/n): ")
            if mayus.lower() == "s" or mayus.lower() == "si":
                mayus = True
            else:
                mayus = False
            print(generador.generar(largo, symb, mayus))
            logging.info("[Generar] - Contraseña generada")
        except:
            print("Error al generar contraseña")
            logging.warning("[Generar] - Error al generar contraseña")
    else:
        print("Comando no reconocido")
        logging.info("Comando no reconocido")