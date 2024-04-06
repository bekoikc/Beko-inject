import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def nmap():
    print(Fore.GREEN + """

-----------------------------------------------------

              Welcome to BEKO Nmap

-----------------------------------------------------

          1-        NMAP Search
          2-        -sC -sV
          3-        DDos Attack
          4-        Basic Port Scan
          5-        Advanced Port Scan
          6-        -sV (Port Version Scan)
          7-        TCP SYN Port Scan
          8-        UDP Port Scan
          9-        TCP ACK Port Scan
          10-       TCP Window Port Scan
          11-       TCP Maimon Port Scan
          12-       Scan Port Range
          13-       Specific Port Scan
          14-       Scan IP a txt file

-----------------------------------------------------


        """)

    processNo = input(Fore.GREEN + "Number: ")
    ip = input(Fore.GREEN + "IP or URL: ")

    if (processNo == "1"):
        os.system("nmap " + ip)
    elif (processNo == "2"):
        os.system("nmap -sC -sV " + ip)
    elif (processNo == "3"):
        os.system("nmap " + ip + " -max-parallelism 10000 -Pn --script http-slowloris --script-args http-slowloris.run forever=True")
    elif (processNo == "4"):
        sTbasicport = input("enter url: ")
        os.system("nmap -sT -v " + sTbasicport)
    elif (processNo == "5"):
        os.system("nmap -p- " + ip)
    elif (processNo == "6"):
        os.system("nmap -sV " + ip)
    elif (processNo == "7"):
        os.system("nmap -sS " + ip)
    elif (processNo == "8"):
        os.system("nmap -sU " + ip)
    elif (processNo == "9"):
        os.system("nmap -sA " + ip)
    elif (processNo == "10"):
        os.system("nmap -sW " + ip)
    elif (processNo == "11"):
        os.system("nmap -sM " + ip)
    elif (processNo == "12"):
        firstport = input("First Port: ")
        secondport = input("Second Port: ")
        os.system("nmap -p "+firstport+"-"+secondport)
    elif (processNo == "13"):
        port13 = input("Enter Port: ")
        os.system("nmap -p " + port13 + " " + ip)
    elif (processNo == "14"):
        dosyakonumu14 = input("(should be in this folder) Enter file name: ")
        os.system("nmap -iL "+dosyakonumu14)

def sqlmap():
    print(Fore.GREEN + """

    -----------------------------------------------------

                  Welcome to BEKO SqlMap

    -----------------------------------------------------

              1-        Show Database
              2-        Table
              3-        Table and Users

    -----------------------------------------------------


            """)
    processNo = input("Number: ")
    parameter = input("Parameter: ")
    os.system("sqlmap -u " + parameter)
    print(Fore.RED+"Wait a min...")
    time.sleep(2)

    if (processNo == "1"):
        os.system("sqlmap -u " + parameter + " --dbs")

    if (processNo == "tablo"):
        tablo1 = input("Enter Table Name: ")
        os.system("sqlmap -u " + parameter + " -T " + tablo1)

    if (processNo == "tablo & Users"):
        tablo2 = input(Fore.CYAN+"Enter Table: ")
        user1 = input(Fore.CYAN+"Enter User: ")
        os.system("sqlmap -u " + parameter + " -T " + tablo2 + "-U " + user1)

def reconcobra():
    print(Fore.GREEN + """

    -----------------------------------------------------

                  Welcome to BEKO REDHAWK

    -----------------------------------------------------

              1-       Take İnfo 
              2-       Censys Database Search
              3-       DNS Brute Force Attack

    -----------------------------------------------------


            """)

    number = input("Number: ")
    rurl = input("Enter URL: ")

    if (number == "1"):
        os.system("perl ReconCobra.pl -t "+rurl)
    if (number == "2"):
        os.system("python censys.py -d "+rurl)
    if (number == "3"):
        os.system("bash dnsbrute.sh -d "+rurl)



def main():
    print(Fore.GREEN + """
---------------------------------------------------------

                   WELCOME THE BEKO

---------------------------------------------------------

                   1- NMAP
                   2- SQLMAP
                   3- RECON COBRA

----------------------------------------------------------

    """)

    menuno = input(Fore.GREEN + "Number: ")

    if menuno == "1":
        nmap()
    if menuno == "2":
        sqlmap()
    if menuno == "3":
        reconcobra()

main()