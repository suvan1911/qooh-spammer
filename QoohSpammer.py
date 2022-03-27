from requests import get, post
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from os import system
import threading

init()
system("cls")

screenlock = threading.Semaphore(value=1)
THREADS = 50

def inp():
  return f'[{Fore.BLUE}input{Style.RESET_ALL}] »'

def info():
  return f'[{Fore.YELLOW}info{Style.RESET_ALL}] »'

def suc():
  return f'[{Fore.GREEN}success{Style.RESET_ALL}] »'

def err():
  return f'[{Fore.RED}err{Style.RESET_ALL}] »'

def ext():
  input('Press enter to exit: ')
  exit()

def get_uid(username):
  r = get(f'https://qooh.me/{username}')
  soup = BeautifulSoup(r.content, 'html.parser')
  id  = soup.find("input", {"type": "hidden", "name":"user"})
  if not id:
    print(f'{err()} Could not find the given username')
    ext()
  else:
    return id["value"]

sent = 0
def spam(data,max):
    global sent
    while sent < max:
      response = post('https://qooh.me/processes/userprofile/index.php',  data=data)
      if response.status_code == 200:
        screenlock.acquire()
        print(f'{suc()} {sent+1} Questions sent successfully', end = '\r')
        screenlock.release()
        sent += 1
      else:
        print(f'{err()} Error sending question') 
  
print(f'{info()} Qooh Spammer')
print(f'{info()} Created by: Len#7817 | https://github.com/suvan1911\n')

username = input(f'{inp()} Enter target qooh username: ')
id = get_uid(username)
ques = input(f'{inp()} Enter question: ')

loop = ''
while not loop.isdigit(): 
  loop = input(f'{inp()} How many times to send? ')
  if loop.isdigit():
    loop = int(loop)
    if loop < THREADS:
      THREADS = loop
    break
  else: 
    print(f'{err()} Please enter a valid number')
    
data = {
  'ajax': 'post_question',
  'user': id,
  'question': ques,
  'userinfo': 'anonymous'  
}

allThreads = []

for i in range(THREADS):
  t = threading.Thread(target=spam, args=(data,loop-(THREADS-1)))
  allThreads.append(t)
  t.start()

for t in allThreads:
  t.join()

print(f'{info()} Sent {sent} questions to https://qooh.me/{username}')

ext()
