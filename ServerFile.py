# Import relevant modules
import socket, threading, os

# Define the function to allow socket connections
def Main ():
    host = '0.0.0.0'
    port = 5000 # Port to be used for the connection
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)

    print("Server Started") # When Server is listening, display this text
    while True:
        c, addr = s.accept()
        print("client connected IP:< "+ str(addr) + " >") # Prints IP Address of connected client
        t = threading.Thread(target= retreiveFile, args=("retrthread",c))
        t.start()
    s.close() # Close Socket

if __name__=='__main__':
    Main()
