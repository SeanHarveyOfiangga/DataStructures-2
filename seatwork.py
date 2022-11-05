# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

#Introduction and user input

def Intro():
    print("Welcome to my array program!")
Intro()

#User input
list1 = []
def User():
    for i in range(10):
        content = int(input("\nPlease enter 10 random numbers: "))
        list1.append(content)
    print(f"\nYou picked {list1}\n")
    return list1
User()

def Menu():
    print(""" *************************************************** ARRAY MENU ***************************************************
    Choose what do you want to do with your Array:
        1 -> Add an element
        2 -> Insert an element
        3 -> Modify an element
        4 -> Delete an element
        5 -> Arrange in ascending order
        6 -> Arrange in descending order""")
    global Choice
    Choice = int(input("What do you want to do: "))
    ans()



def ans():
    if  Choice == 1:
        list1.append(int(input("\nEnter the number you would like to add: ")))
        print(list1)
        ans = input("Do you wish to continue?: ")
        if ans == "YES".lower():
            Menu()
        else:
            bye()
    elif Choice == 2:
        pos = int(input("Enter where do you wish to put the number (starting from 0): "))
        newnum = int(input("Enter the number you wish to add: "))
        list1.insert(pos, newnum)
        print(list1)
        ans = input("Do you wish to continue?: ")
        if ans == "YES".lower():
            Menu()
        else:
            bye()

def bye():
    print("Thank you for using my program ^^")      

Menu()           
    