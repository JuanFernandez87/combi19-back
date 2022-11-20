# combi19-back


## Requisitos

- python - **3.8.10**
- pip - **20.0.2**
- virtualenv - **20.13.2**

# Descargar proyecto

Descargar el proyecto desde el repositorio.

```
git clone git@gitlab.com:juanfernandez87/combi19-back.git
```

# Crear entorno virtual

Una vez que tengamos el proyecto descargado nos situamos dentro de la carpeta y abrimos una terminal (git bash) para crear un entorno virtual e instalar las librerias que se utilizan para el funcionamiento del script.

```
virtualenv venv
```
Se creara una carpeta con el nombre venv, para iniciar el proyecto ejecutamos el siguiente comando que activa el entorno virtual.

Windows:
```
venv\Scripts\activate. bat.
```

Linux:
```
source venv/bin/activate
```

Si todo salió bien se debería ver el nombre de nuestro entorno virtual en la terminal,  en este caso venv.

```
(venv) User@DESKTOP ~/combi19-back
```

# Iniciar proyecto

Una vez que tenemos el entorno virtual activado, nos vamos a la carpeta del proyecto e instalamos las dependencias.

```
pip install -r requirements.txt
```
# Ejecutar servidor 

Para correr el servidor ejecutamos el comando:

```
uvicorn app.main:app --reload
```
