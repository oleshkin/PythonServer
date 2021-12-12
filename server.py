#!/usr/bin/env python3

import socket
from sshkeyboard import listen_keyboard

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        print("\nType in a msg to stream to connected clients, press [esc] to end:")
        def press(key):
            
            print(f"'{key}' was pressed")
            conn.sendall(key.encode()) #.encode() is using utf8
        
        listen_keyboard(
            on_press=press,
            until="esc",
        )


