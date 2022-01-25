from requests import get, post
from bs4 import BeautifulSoup
from colorama import Fore, Style

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
    break
  else:
    print(f'{err()} Please enter a number')

data = {
  'ajax': 'post_question',
  'user': id,
  'question': ques,
  'userinfo': 'anonymous'  
}

sent = 0
for i in range(loop):
    response = post('https://qooh.me/processes/userprofile/index.php',  data=data)
    if response.status_code == 200:
      print(f'{suc()} Question sent successfully')
      sent += 1
    else:
      print(f'{err()} Error sending question')

print(f'{info()} Sent {sent} questions to https://qooh.me/{username}')
ext()


