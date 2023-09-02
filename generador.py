def generar(largo = 8, symb = False, mayus = False):
    """
    Genera una contraseña aleatoria de largo 'largo', con o sin simbolos y/o mayusculas
    """
    import random
    import string

    if symb:
        if mayus:
            caracteres = string.ascii_letters + string.digits + string.punctuation
        else:
            caracteres = string.ascii_lowercase + string.digits + string.punctuation
    else:
        if mayus:
            caracteres = string.ascii_letters + string.digits
        else:
            caracteres = string.ascii_lowercase + string.digits
    contraseña = ""
    for i in range(largo):
        contraseña += random.choice(caracteres)
    return contraseña