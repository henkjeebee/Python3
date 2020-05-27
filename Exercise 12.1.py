import socket

#Get url and extract hostname
url = input("Please enter a url: ")
host = url.split("/")
host = host[2]

#Open socket and GET url
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'

#Send the UTF-8 encoded data
cmd = cmd.encode()
mysock.send(cmd)

#Loop to parse content from page
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()