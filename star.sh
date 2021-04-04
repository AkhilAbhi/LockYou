#!/bin/bash
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'

clear

ged (){
    printf "${cyan}"
    figlet __Lock You__
    printf "${reset}"
    printf "${red}developer ${green}@AkhilAbhi\n"
    printf "${red}github${green}https://github.com/AkhilAbhi\n"
}

printf "${green} whaite chekking required package...\n"
sleep 1

for i in git python figlet mpv ; do
clear
printf "${yellow} [*] chekking $i"
sleep 1
		 if [ -e ${PREFIX}/bin/$i ]; then
		  	printf "${green} \n$i is Already installed\n ${reset}"
		  	sleep 2
		  else
		  	printf "${blue} [*]Installing ${i}....${reset}"
                        sleep 1
		  	apt install $i -y || {
		  		printf "${red}"
		  	    echo ""
		  		echo "ERROR: Check your internet connection"
		  		printf "$reset"
		  		exit 1
		  	}
		  fi
		  done
		  
		  
clear

ged


printf "${yellow} setup lock in your termux (y or n ): ${reset}"
read lock
if [ $lock == "y" ]
then
    clear
    printf "${green} please white... \n "
    python register.py
   
elif [ $lock == "n" ]; then
     exit 1
else
   printf "${red} [!] ${yellow} wrong input \n"
   exit 1
fi

cd $HOME
cd ..
cd usr/etc
rm -rf bash.bashrc
echo -e "PS1='\$'\ncd $HOME\ncd lock\npython login.py\ncd $HOME" > bash.bashrc
		  
