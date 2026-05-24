DANIELA ANDREA JARABA ESCOBAR 
Ficha:3407180
# Descripción general

El presente proyecto consiste en el desarrollo de una API básica utilizando FastAPI.  
Su objetivo es permitir el acceso a información de un proyecto y visualizar un conjunto de clientes mediante distintas rutas de acceso conocidas como endpoints.

# Creación del proyecto

Inicialmente se creó una carpeta con el nombre `nombre_pro_clientes` en el escritorio.  
Luego, esta carpeta fue abierta desde Visual Studio Code para empezar a trabajar en la aplicación.

# Generación del entorno virtual

Dentro de Visual Studio Code se utilizó la terminal integrada para crear un entorno virtual ejecutando el siguiente comando:

py -m venv yober

Este comando genera un entorno independiente llamado `Dani`, el cual facilita la administración de librerías y paquetes sin alterar la configuración principal de Python.

# Activación del entorno

Después de crear el entorno virtual, se procedió a habilitarlo mediante el siguiente comando:

.\yober\Scripts\activate

Al activarse correctamente, el nombre `(Dani)` aparece al inicio de la terminal, indicando que el entorno virtual ya está en uso.

# Instalación de FastAPI

Con el entorno virtual activo, se realizó la instalación del framework usando el siguiente comando:

pip install "fastapi[standard]"

Esta instrucción instala FastAPI junto con las dependencias necesarias para el funcionamiento de la API.

# Verificación de paquetes instalados

Para revisar las librerías instaladas dentro del entorno virtual, se ejecutó el siguiente comando:

pip list

Esto permitió confirmar que FastAPI y sus dependencias se encontraban correctamente instaladas.

# Archivo principal del proyecto

Posteriormente se creó el archivo `main.py`, encargado de contener la estructura principal de la API y los diferentes endpoints.

Las primeras líneas escritas fueron:

from fastapi import FastAPI 

app = FastAPI()

## Explicación

`from fastapi import FastAPI`  
Importa la clase FastAPI necesaria para desarrollar la aplicación.

`app = FastAPI()`  
Inicializa la API principal sobre la cual se crearán las rutas y funcionalidades.

# Implementación de endpoints

@app.get("/proyecto")

def mensaje():
    return {"proyecto": "este es el proyecto de clientes a desarrollar"}

# Explicación

Este endpoint crea la ruta `/proyecto`.  
Cuando un usuario entra a esta dirección, la API devuelve una respuesta en formato JSON con información relacionada al proyecto.

# Endpoint de clientes

lista_clientes = ["Ricardo","yoberson","quiroga","daniela","ana","kamila","zuelima"]

@app.get("/clientes")
def clientes():
    return {"clientes": lista_clientes}

# Explicación

Este endpoint corresponde a la ruta `/clientes`.  
Su función es retornar una lista de clientes almacenados previamente dentro de una variable.

# inicializacion de la api 

Para iniciar la API se utilizó el siguiente comando:

fastapi dev main.py

