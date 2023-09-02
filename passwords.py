passwords = {}

fin = False #por si acaso se sale en otro lado

while not fin:
    comando = input("Ingresa un comando (agregar, borrar, actualizar, recuperar o fin): ")
    if comando.lower() == "fin":
        print("Saliendo del programa...")
        break
    elif comando.lower() == "agregar":
        print("Agregando...")
        nombre = input("Ingresa el login de la cuenta (email o username): ")
        contraseña = input("Ingresa la contraseña: ")
        palabra_clave = input("Ingresa una palabra clave (enter para dejar vacio): ")
        if palabra_clave == "":
            palabra_clave = None
        passwords[nombre] = [contraseña, palabra_clave]
        print("Cuenta agregada exitosamente!")
    elif comando.lower() == "borrar":
        print("Borrando...")
        nombre = input("Ingresa el login de la cuenta a borrar: ") #o palabra clave?
        if nombre in passwords:
            del passwords[nombre]
            print("Cuenta borrada exitosamente!")
        else:
            print("No se encontro la cuenta")
    elif comando.lower() == "actualizar":
        print("Actualizando...")
        nombre = input("Ingresa el login de la cuenta a actualizar: ")
        if nombre in passwords:
            contraseña = input("Ingresa la contraseña: ")
            palabra_clave = input("Ingresa una palabra clave (enter para dejar vacio): ")
            if palabra_clave == "":
                palabra_clave = None
            passwords[nombre] = [contraseña, palabra_clave]
            print("Cuenta actualizada exitosamente!")
        else:
            print("No se encontro la cuenta")
    elif comando.lower() == "recuperar":
        print("Recuperando...")
        nombre = input("Ingresa el login de la cuenta a recuperar: ")
        if nombre in passwords:
            print("La contraseña es: " + passwords[nombre][0])
        else:
            print("No se encontro la cuenta")
    else:
        print("Comando no reconocido")
