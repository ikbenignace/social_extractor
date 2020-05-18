import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

path = input("Gelieve het pad in te vullen: ")

def main():
    print('test')
    os.chdir(path)
    os.chdir('html')
    print(os.getcwd())
    f = open("memories_history.html", "r")
    print(f.read())
    



def check_Path():
    if os.path.isdir(path):
        main()
    else:
        return False


def check_Empty():

    if path != "":
        check_Path()
        
    else:
        return False
        
        





check_Empty()