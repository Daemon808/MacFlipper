#!/usr/bin/env python3
import subprocess

subprocess.call("ifconfig en0 down", shell=True)
subprocess.call("ifconfig en0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig en0 up", shell=True)
