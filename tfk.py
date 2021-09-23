#!usr/bin/env python
# -*- coding: utf-8 -*-
 



import os

os.system("apt install figlet")
os.system("clear")
os.system("figlet TFK")

print("""

KODLAYAN:SAEPSH

1)Kur

2)Çıkış

""")

secim = input("Seçim Yapınız: ")

if(secim =="1"):
	os.system("termux-setup-storage")
	os.system("pkg install root-repo unstable-repo x11-repo -y")
	os.system("apt update -y")
	os.system("apt upgrade")
	os.system("pkg install git -y")
	os.system("pkg install python python2 -y")
	os.system("pkg intall python3")
	os.system("pkg install pip")
	os.system("apt install purge-repo -y")
	os.system("pkg install php -y")
	os.system("pkg install perl -y")
	os.system("pkg install nano -y")
	os.system("pkg install vim -y")
	os.system("pkg install cat -y")
	os.system("pkg install pip2 -y")
	os.system("pip install wordlist -y")
	os.system("pkg install nmap -y")
	os.system("pkg install hydra -y")
	os.system("pkg install openssl -y")
	os.system("apt install nodejs -y")
	os.system("clear")
elif(secim == "2"):
	os.system(" ")
	print("Program Kapatılıyor...")

else:
	print("Yanlış seçim")


tem = input("""

Ekran Temizlensin mi? [Y/n]: """)

if(tem == "y"):
	os.system("clear")

elif(tem == "n"):
	os.system("figlet Iyi Günler")

