import socket

#Constant Variables
HEADER = 128
PORT = 9883
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE='---Disconnected'

#Creates the client socket and sends a conenction request to the server
client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_soc.connect(ADDR)

#Sends a message to the server
def send(msg):
  message = msg.encode(FORMAT)
  msgLength = len(message)
  msgPadding = str(msgLength).encode(FORMAT)
  msgPadding += b' '* (HEADER-len(msgPadding))
  client_soc.send(msgPadding)
  client_soc.send(message)

#Converts epoch time
def convert_time(time):
    time = float(time)
    hour = (time % (3600*24)) / 3600
    minute = hour%1 * 60
    seconds = minute%1 * 60
    return "%02d:%02d:%02d" %(hour,minute,seconds)

print(f"What is the time?")
#Requirement 2
send("What is the time?")
#Receives the message from server
recdMsg = client_soc.recv(1024).decode(FORMAT)

#Requirement 4
print(convert_time(recdMsg))

#Disconnect from the server
send(DISCONNECT_MESSAGE)