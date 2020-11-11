import socket 
import threading
import random

print ("")
print ("   _____                          ")
print ("  / ____|                         ")
print (" | (___   ___ _ ____   _____ _ __ ")
print ("  \___ \ / _ \ '__\ \ / / _ \ '__|")
print ("  ____) |  __/ |   \ V /  __/ |   ")
print (" |_____/ \___|_|    \_/ \___|_|   ")
print ("")

HEADER = 64
PORT = input("Select a port for server: ")
SERVER = '192.168.86.222'
ADDR = (SERVER, int(PORT))
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

count = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

Objects = ['Emu','Unicorn','Pineapple','Thermometre','Cucumber','Goat','Sheep','Emu','Clock','Teletubby','Chicken','Giraffe','Laptop','Paperclip','Lunchbag','Egg','Monitor','Keyboard','Password','Can','Notepad','Calander']
Describers = ['Rotten','Smart','Deluxe','Pregnant','Handy','Amusing','Hard-To-Find','Oafish','Observant','Hushed','Tangible','Witty','Incredible','Flagrant','Upset','Jealous','Untidy','Fat','Demonic','Ugly']

def handle_client(conn, addr):
    User_O = random.choice(Objects)
    User_D = random.choice(Describers)

    name = (User_D + " " + User_O)

    print(f"[NEW CONNECTION] {addr} connected. User Name: {name}")
    
    connected = True
    count = 0
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}, {name}] >> {msg}")
            server_to_clients = input("send: ")
            conn.send(server_to_clients.encode(FORMAT))

    conn.close()
        

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    server.send(send_length)
    server.send(message)
    print(client.recv(2048).decode(FORMAT))

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER} on port {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
