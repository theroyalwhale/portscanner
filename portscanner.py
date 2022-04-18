import pyfiglet
import sys
import socket
from colorama import init
from colorama import Fore as f
import easygui as eg
from datetime import datetime
init(autoreset=True)
eg.msgbox("Welcome to DeLevo Port Scanner!", "DeLevo Port Scanner")
while True:
    choices = ["Scan for ports", "Credits", "Exit"]
    menu = eg.buttonbox("DeLevo Port Scanner", "DeLevo Port Scanner", image="dlgportscanner.png", choices=choices)
    if menu == "Credits":
        eg.msgbox("Software and UI: WalesWorksLtd", "DeLevo Port Scanner")
    if menu == "Exit":
        sys.exit()
    if menu == "Scan for ports":
        target = eg.enterbox("Please enter the desired IP address to scan ports for.", "DeLevo Port Scanner")
        if len(sys.argv) == 2:
                target = socket.gethostbyname(sys.argv[1])
        print(f.CYAN + "-" * 50)
        print(f.CYAN + "Scanning Target: " + target)
        print(f.CYAN + "Scanning started at:" + str(datetime.now()))
        print(f.CYAN + "-" * 50)
        try:
            for port in range(1,65535):
                print(f.BLUE + "Scanning for port " + str(port))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                    print(f.GREEN + "Port {} is open".format(port))
                s.close()
        except KeyboardInterrupt:
            eg.msgbox("The software was stopped.", "DeLevo Port Scanner")
        except socket.gaierror:
            eg.msgbox("The hostname could not be resolved.", "DeLevo Port Scanner")
        except socket.error:
            eg.msgbox("The server is not responding.", "DeLevo Port Scanner")


