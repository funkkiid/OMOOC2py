# -*- coding: utf-8 -*-
from datetime import datetime

import socket
import sys

HOST = '' # Symbolic name meaning all available interfaces
PORT = 1234 # Arbitary non-privileged port

# Datagram(udp) socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print '创建中...'
except socket.error, msg:
    print 'Failed to create socket. Error Code : '+str(msg[0])+' Message ' +msg[1]
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST,PORT))
except socket.error, msg:
    print 'Bind failed. Error Code: '+str(msg[0])+' Message '+msg[1]
    sys.exit()

print 'Socket bind complete'

#now keep taling with the client
while 1:
    # receive data from client(data, addr)
    d=s.recvfrom(1024)
    data=d[0]
    addr=d[1]

    if not data:
        break

    today=datetime.now()
    diary=data.strip()
    print diary
 
    diaryFile = open('diary.txt','a')
    diaryFile.write('\n'+today.strftime("%y/%m/%d")+' client['+str(addr[1])+'] '+ diary)
    diaryFile.close()
    diaryFile = open('diary.txt')
    diary = diaryFile.read()
    print('============日记============')
    print(diary)
    
    reply='帮你记录下来啦。日记：'+data
    s.sendto(reply,addr)    

s.close()

