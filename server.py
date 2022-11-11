from socket  import *
from constCS import * #-
import time

def check_type(data):
  if '*' in data:
    return '*'
  elif '/' in data:
    return '/'
  elif '+' in data:
    return '+'
  else:
    return None

def calc(data):
  print(f"- {data}")
  op = check_type(data)
  if not op:
    return "Missing operator ['*', '/', '+']"
  values = data.split(op)
  if len(values) > 2:
    return "Wrong format. Pattern: <number1><operator><number2> | Example: 5.2*4.1"
  if op == '*':
    return float(values[0]) * float(values[1])
  elif op == '/':
    return float(values[0]) / float(values[1])
  elif op == '+':
    return float(values[0]) + float(values[1])

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
while True:                # forever
  (conn, addr) = s.accept()  # returns new socket and addr. client 
  data = conn.recv(1024)   # receive data from client
  if not data: 
    conn.close()
    continue
  rcv_data = bytes.decode(data)
  if rcv_data == 'close': break
  result = calc(rcv_data)
  print(f" > {result}")
  conn.send(str.encode(f"{result}")) # return sent data plus an "*"
conn.close()               # close the connection





  