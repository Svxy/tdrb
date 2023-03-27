import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"TDRB - TnyavnTos Discord Report Bot")

print(f"""

{b+Fore.GREEN}



                                                                                  
                                                                                  
TTTTTTTTTTTTTTTTTTTTTTTDDDDDDDDDDDDD      RRRRRRRRRRRRRRRRR   BBBBBBBBBBBBBBBBB   
T:::::::::::::::::::::TD::::::::::::DDD   R::::::::::::::::R  B::::::::::::::::B  
T:::::::::::::::::::::TD:::::::::::::::DD R::::::RRRRRR:::::R B::::::BBBBBB:::::B 
T:::::TT:::::::TT:::::TDDD:::::DDDDD:::::DRR:::::R     R:::::RBB:::::B     B:::::B
TTTTTT  T:::::T  TTTTTT  D:::::D    D:::::D R::::R     R:::::R  B::::B     B:::::B
        T:::::T          D:::::D     D:::::DR::::R     R:::::R  B::::B     B:::::B
        T:::::T          D:::::D     D:::::DR::::RRRRRR:::::R   B::::BBBBBB:::::B 
        T:::::T          D:::::D     D:::::DR:::::::::::::RR    B:::::::::::::BB  
        T:::::T          D:::::D     D:::::DR::::RRRRRR:::::R   B::::BBBBBB:::::B 
        T:::::T          D:::::D     D:::::DR::::R     R:::::R  B::::B     B:::::B
        T:::::T          D:::::D     D:::::DR::::R     R:::::R  B::::B     B:::::B
        T:::::T          D:::::D    D:::::D R::::R     R:::::R  B::::B     B:::::B
      TT:::::::TT      DDD:::::DDDDD:::::DRR:::::R     R:::::RBB:::::BBBBBB::::::B
      T:::::::::T      D:::::::::::::::DD R::::::R     R:::::RB:::::::::::::::::B 
      T:::::::::T      D::::::::::::DDD   R::::::R     R:::::RB::::::::::::::::B  
      TTTTTTTTTTT      DDDDDDDDDDDDD      RRRRRRRR     RRRRRRRBBBBBBBBBBBBBBBBB   
                                                                                  


{b+Fore.RED} x > {Fore.RESET}Options

{b+Fore.RED} {1} > {Fore.RESET}illegal Content {b+Fore.GREEN}::{Fore.RESET} 1
{b+Fore.RED} {2} > {Fore.RESET}Harassment {b+Fore.GREEN}::{Fore.RESET} 2
{b+Fore.RED} {3} > {Fore.RESET}Spam or Phishing Links {b+Fore.GREEN}::{Fore.RESET} 3
{b+Fore.RED} {4} > {Fore.RESET}Self Harm {b+Fore.GREEN}::{Fore.RESET} 4
{b+Fore.RED} {5} > {Fore.RESET}NSFW Content {b+Fore.GREEN}::{Fore.RESET} 5
""")

token = input(f"{b+Fore.RESET} > CLIENT TOKEN{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > Invalid Token")
        input()
guild_id1 = input(f"{b+Fore.BLUE} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.BLUE} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.BLUE} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.BLUE} > Option{Fore.RESET}: ")

def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.GREEN} > Sent Report {b+Fore.BLUE}::{Fore.GREEN} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"TDRB by TnyavnTo | Sent: %s" % sent)
      sent += 1
    elif r.status_code == 401:
      print(f"{Fore.RED} > Invalid token")
      input()
      exit()
    else:
      print(f"{Fore.RED} > Error")

print()
for i in range(500, 1000):
    Thread(target=Main).start()