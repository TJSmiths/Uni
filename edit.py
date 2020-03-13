def Main():
    while True:
# This is what is displayed to the end user, while also asking for inputs
        myFile= input("Please enter the name of the file you wish to edit..")
        changeNum = int(input("Please enter the line you wish to change"))
        newLine = input("Please enter the new text..")
# Open and read the selected file
        f = open(myFile, 'r')
        content = f.readlines()
        f.close()
# Open and write to the selected file
        f = open(myFile, 'w')
        content[changeNum-1] = newLine + "\n"
        f.writelines(content)
# Print the new text
        for things in content:
            print ("The following text has been added to the file: " + things)

        f.close()
# Stop the script from looping and print exit message
        break
    print("File has been edited, Goodbye.")

if "__name__ == __main__":
    Main()
