import socket
import threading

# Connection Data
host = "127.0.0.1"
port = 25565

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists for Clients and their Nicknames
clients = []
nicknames = []

# Sending messages to all connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv_message(1024)
            broadcast(message)
        except:
            # Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nickname[index]
            broadcast("{} discconnected".format(nickname).encode("ascii"))
            nicknames.remove(nickname)
            break

# Receiving / listening functionality
def receive():
    while True:
        # Accept connection
        client, address = server.accept()
        print("{} connected".format(str(address)))

        # Request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()