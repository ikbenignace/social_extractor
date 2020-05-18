import urllib.request
import tempfile
import os
import time
import logging
import shutil
import zipfile
from zipfile import ZipFile
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tkinter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# If you want to open Chrome



tkinter.messagebox.showinfo(title='Info', message='Please select the snapchat zip file.')
root = tk.Tk()
root.withdraw()
snap_zip_path = filedialog.askopenfilename()



root = tk.Tk()
root.withdraw()
tkinter.messagebox.showinfo(title='Info', message='Please select where you want the pictures to be saved')
destination_path = filedialog.askdirectory()

destination_path_urllib = destination_path + '/chromedriver.exe'
destination_path_urllib_zip = destination_path + '/chromedriver_win32.zip'

url = 'https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_win32.zip'




def change_Slashes(path):

    newpath = path.replace('/', "\\")

    return newpath

snap_zip_path = change_Slashes(snap_zip_path)
destination_path = change_Slashes(destination_path)



def download_files(path, path_driver):

    driver_path = path_driver
    print(driver_path)

    html_path = path + "\\html\\memories_history.html"
   

    prefs = {"download.default_directory": path}
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('prefs', prefs)
    chromedriver = driver_path
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)


    driver.get(html_path)

    

    
    logger = logging.Logger('catch_all')

    try:
        i = 2
        
        for i in range(2, 1000000):
            number = i +  1
            number = str(number)
            string = "//body/div[2]/table[1]/tbody[1]/tr["
            string2 = "]/td[3]/a[1]"
            total = str(string + number + string2)
            driver.find_element_by_xpath(total).click()
            i = i + 1
            time.sleep(1)
            


    except Exception as e:
        logger.error(e, exc_info=True)

        


    
    time.sleep(10)




def prepare_destination(url, destination_path, snap_zip_path, destination_path_urllib_zip):
    print('Perparing chrome driver')
    if os.path.isfile(destination_path_urllib):
        print('Driver Already Downloaded')
    else:
        print('Downloading driver')
        urllib.request.urlretrieve(url, destination_path_urllib_zip)
        zf = ZipFile(destination_path_urllib_zip, 'r')
        zf.extractall(destination_path)
        zf.close()


 
    zf = ZipFile(snap_zip_path, 'r')
    zf.extractall(destination_path)
    zf.close()
   

    



def main():
    print('test')
    



def check_isDirectory(path):
    if os.path.isdir(path):
        return True
    else:
        return False


def check_Empty(path):

    if path != "":
        return True
        
    else:
        return False


def check_isZip(path):

    if path.endswith('.zip'):
        if os.path.isfile(path):
            
            return True
        else:
            return False

        
    else:
        return False




def check_Paths():
    print('Checking paths...')
    print(snap_zip_path)
    print(destination_path)

    if check_isZip(snap_zip_path) == True & check_isDirectory(destination_path) == True:

        return True
        
        
    else:
        print('Fout pad')
        return False
   


print(check_Paths())



prepare_destination(url, destination_path, snap_zip_path, destination_path_urllib_zip)
download_files(destination_path, destination_path_urllib)

