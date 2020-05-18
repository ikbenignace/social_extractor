#Main file
#Zip Selector
#Invoke script for selected platform


def snap(): #Start the snapchat script

    print('test')
    exec(open("snap.py").read())


while True:
    platform_selector = input('Enter the number of the platform.. ')

    if int(platform_selector) == 1:
        snap()

