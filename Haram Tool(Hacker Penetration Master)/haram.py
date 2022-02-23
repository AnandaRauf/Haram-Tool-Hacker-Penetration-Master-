import os
import pyfiglet
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
print("--------------------------------------------------------------------------\n")

programname= "Haram Tool"
version= "Version 1.0.0"
devby="Developed by Ananda Rauf Maududi"
devdate= "Developed date 23 February"
print(programname)
print(version)
print(devby)
print(devdate)
print("--------------------------------------------------------------------------\n")


pathsound= "E:/Punya Rauf/Folder project Visual Studio dan Xampp/Haram Tool(Hacker Penetration Master)/"
playsound(pathsound+'soundopening.mp3')
playsound(pathsound+'welcomeback.mp3')


text = input("Nickname Hacker:")
art_img = pyfiglet.figlet_format(text)
print(art_img)

class MenuHaramTool():
    def menu():
        print("Menu Haram Tool:")
        print
        print("1.SQL Injection Manual")
        print("2.SQLMap")
        print("3.Xss")
        print("4.Clickjacking")
        print("5.DDOS")
        print("6.DNS Poisoning")
        print("7.Email Spammer")
        print("8.Call Spammer")
        print("9.Create Backdoor File")
        print("10.Spy Smartphone")
        print("11.Spy PC")
        print("12.Ransomware")
          

class SQLInMan():
    def sqlman():
        print("You're choose SQL Injection Manual\n")
        opendriver = webdriver.Chrome('webdriver/chromedriver.exe')
        openbrowser = opendriver
        filetarget = open('target.txt')
        readfiletarget = filetarget.readlines()
        target = readfiletarget[0]
        checkvulfile = open('checkvuln.txt')
        readvuln = checkvulnfile.readlines()
        checkvuln = readvuln[0]
        openbrowser.get(target+checkvuln)
        sql_order_by_file = open('orderby.txt')
        read_order_by = sql_order_by_file.readlines()
        excute_order_by = read_order_by[0]
        openbrowser.get(target+checkvuln+excute_order_by)
        
class SQLMap():
    def sqlmap(self):
        print("You're choose SQLMap\n")
        os.system("CloneSqlMap.bat")
        print("Successfull cloning SQLMap to your folder\n")
        print("SQLMap loading........\n")
        os.system("ExcuteSQLMap.bat")

class XSSAtck():
    def xssatck(self):
        print("You're choose Xss Attack\n")
        print("Comingsoon\n")

class ClickJacking():
    def clickjack():
        print("You're choose Clickjacking Attack\n")
        print("Comingsoon\n")

class DDOSS():
    def ddos(self):
        print("You're choose Ddos Attack\n")
        print("Comingsoon\n")

class DNSPo():
    def dnspo(self):
        print("You're choose DNS Poisoning Attack\n")
        print("Comingsoon\n")

class EmSpam():
    def emspam(self):
        print("You're choose Email Spammer Attack\n")
        print("Comingsoon\n")

class CalSpam():
    def calspam(self):
        print("You're choose Call Spammer Attack\n")
        print("Comingsoon\n")

class CreBaFile():
    def crebafile(self):
        print("You're choose Create Backdoor File\n")
        print("Comingsoon\n")

class SpySm():
    def spysm(self):
        print("You're choose Spy Smartphone Attack\n")
        print("Comingsoon\n")

class SpyPc():
    def spypc(self):
        print("You're choose Spy PC Attack\n")
        print("Comingsoon\n")

class Ransom():
    def ransom(self):
        print("You're choose Create Ransomware\n")
        print("Comingsoon\n")
        
        
MenuHaramTool.menu()

choose= int(input("Please,choose number on menu:"))
SQLIM = SQLInMan()
SQLMP = SQLMap()
XSSAT= XSSAtck()
CLCKJ = ClickJacking()
DDOSSS = DDOSS()
DNSPO = DNSPo()
EMAS = EmSpam()
CALSS =  CalSpam()
BACKF = CreBaFile()
SPYSMP = SpySm()
SPYPC = SpyPc()
RANSOM = Ransom()

if choose== 1:
        SQLIM.sqlmal()
elif choose==2:
        SQLMP.sqlmap()
elif choose==3:
        XSSAT.xssatck()
elif choose==4:
    CLICKJ.clickjack()
elif choose==5:
        DDOSSS.ddos()
elif choose==6:
        DNSPO.dnspo()
elif choose==7:
        EMAS.emspam()
elif choose==8:
        CALSS.calspam()
elif choose==9:
        BACKF.crebafile()
elif choose==10:
        SPYSMP.spysm()
elif choose==11:
    SPYPC.spypc()
elif choose==12:
        RANSOM.ransom()
else:
    print("Number not found on menu\n")
    print("Please try again\n")

MenuHaramTool.menu()
choose= int(input("Please,choose number on menu:"))
