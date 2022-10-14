import socket
import sys
s = socket.socket()
s2 = socket.socket()
print("Socket successfully created")
port = 42690
port1 = 50000
s.bind(("192.168.18.19", port))
print("socket bound to %s" %(port))
angle = 90.0
print("angle var is created")
s.listen(5)
print("socket is listening")
while True:
	c, addr = s.accept()
	print('Got connection from', addr)
	message = str(angle)
	c.send(message.encode("utf-8"))
	c.close()
	s.close()
	break

s2.connect(("192.168.18.19", port1))
test = True
while test:
	message = s2.recv(1024)
	if message == b'':
		print("No data passed, closing \"server\"")
		test = False
	else:
		print("data received from client", message.decode("utf-8"))
		angle = float(message.decode("utf-8"))
