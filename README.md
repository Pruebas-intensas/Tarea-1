# Tarea 1 - Gestor de Contraseñas

## Gestor de contraseñas en Python

Es un gestor de contraseñas local que tiene la opcion de agreagar, eliminar, modificar y ver las contraseñas guardadas. Además existe un modulo para generar constaseñas aleatorias, que pueden ser usadas como recomendaciones para las cuentas del usuario.

## Instalación

Instalar [Python](https://www.python.org/) en el sistema.

Installar las dependencias:
```bash
pip install -r requirements.txt
```

### Supuestos

1. El programa se usa de forma local en la linea de comandos
2. Solo puede haber una palabra clave por cuenta
3. La palabra clave es opcional
4. El programa termina con el comando `fin`
5. El comando actualizar recibe la cuenta y actualiza la contraseña
6. El generador de contraseñas tiene 3 parametros configurables, largo, si se usan caracteres especiales y si se usan numeros.
7. El generador siempre incluye numeros
8. EL generador tiene por defecto largo 8, sin caracteres especiales y sin mayusculas.

## Uso

```bash
python passwords.py
```

* Cuando se inicia el programa por primera vez, se pedirá que se ingrese una contraseña nueva
* Una vez creada, cada vez que se quiera usar el programa se debe ingresar esa contraseña

* El programa provee los siguientes comandos para administrar las contraseñas:
* Escribir `agregar` y luego ingresar el nombre de usuario y la contraseña. Opcionalmente se pide una palabra clave para recordar la cuenta.
* Escribir `eliminar` y luego ingresar el nombre de usuario o palabra clave de la cuenta que se desea eliminar.
* Escribir `actualizar` y luego ingresar el nombre de usuario o palabra clave de la cuenta que se desea modificar. Luego se pide ingresar la nueva contraseña.
* Escribir `recuperar` y luego ingresar el nombre de usuario o palabra clave de la cuenta que se desea ver.
* Escribir `fin` para terminar la ejecución del programa.

## Como contribuir

Todas las *Pull Request* son bienvenidas. Para cambios mayores, por favor abrir un *issue* primero para discutir lo que le gustaria cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
