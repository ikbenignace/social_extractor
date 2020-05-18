#Main file
#Zip Selector
#Invoke script for selected platform
import os


#VARIABLES
script_directory = os.path.dirname(os.path.realpath(__file__))

#Main

print()
def snap(): #Start the snapchat script

    path_snap_script = script_directory + '/snap.py'
    exec(open(path_snap_script).read())


while True:
    platform_selector = input('Enter the number of the platform.. ')

    if int(platform_selector) == 1:
        snap()

    else:
        pass




