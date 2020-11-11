import socket
import random

print ("")
print ("   _____ _ _            _   ")
print ("  / ____| (_)          | |  ")
print (" | |    | |_  ___ _ __ | |_ ")
print (" | |    | | |/ _ \ '_ \| __|")
print (" | |____| | |  __/ | | | |_ ")
print ("  \_____|_|_|\___|_| |_|\__|")
print ("")

HEADER = 64
PORT = input("Input port >> ")
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.86.222'
ADDR = (SERVER, int(PORT))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

Objects = ['Emu', 'Unicorn','Pineapple','Thermometre','Cucumber','Goat','Sheep','Clock','Teletubby','Chicken','Giraffe','Laptop','Paperclip','Lunchbag','Egg','Monitor','Keyboard','Password','Can','Notepad','Calander']
Describers = ['Rotten','Smart','Deluxe','Pregnant','Handy','Amusing','Hard-To-Find','Oafish','Observant','Hushed','Tangible','Witty','Incredible','Flagrant','Upset','Jealous','Untidy','Fat','Demonic','Ugly']
Server_O = random.choice(Objects)
Server_D = random.choice(Describers)

server_user_name = Server_D + " " + Server_O

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Server, " + server_user_name + " >> " + client.recv(2048).decode(FORMAT))

while True:

  message = input("send: ")
  if message == "quit":
    send(DISCONNECT_MESSAGE)
  else:
    send(message)
