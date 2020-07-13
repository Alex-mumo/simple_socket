#program to create a simple server
import socket
import sys
#creating a socket object
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket object
    print("socket created successfully")
except socket.error as err:
    print("socket failed to create with error %s" %(err))

#defalut port
port = 80

#get the local machine hostname
try:
    host_ip = socket.gethostname('www.google.com')
except socket.gaierror:
    print("Error while resolving the host")
    sys.exit()

#connecting to the server
s.connect((host_ip, port))

print("Socket successfully connected to google on port == %s" %(host_ip))