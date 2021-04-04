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
    os.system("figlet __Lock You__")
    print(reset)
    print(red+"developer "+green+"@AkhilAbhi")
    print(red+"github "+green+"https://github.com/AkhilAbhi")
def chainge():
    hed()
    print(reset)
    f=open("/data/data/com.termux/files/usr/etc/user.txt","r")
    usr=f.readline()
    usr=usr.strip()
    pas=f.readline()
    pas=pas.strip()
    
    olusr=input(green+"enter olde username: ")
    olpass=getpass("enter olde password: ")
    if olusr==usr:
        #print("hello")
        if olpass==pas:
            #print("hello")
            
            hed()
            print(reset)
            nn=input(green+"[*] enter new username : "+reset)
            np=getpass(green+"[*] enter new password : "+reset)
            ln=len(nn)
            if nn:
                if np:
                    f=open("/data/data/com.termux/files/usr/etc/user.txt","w")
                    f.write(f"{nn}\n")
                    f.write(np)
                    f.close()
                    
                    
                    
                else:
                    cle()
                    print(red+"[!] wrong "+reset)
            else:
                cle()
                print(red+"[!] wrong"+reset)
            
            
            
            
        
        else:
            print(reset)
            print(red+"[!]"+yellow+" incorrect password")
        
        
    else:
        print(reset)
        print(red+"[!]"+yellow+" incorrect username ")
    

def delt():
    cle()
    hed()
    print(reset)
    nm=input(yellow+"[*] enter username : " +reset)
    np=getpass(yellow+"[*] enter password : "+reset)
    f=open("/data/data/com.termux/files/usr/etc/user.txt","r")
    usr=f.readline()
    usr=usr.strip()
    pas=f.readline()
    pas=pas.strip()
    if nm==usr:
        if np==pas:
            print(reset)
            ys=input(yellow+"[?]"+reset+" delete termux lock (y or s ): ")
            
            if ys=="y" or ys=="Y":
                
                os.system("bash r.sh")
            elif ys=="n" or ys=="N":
                pass
                
            else:
                print(reset)
                print(red+"[!] "+yellow+"Wrong Input ")
            
        else:
            pass
            
            
    else:
        pass




    
    
def c():
    print(reset)
    print(yellow+"[1] "+green+"reset")
    print(yellow+"[2] "+green+"delet")
    var=input("enter number : "+reset)
    if var=="1":
        chainge()
    elif var=="2":
        delt()
    else:
        pass
        
hed()
c()