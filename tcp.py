import socket

# Can you send "GET / HTTP/1.1\r\nHost: amazon.com\r\nConnection: close\r\n\r\n" to amazon.com using sockets?
# Hint: HTTP works on port 80
# Try finding quick socket guides online

import socket

HOST = "amazon.com"
PORT = 80

import socket

HOST = "amazon.com"
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    request = "GET / HTTP/1.1\r\nHost: amazon.com\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())
    
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data
    
    print(response.decode("utf-8", errors="ignore"))
