import socket
import argparse
from cryptography.fernet import Fernet

# Se preparan datos de la conexión:
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

# Establecer conexión:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

(conn, addr) = s.accept()
print("Dirección de conexión: ", addr)
while True:
    msj_cifrado = conn.recv(BUFFER_SIZE)
    conn.send(b"Enterado. Hasta luego.")
    break 
conn.close()

# Generar el objeto para cifrar.
file = open('clave.key', 'rb')
clave = file.read()
file.close()
cipher_suite = Fernet(clave)

mensaje_bytes = cipher_suite.decrypt(msj_cifrado, None)
mensaje = mensaje_bytes.decode()
print("Mensaje recibido: ", mensaje)




'''
HOST = "0.0.0.0"
PORT = 4444
SIZE = 1024
s = socket.socket()
# bind the socket to all IP addresses of this host
s.bind((HOST,PORT))
# make the PORT reusable
# when you run the server multiple times in Linux, Address already in use error will raise
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"[*]Listening as {HOST}:{PORT} ...")
# accept any connections attempted
client_socket, client_address = s.accept()
print(f"[*]{client_address[0]}:{client_address[1]} Connected!")
# just sending a message, for demonstration purposes
message = "[*]Hello and Welcome".encode()
client_socket.send(message)
while True:
    # get the command from prompt
    command = input("[*]>")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()
'''