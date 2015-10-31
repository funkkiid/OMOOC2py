# -*- coding: utf-8 -*-

import socket  #for sockets
import sys # for eit

# create dgram udp socket
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host='localhost';
port = 1234;

print '哥哥，我是你的日记。'
print '你今天有什么想和我分享的吗？'
print '你也可以按"回车键"来阅读我。'
while(1):
	msg=raw_input('>>')

	if msg=='':
		diaryFile = open('diary.txt')
		diary = diaryFile.read()
		print('============日记============')
		print(diary)
		sys.exit()

	if msg=='q':
		print('谢谢你和我分享这些。')
		print('再见。我会想你的。')
		sys.exit()

	try:
		# Set the whole string
		s.sendto(msg,(host,port))

		# receive data from client(data, addr)
		d=s.recvfrom(1024)
		reply=d[0]
		addr=d[1]

		print 'Server reply: '+reply

	except socket.error , msg:
		print 'Error Code: '+str(msg[0])+' Message '+ msg[1]
		sys.exit()

