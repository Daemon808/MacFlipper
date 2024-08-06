#!/usr/bin/env python3

import subprocess

interface = input("Saisre une interface : ")
NewMacAddres=input("Saisire une nouvelle addresse MAC : ")

def SetNewAddressMac(interface, NewMacAddres):
    print("Changing MAC address for " + interface + " to " + NewMacAddres)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " +  NewMacAddres, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

SetNewAddressMac(interface,NewMacAddres)