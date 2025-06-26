from usuario import Usuario
import datetime
import json
import pytz

# Configura la zona horaria de Chile
tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

# Lista para almacenar las instancias de Usuario creadas
instancias = []

# Abre el archivo de usuarios para leer línea por línea
with open("usuarios.txt") as u:
    linea = u.readline()
    while linea:
        try:
            # Intenta cargar la línea como un diccionario desde JSON
            usuario = json.loads(linea)
            # Crea una instancia de Usuario y la agrega a la lista
            instancias.append(Usuario(
                usuario.get("nombre"),
                usuario.get("apellido"),
                usuario.get("email"),
                usuario.get("genero")
            ))
        except Exception as e:
            # Si ocurre un error, lo escribe en error.log con la fecha y hora
            with open("error.log", "a+") as log:
                log.write(f"{datetime_CL.strftime('%d/%m/%Y %H:%M:%S')}, {e} \n")
        finally:
            # Lee la siguiente línea
            linea = u.readline()

# Imprime la lista de instancias








