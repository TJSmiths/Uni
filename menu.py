
def welcomeMessage():
# Print the menu itself
    print ("""

Please enter the appropriate number:

1. Connect to server and download a file
2. Write to File
3. Quit

    """)
# Asks for input from the user
while True:
    welcomeMessage()
    selection = int(input("Please enter an option from the list: "))
# Once user has selected, cycles through and imports relevant script.
    if selection == 1:
        import Client # Imports and runs the script Client.py
        Client.Main()
    elif selection == 2:
        import edit # Imports and runs the script edit.py
        edit.Main()
    elif selection == 3:
        input ("Press the Enter key to exit") # Validates the user quitting
# Stops the Menu Looping
        break
