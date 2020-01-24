#program or script pretending to be browser
import socket
import urllib.request

#making a small web browser problem without using urllib
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org",80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data)<1):
        break
    print(data.decode())



#making a small web browser problem with using urllib
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhandle:
    words = line.decode().strip().split()
    for word in words:
        count[word] = count.get(word,0) + 1

print(count)

#get html document
fhandle = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in fhandle:
    print(line)



