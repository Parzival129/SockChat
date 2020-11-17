# import all modules
import os
import time
from rich.console import Console
console = Console()
print ("")

# creating a progress bar because it looks cool, not because it tells you the status of the programs loading

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    console.print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd, style="bold white")
    # Print New Line on Complete
    if iteration == total: 
        print()

# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.02)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

# Display main menu

os.system('cls')

print ("")
print ("")
# Add somma that nice colorssss
console.print("███████╗ ██████╗  ██████╗██╗  ██╗ ██████╗██╗  ██╗ █████╗ ████████╗", style="bold yellow")
console.print("██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝", style="bold yellow")
console.print("███████╗██║   ██║██║     █████╔╝ ██║     ███████║███████║   ██║   ", style="bold yellow")
console.print("╚════██║██║   ██║██║     ██╔═██╗ ██║     ██╔══██║██╔══██║   ██║   ", style="bold yellow")
console.print("███████║╚██████╔╝╚██████╗██║  ██╗╚██████╗██║  ██║██║  ██║   ██║   ", style="bold yellow")
console.print("╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ", style="bold yellow")
console.print("                   Programmed By, Russell Tabata                  ", style="bold yellow")
console.print("                        Innovecore Inc.                           ", style="bold yellow")
print ("")
print ("Do you want to join or create a chat sesion?")
console.print("1. [bold]JOIN[/bold]")
console.print("2. [bold]CREATE[/bold]")
print ("")

task = input("> ")
# My code is so unefficient
if task == 'join':
  os.system('cls')
  print ("")
  import client

if task == 'JOIN':
  os.system('cls')
  print ("")
  import client

elif task == '1':
  os.system('cls')
  print ("")
  import client

elif task == 'create':
  os.system('cls')
  print ("")
  import server

elif task == 'CREATE':
  os.system('cls')
  print ("")
  import server

elif task == '2':
  os.system('cls')
  print ("")
  import server

else:
  print ("")
  print ("That is not an option")
  time.sleep(5)
  exit()

