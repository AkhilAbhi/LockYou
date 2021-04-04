import os
from getpass import getpass



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
    os.system("figlet __Lock You__ ")
    print(reset)
    print(red+"developer "+green+"@AkhilAbhi")
    print(red+"github"+green+"https://github.com/AkhilAbhi")
    
def setpass():
    if not os.path.exists("/data/data/com.termux/files/usr/etc/user.txt"):
        
        usrname=input(green+"username : "+reset)
        print(" ")
        pas=input(green+"password : "+reset)
        print(" ")
        repas=input(green+"re enter password : " +reset)
        print(" ")
        
        if pas==repas:
            user=open("/data/data/com.termux/files/usr/etc/user.txt","w")
            user.write(f"{usrname}\n")
            user.write(repas)
            user.close()
            
        else:
            print(red+"not maching password " +reset)
            
        
    else:
        print(red+"[!] " + yellow +"allredy  set password"+reset)
        print(" ")
        res=input(red+"[?] "+reset+"do you want reset password (y or n) : ")
        if res=="y" or res=="Y":
            os.system("python reset.py")
            
        elif res=="n" or res=="N":
            exit()
        else:
            print(red+"[!] "+yellow+"wrong input")
        
hed()
setpass()