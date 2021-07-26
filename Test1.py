#_______________________________________________________#
# Assignment #3
# Dev: Andrei Arevalo
# Date: January 22nd, 2021
# ChangeLog:
# AArevalo, 1/22,2021, Initial Revision
#_______________________________________________________#

# Assignment Task: Create a program that asks the user
#   for the name of a household item, and then asks for its
#   estimated value. Store both pieces of data in a text file
#   called, HomeInventory.txt.
#_______________________________________________________#

# Open the file labeled House Inventory
objFile = open("C:\\_PythonClass1\\HouseInventory.txt", "a")
#_______________________________________________________#

# Print the welcome message for the program and specify data type
print("You'll be entering both the household item name and value:")
print("Enter 'Exit' to quit!")
#_______________________________________________________#

# Create while loop to allow user to keep adding data
while(True):
    # Create string for Item name
    Name_str   = input("Enter Item Name: ")
    
    # If the user types "Exist" here, end the program
    if(Name_str.lower() == "exit"):break

    # If the user types something else, prompt them to type the value
    else: Value_str   = input("Enter Estimated Value in Dollars: ")

    # Write the two pieces of data to the txt file with a comma
    objFile.write(Name_str + "," + Value_str + "\n")
#_______________________________________________________#
    
# If the loop is broken with "Break" close the file
objFile.close()
print("\nYour data has been stored!")
#_______________________________________________________#
















