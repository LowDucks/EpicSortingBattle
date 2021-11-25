myList = [1, 2, 3, 4, 5, 7, 6]

def insertionSort(item):
    for round in range(len(item)):
        x = round

        while x > 0:
            if item[x-1] > item[x]:
                item[x-1], item[x] = item[x], item[x-1]
                #print(myList)
            x = x-1
    return item



insertionSort(myList)
