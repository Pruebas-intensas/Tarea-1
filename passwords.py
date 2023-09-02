import password_management

fin = False #por si acaso se sale en otro lado

while not fin:
    comando = input("Ingresa un comando (agregar, borrar, actualizar, recuperar o fin): ")
    if comando.lower() == "fin":
        print("Saliendo del programa...")
        break
    elif comando.lower() == "agregar":
        print("Agregando...")
        nombre = input("Ingresa el login o keyword de la cuenta (email o username): ")
        contraseña = input("Ingresa la contraseña: ")
        palabra_clave = input("Ingresa una palabra clave (enter para dejar vacio): ")
        if palabra_clave == "":
            palabra_clave = None
        print(password_management.store_information(nombre, contraseña, palabra_clave))
        print("Cuenta agregada exitosamente!")
    elif comando.lower() == "borrar":
        print("Borrando...")
        nombre = input("Ingresa el login o keyword de la cuenta a borrar: ") #o palabra clave?
        print(password_management.delete_information(nombre))
    elif comando.lower() == "actualizar":
        print("Actualizando...")
        nombre = input("Ingresa el login o keyword de la cuenta a actualizar: ")
        print(password_management.update_information(nombre))
    elif comando.lower() == "recuperar":
        print("Recuperando...")
        nombre = input("Ingresa el login o keyword de la cuenta a recuperar: ")
        print(password_management.get_information(nombre))
    else:
        print("Comando no reconocido")