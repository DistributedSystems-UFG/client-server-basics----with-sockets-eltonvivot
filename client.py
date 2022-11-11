from socket  import *
from constCS import * #-
import sys

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
ipt_data = sys.argv[1].strip()  # input data
s.send(str.encode(ipt_data))  # send some data
data = s.recv(1024)     # receive the response
print (bytes.decode(data))            # print the result
s.close()               # close the connection
