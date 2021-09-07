import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(("127.0.0.1",5000))
s.listen(5)
conn,addr=s.accept()
print(addr)
print()
conn.send(b"Hey this is server")
print(conn.recv(1024))
