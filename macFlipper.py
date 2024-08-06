#!/usr/bin/env python3

import subprocess
import optparse

def getArguments():
    parser = optparse.OptionParser()
    parser.add("-i","--interface",dest="interface",help="Interface to changer MAC address")
    parser.add("-m","--mac",dest="newMacAddress" ,help="New MAC Address")
    (option, arguments) = parser.parse_args()
    if not parser.interface:
        parser.error("Please specify interface, use --help for more information")
    elif not parser.newMacAddress:
            parser.error("Please specify MAC address, use --help for more information")
    return option

def SetNewAddressMac(interface, NewMacAddres):
    print("Changing MAC address for " + interface + " to " + NewMacAddres)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " +  NewMacAddres, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

option = getArguments()
SetNewAddressMac(option.interface,option.newMacAddress)