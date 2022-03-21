import socket
import threading
import time

#Constants
HEADER = 128
PORT = 9883
HOST = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE='---Disconnected'

#Creates a server socket and binds the socket to the IP and Port
server_soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_soc.bind(ADDR)

#Establish a connection between the server and client
def create_client_conn(client_soc, addr):
  print(f"    client connection created {addr}")
  connected = True
  while(connected):
    msgLength = client_soc.recv(HEADER).decode(FORMAT)
    #Checks if client sends a message
    if msgLength:
      msgLength = int(msgLength)
      msg = client_soc.recv(msgLength).decode(FORMAT)
      print(f"msg={msg} from addr")

      #If correct message, sends the epoch time back to the client
      if msg == "What is the time?":
        return_msg = str(time.time())
        print(f"server process msg: {return_msg}")
        #Requirement 3
        client_soc.send(f"{return_msg}".encode(FORMAT))
        print("Sleeping.....")
        time.sleep(15)
      #If disconnect message, disconnects from the server
      if msg == DISCONNECT_MESSAGE:
        print("disconnect")
        client_soc.close()
        connected = False

#Starts the server
def start_server():
  #Wait for a connection request
  server_soc.listen()
  print("Server is listening on host " + HOST)
  while True:
    #Create a new connection socket for the server and the client
    client_soc, addr = server_soc.accept()
    thread = threading.Thread(target=create_client_conn, args = (client_soc, addr))
    #Create a thread for the socket
    thread.start()
    print(f"{threading.activeCount()-1} threads connection running")

#Start
start_server()