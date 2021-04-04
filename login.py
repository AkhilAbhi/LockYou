import os
from getpass import getpass
import time


red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'



def cle():
    os.system("clear")


def hed():
    cle()
    print(cyan)
    os.system("figlet __Lock You__")
    print(reset)
    print(red+"developer "+green+"@AkhilAbhi")
    print(red+"github "+green+"https://github.com/AkhilAbhi")
    
            


while(1):
    try:
        hed()
        f=open("/data/data/com.termux/files/usr/etc/user.txt","r")
        usr=f.readline()
        usr=usr.strip()
        pas=f.readline()
        pas=pas.strip()
        #print(usr)
        #print(pas)
        f.close()
        print(" ")
        user=input(green+"username : "+reset)
        ppa=getpass(green+"password : "+reset )
        #print(user)
        #print(ppa)
        if user==usr:
            
            if ppa==pas:
                
                os.system("mpv aud/Granted.mp3")
                os.system("clear")
                exit()
                
            else:
                print(" ")
                print(" ")
                print(" ")
                print(red+"[×] "+yellow+"password not maching")
                print(reset)
                print(" ")
                print(" ")
                os.system("mpv aud/Denied.mp3")
            
            
        else:
            
            
            print(" ")
            print(" ")
            print(" ")
            print(red+"[×] "+yellow+"user name not maching")
            print(reset)
            print(" ")
            print(" ")
            os.system("mpv aud/usr.mp3")
            
    except Exception:
        print("try again")
    except KeyboardInterrupt:
        os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
    
