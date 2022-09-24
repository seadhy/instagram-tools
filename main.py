from Dedection import Dedection
from getAllFollowed import Followed
from getAllFollowers import Followers
from os import system
from time import sleep
from json import load

def clear():
    system('cls')

clear()

userinfo = load(open('userinfo.json','r',encoding='utf-8'))

username = userinfo['username']
password = userinfo['password']

system('title coded by seadhy')

logo = """
      [coded by seadhy#9999]
      
[1] Get All Followers
[2] Get All Followed
[3] Dedection
[4] Escape
      
      """
print(logo)

while True:
    choice = int(input('> '))

    if choice == 1:
        Followers(username,password)
        sleep(3)
        input('press enter... ')
        clear()
        print(logo)
    elif choice == 2:
        Followed(username,password)
        sleep(3)
        input('press enter... ')
        clear()
        print(logo)
    elif choice == 3:
        Dedection()
        sleep(3)
        input('press enter... ')
        clear()
        print(logo)
    elif choice == 4:
        break