from os import system
from time import sleep
from json import load
from modules.Dedection import checkFollowers
from modules.getAllFollowed import getFollowed
from modules.getAllFollowers import getFollowers


def clear():
    system('cls')


clear()

userinfo = load(open('userinfo.json', 'r', encoding='utf-8'))

username = userinfo['username']
password = userinfo['password']

system('title coded by github.com/seadhy')

logo = """
      [coded by github.com/seadhy]
      
[1] Get All Followers
[2] Get All Followed
[3] Dedection
[4] Escape
      
      """
print(logo)

while True:
    choice = int(input('> '))

    if choice == 1:
        getFollowers(username, password)
        sleep(3)
        input('Press enter... ')
        clear()
        print(logo)
    elif choice == 2:
        getFollowed(username, password)
        sleep(3)
        input('Press enter... ')
        clear()
        print(logo)
    elif choice == 3:
        checkFollowers()
        sleep(3)
        input('Press enter... ')
        clear()
        print(logo)
    elif choice == 4:
        break
