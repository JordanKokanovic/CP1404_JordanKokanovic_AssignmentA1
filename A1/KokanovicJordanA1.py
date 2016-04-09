"""CP1404 Assignment 1 - 2016
   Items for hire
   Jordan Kokanovic
https://github.com/JordanKokanovic/CP1404_JordanKokanovic_AssignmentA1
Pseudocode
load .CSV
listOfLists = []
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
           print(inside_list)
           returnItem= input(Enter the number of an item to return)
           while line is not returnItem:
           next option
           else print(item returned)
        else print goodbye message

function loadingItems():
for line in items.csv
    split lines
    append lines to inside_list
    print inside_list
Return Function

function hireItems():
print(inside_list)
hire= input(Enter the number of an item to hire)
while line is not hire:
  next option
  else print(Item hired for $0.00)
  Return Function
"""
items_file = open('items.csv','r')
listOfLists = []

menu = "\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"


def main():
    print("Welcome to Items for Hire.\nCreated by Jordan Kokanovic")

    print(menu)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "L":
            loadingItems()

        elif option == "H":
            hiringItems()
        elif option == "A":
            print()
        else:
            print("Invalid Input")
        print(menu)
        option = input(">>>").upper()

    print("Thanks for using Items for Hire")

def loadingItems():
    for line in items_file:
        inside_list = [elt.strip() for elt in line.split(',')]
        listOfLists.append(inside_list)
        print(inside_list)
    return loadingItems()

def hiringItems():
    return hiringItems()




main()


