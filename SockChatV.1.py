import os
import time
print ("")
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
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
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



os.system('cls')

print ("")
print ("")
print ("███████╗ ██████╗  ██████╗██╗  ██╗ ██████╗██╗  ██╗ █████╗ ████████╗")
print ("██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██║  ██║██╔══██╗╚══██╔══╝")
print ("███████╗██║   ██║██║     █████╔╝ ██║     ███████║███████║   ██║   ")
print ("╚════██║██║   ██║██║     ██╔═██╗ ██║     ██╔══██║██╔══██║   ██║   ")
print ("███████║╚██████╔╝╚██████╗██║  ██╗╚██████╗██║  ██║██║  ██║   ██║   ")
print ("╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ")
print ("                   Programmed By, Russell Tabata                  ")
print ("                        Innovecore Inc.                           ")
print ("")
print ("Do you want to join or create a chat session?")
print ("1. JOIN")
print ("2. CREATE")
print ("")

task = input("> ")

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
  
