from random2 import *
import os

clear = lambda: os.system('cls')

#Ideas:
#-Add file writer
#-Add password checker

def logo():
    print("""

\033[1;31;40m /$$$$$$$                               /$$$$$$                     \033[0;36;40m             /$$$$$$       /$$
\033[1;31;40m| $$__  $$                             /$$__  $$                    \033[0;36;40m            /$$$_  $$    /$$$$
\033[1;31;40m| $$  \ $$ /$$$$$$   /$$$$$$$ /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$$ \033[0;36;40m /$$    /$$| $$$$\ $$   |_  $$
\033[1;31;40m| $$$$$$$/|____  $$ /$$_____//$$_____/| $$ /$$$$ /$$__  $$| $$__  $$\033[0;36;40m|  $$  /$$/| $$ $$ $$     | $$
\033[1;31;40m| $$____/  /$$$$$$$|  $$$$$$|  $$$$$$ | $$|_  $$| $$$$$$$$| $$  \ $$\033[0;36;40m \  $$/$$/ | $$\ $$$$     | $$
\033[1;31;40m| $$      /$$__  $$ \____  $$\____  $$| $$  \ $$| $$_____/| $$  | $$\033[0;36;40m  \  $$$/  | $$ \ $$$     | $$
\033[1;31;40m| $$     |  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$\033[0;36;40m   \  $/   |  $$$$$$//$$ /$$$$$$
\033[1;31;40m|__/      \_______/|_______/|_______/  \______/  \_______/|__/  |__/\033[0;36;40m    \_/     \______/|__/|______/



\033[1;37;40m
PassGen v0.1 made by \033[1;35;40mTataQueen\033[1;37;40m(https://github.com/\033[1;35;40mTataQueen\033[1;37;40m/passgen)
Please do not distribute without giving credit to the author(s): \033[1;35;40m@TataQueen\033[1;37;40m
""")


def start(err):
    logo()
    print('Select an option from down below: ')
    print("""
\033[1;31;40m1. Default (12C, YN, NSC) [Not recommended!]
\033[1;33;40m2. Complex (12C, YN, YSC) [Recommended]
\033[1;32;40m3. Master (32C, YN, YSC) [Most secure]
\033[1;35;40m9. Custom
\033[1;37;40m99. Exit program
""")
    if err==1:
        print("That's not a number...")
    elif err==2:
        print("That's not a valid option, try again.")
    elif err==3:
        print("That function is WIP (Work-In-Progress). Check for updates on github(soon)!")
    try:
        sel=int(input('To be selected: '))
    except ValueError:
        clear()
        start(1)
    else:
        selection(sel)

def selection(n):
    if n==1:
        PassGen(12, True, False)
    elif n==2:
        PassGen(12, True, True)
    elif n==3:
        PassGen(32, True, True)
    elif n==9:
        customization()
    elif n==99:
        clear()
        exit()
    else:
        clear()
        start(2)

def customization():
    clear()
    logo()
    print("Password customization menu, please follow the instructions as intended, or it will restart.\n")
    try:
        n=int(input('Number of chars [0,32768]: '))
        num=str(input('Numbers? [y/n]: '))
        scs=str(input('Special characters? [y/n]: '))
    except ValueError or TypeError:
        print('Not a valid value...')
        customization()
    else:
        if n>32768:
            print('Too big!')
            customization()
        elif n<0:
            print('Too small, she said.')
            customization()
        if num=="y":
            num=True
        elif num=="n":
            num=False
        if scs=="y":
            scs=True
            PassGen(n,num,scs)
        elif scs=="n":
            scs=False
            PassGen(n,num,scs)
        else:
            print("Not valid, try again.")
            customization()


def PassGen(nchars,nums,specialchars):
    schars=['!','@','#','$','&','.',',',';','-','_','+','=']
    if nums==False and specialchars==False:
        print('NN')
        passwd=[]
        cc=""
        for i in range(0,nchars):
            mm=randint(0,1)
            if mm==0:
                cc=chr(randint(97,122))
                passwd.append(cc)
            elif mm==1:
                cc=chr(randint(65,90))
                passwd.append(cc)
        print(passwd)
    elif nums==True and specialchars==False:
        print('YN')
        passwd=[]
        cc=""
        nn=""
        for i in range(0,nchars):
            con=randint(0,1)
            if con==0:
                mm=randint(0,1)
                if mm==0:
                    cc=str(chr(randint(97,122)))
                    passwd.append(cc)
                elif mm==1:
                    cc=str(chr(randint(65,90)))
                    passwd.append(cc)
            elif con==1:
                nn=str(randint(0,9))
                passwd.append(nn)
        print(passwd)

    elif nums==True and specialchars==True:
        print('YY')
        passwd=[]
        cc=""
        nn=""
        sc=""
        for i in range(0,nchars):
            conos=randint(0,2)
            if conos==0:
                mm=randint(0,1)
                if mm==0:
                    cc=str(chr(randint(97,122)))
                    passwd.append(cc)
                elif mm==1:
                    cc=str(chr(randint(65,90)))
                    passwd.append(cc)
            elif conos==1:
                nn=str(randint(0,9))
                passwd.append(nn)
            elif conos ==2:
                sc=randint(0,len(schars)-1)
                passwd.append(schars[sc])
        print(passwd)

clear()
start(0)
