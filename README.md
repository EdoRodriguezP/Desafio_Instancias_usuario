# Desafío Instancias de Usuario

Desafío Latam: Instancias de usuario

En este desafío validaremos nuestros conocimientos de manejo de archivos. Para lograrlo, necesitarás utilizar el archivo `Apoyo Desafío evaluado - Instancias de usuario.zip`.

Lee todo el documento antes de comenzar el desarrollo individual o grupal, para asegurarte de obtener el máximo puntaje y enfocar bien los esfuerzos.

## Descripción

Se solicita crear un script en Python que permita crear instancias de usuario a partir de los datos entregados en el archivo `usuarios.txt`, y almacene cada instancia creada en una lista.

Cada línea del archivo `usuarios.txt` contiene un texto en formato JSON, donde cada clave corresponde al nombre de un atributo de la clase `Usuario`, y su valor asociado corresponde al valor que debe tener dicho atributo en cada instancia creada.

Además, se debe manejar las posibles excepciones en cada intento de leer los datos de un usuario y crear una instancia a partir de ellos. En caso de que se produzca una excepción, se debe añadir el error al archivo `error.log`.

Se proporciona el archivo `usuario.py` que contiene la definición de la clase `Usuario`, y el archivo `usuarios.txt` que contiene los datos de los usuarios a ser creados.

## Requerimientos

1. Crear un archivo `script.py` que permita leer línea a línea el archivo `usuarios.txt`, y crear una instancia de `Usuario` a partir de los datos de cada línea leída.  
   **(5 puntos)**

2. En el mismo archivo, manejar las posibles excepciones al leer cada línea y/o generar cada instancia, y agregar la excepción en un archivo `error.log`.