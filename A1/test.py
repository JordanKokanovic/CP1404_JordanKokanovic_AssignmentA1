items_file = open('items.csv', 'r')
itemLines = items_file.readlines()
for line in itemLines:
    type = [line.strip().split(',')]
    itemsList = type[0]

    #print(len(itemName))
    #print(itemsList[0:4])
    print('1- {}, {}, ${}, {}'.format(itemsList[0], itemsList[1], itemsList[2], itemsList[3]))

'''
listsOfList.append(itemLines[0])
listsOfList.append(itemLines[1])
listsOfList.append(itemLines[2])
listsOfList.append(itemLines[3])
listsOfList.append(itemLines[4])
'''