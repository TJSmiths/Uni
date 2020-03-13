# Imports relevant modules
import socket, os
# Define the destination IP Address and Port
def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    while True:
        filename = input("Filename?? - > ") # Asks for filename
        if os.path.exists('./' + filename):
            ans = input ("That file already exists - overwrite? Y/N") # If the file exist, will prompt for confirmation
            if ans in ["y"]:
                if filename != 'q':
                    s.send(filename.encode('utf-8'))
                    data = s.recv(1024).decode('utf-8')
            if data[:6] == 'EXISTS':
                filesize = int(data[6:])
                message = input("File exists, " + str(filesize) + "Bytes, download (Y/N)? -> ") # Repeats the file existing check but with filesize included
                if message in ['y']:
                    s.send('OK'.encode('utf-8'))
                    f = open(filename, 'wb')
                    data = s.recv(1024)
                    #data = data.decode('utf-8')
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = s.recv(1024).decode('utf-8')
                        totalRecv += len(data)
                        f.write(data)
                        print("{0:.2f}". format((totalRecv/float(filesize)) * 100) + "% done")
                    print (" Download Complete") # Shows the user the donwload has completed
                    f.close()
                    ans = input ("Download another file? y/n") # Asks the user if they wish to transfer another file
                    if ans in ["n"]: # If the user enters the letter 'n', the script will exit
                        break
            else:
                print ("File does not exist") # Printed if the file typed in for value 'filename' does not exist
        else:
            print ("BYE!!!") # Printed if a filename is not given
    input ("Goodbye")
    s.close() # Closes the socket

if __name__ == '__main__':
    Main()
