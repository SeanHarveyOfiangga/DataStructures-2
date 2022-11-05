# Sean Harvey S. Ofiangga 
# BSCOE 2-6

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
    print("\033[01m\033[30m\033[42m************************************************************Welcome to my array program!************************************************************\033[0m")
Intro()

#User input
list1 = []
def User():
    k = 11
    for i in range(10):
        k = k - 1
        content = int(input(f"\nPlease enter \033[01m\033[32m\033[04m10\033[0m random numbers ({k} more): "))
        list1.append(content)
    print(f"\n\033[01mYou picked \033[46m\033[30m{list1}\033[0m\n")
    return list1
User()

# Menu and infos
def Menu():
    print("""\033[01m\033[30m\033[43m*************************************************** ARRAY MENU ***************************************************\033[0m
    Choose what do you want to do with your \033[01mArray\033[0m:
        \033[31m1 -> Add an element\033[0m
        \033[32m2 -> Insert an element\033[0m
        \033[33m3 -> Modify an element\033[0m
        \033[34m4 -> Delete an element\033[0m
        \033[35m5 -> Arrange in ascending order\033[0m
        \033[36m6 -> Arrange in descending order\033[0m""")
    global Choice
    Choice = int(input("\033[01mWhat do you want to do: \033[0m"))
    ans()



def ans():
    # Add
    if  Choice == 1:
        list1.append(int(input("\n\033[31mEnter the number you would like to add: \033[0m")))
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".lower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue
    # Insert
    elif Choice == 2:
        pos = int(input("\033[32mEnter the index you wish to put the number (starting from 0): \033[0m"))
        newnum = int(input("\033[32mEnter the number you wish to add: \033[0m"))
        list1.insert(pos, newnum)
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".islower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue
    # Modify
    elif Choice == 3:
        index = int(input("\033[33mWhat is the index of the number you wish to modify? (Starting form 0): \033[0m"))
        list1.pop(index)
        mod = int(input("\033[33mReplace it with: \033[0m"))
        list1.insert(index, mod)
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".lower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue
    # Delete
    elif Choice == 4:
        delete = int(input("\033[34mWhat is number you wish to delete?: \033[0m"))
        list1.remove(delete)
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".lower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue
    # Ascending
    elif Choice == 5:
        list1.sort()
        print(list1)
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".lower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue
    # Descending
    elif Choice == 6:
        list1.sort(reverse=True)
        print(list1)
        print(f"\033[46m\033[30m{list1}\033[0m")
        while True: 
            ans = input("\n\033[33mDo you wish to continue?: \033[0m")
            if ans == "YES".lower():
                Menu()
            elif ans == "NO".lower():
                bye()
            else:
                print("\033[01m\033[31mI don't understand\033[0m")
                continue

# Outro
def bye():
    print("\n\033[30m\033[01m\033[45mThank you for using my program ^^\033[0m")  
    exit()    

Menu()               