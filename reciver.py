import socket
#try:

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = '192.168.100.10'
post = 8000
target = (ip_address,post)
s.bind(target)
while True:
    message = s.recvfrom(120)
    data = message[0]
    # data = "\n"   
    # print(data.encode('ascii'))
#except Exception as e:
    #print("hello sir mene msg recive kar liya hai")
#else:
    #print("hello sir mene msg recive ni kiya hai")           
