
myList = [5, 4, 3, 4, 2, 1, 5, 3, 6, 7, 2]

x = 0
print(myList)


while myList[x] > myList[x+1]:
    myList[x], myList[x+1] = myList[x+1], myList[x]
    print(myList)
    if x != 0:
        if myList[x-1] > myList[x]:
            myList[x-1], myList[x] = myList[x], myList[x-1]
            print(myList)
