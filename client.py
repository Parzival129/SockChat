# import all modules
import socket
import random
import time
from rich.console import Console
console = Console()
# put a cool looking title because you can
print ("")
print("   _____ _ _            _   ")
print("  / ____| (_)          | |  ")
print(" | |    | |_  ___ _ __ | |_ ")
print(" | |    | | |/ _ \ '_ \| __|")
print(" | |____| | |  __/ | | | |_ ")
print("  \_____|_|_|\___|_| |_|\__|")
print ("")

HEADER = 64
# input port for connection
PORT = input("Input port >> ")
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = input("Input the server IP: ")
ADDR = (SERVER, int(PORT))

# 192.168.56.1

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

console.print("You have connected to port: " + PORT, style="bold green")

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
    print ("")
    # Add somma that COLOR
    print ("Server,", end=' ')
    console.print(" [bold cyan]" + server_user_name + "[/bold cyan] >> ", end=' ')
    print (client.recv(2048).decode(FORMAT))
    #console.print(f"Server, {[bold cyan]server_user_name[/bold cyan]}  >>  {client.recv(2048).decode(FORMAT)}\\")
    print ("")

while True:

  message = input("send: ")
  if message == "quit":
    send(DISCONNECT_MESSAGE)
  else:
    send(message)
