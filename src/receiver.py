from socket import *
import json
from datetime import datetime

serverHost = ""
serverPort = 2000
serverAddress = (serverHost, serverPort)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(serverAddress)
serverSocket.listen(1)
clientSocket, clientAddress = serverSocket.accept()
print("connection accepted and started!")

try:
    while True:
        recv_data = clientSocket.recv(1024)
        if not recv_data:
            data = ""
            continue
        else:
            data = json.loads(recv_data.decode('utf-8'))

        logs = open("logs.txt", 'a')
        now = datetime.now()
        logs.write(f"Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        logs.write(f"{data}\n\n")
        logs.close()
except (KeyboardInterrupt, ConnectionResetError):
    print("\nExiting gracefully... bye!")
    clientSocket.close()