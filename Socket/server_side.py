import socket

host = "localhost"
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print("The server is listening on port", port)
con, address = s.accept()
print("Connection has been established", str(address))
# con.send("Hello my name is Rahul, I am sending message from server".encode())
try:
    fileName = con.recv(1024)
    file = open(fileName, 'rb')
    readFile = file.read()
    con.send(readFile)
    con.close()
except:
    con.send("File Not Found on the server".encode())
