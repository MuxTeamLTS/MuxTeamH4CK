import os
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
from colorama import Fore
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system('pip install pyfiglet')
import time
os.system("clear")

list_numbers = ["1" , "2"]

while True:
	os.system("clear")
	print("\033[31m")
	print("====================================")
	print("|       MuxTeamH4CK DDoS ATTACK    |")
	print("|                                  |")
	print(Fore.RED + "| [1] IP DDoS                      |")
	print(Fore.RED + "| [2] Minecraft Ping               |")
	print("|                                  |")
	print("| Teams: EnderBob x ItzMuxGamer    |")
	print("====================================")
	
	player = input(Fore.RED + "root@MuxTeamH4CK: ")
	
	if player == '2':
		os.system("clear")
		print("===========================")
		print("|       MuxTeamH4CK       |")
		player_4_ip = input(Fore.RED + "IP: ")
		player_4_port = input(Fore.RED + "Port: ")
		time.sleep(2)
		os.system("clear")
		os.system("pyfiglet --color=RED MuxTeamH4CK")
		os.system(f"python3 ping.py {player_4_ip} -p {player_4_port}")
		
	if player == '1':
		os.system("clear")
		os.system("python3 stress.py")		
		
