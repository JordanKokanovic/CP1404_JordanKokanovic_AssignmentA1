"""CP1404 Assignment 1 - 2016
   Items for hire
   Jordan Kokanovic

Pseudocode
load .CSV

function main()

 get users name
 display welcome message
 display menu
  get option
  while option is not q
        if option is l
           call listItems()
        if option is h
           call hireItems()
        if option id r
           call returnItems()
        else print goodbye message

function listitems()
"""

menu = "\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"
test = "Dis test"

def main():
    print("Welcome to Items for Hire.\nCreated by Jordan Kokanovic")

    print(menu)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            listitems()
        elif option == "H":
            print(test)
        elif option == "A":
            print(test)
        else:
            print("Invalid Input")
        print(menu)
        option = input(">>>").upper()

    print("Thanks for using Items for Hire")


def listitems():




 listitems()


main()







