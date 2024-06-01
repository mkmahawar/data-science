
# port limit 0 to 6553
# ip_address: 192.168.100.10
# ip_address: 192.168.56.1
# post = 8888

import socket
try:

    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address = '192.168.100.10'
    post = 8080
    target = (ip_address,post)
    message = input("kya msg kroge")
    encript_message = message.encode('ascii')
    s.sendto(encript_message,target)
except Exception as e:
    print("no need ")