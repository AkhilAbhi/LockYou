#!/bin/bash

red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'




ged (){
    printf "${cyan}"
    figlet __Lock You__
    printf "${reset}"
    printf "${red}developer ${green}@AkhilAbhi\n"
    printf "${red}github${green}https://github.com/AkhilAbhi\n"
}


clear
ged
printf " "
printf " "
printf " "
printf "${red}[!]${yellow} removing home screen.. ${reset}\n"


cd /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
echo -e "PS1='\$' " > bash.bashrc



sleep 3

clear
ged
printf " "
printf " "
printf " "
printf "${red}[!]${green} lock removed from home screen ${reset} \n"

sleep 2
clear
ged


printf " "
printf " "
printf " "
printf "${red}[!] ${yellow} user name and password is deleting.... ${reset}"
cd /data/data/com.termux/files/usr/etc/
rm -rf user.txt
sleep 3
clear
ged
echo " "
echo " "
printf " "
printf " "
printf " "
printf "${red}[!] ${green} deleted..${reset}"
sleep 2
clear
ged

printf "${reset}"
cd $HOME