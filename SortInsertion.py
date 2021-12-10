myList = [1, 2, 3, 4, 5, 7, 6]

def insertionSort(item):
    for x in range(len(item)):
        while x > 0 and item[x-1] > item[x]:
            item[x-1], item[x] = item[x], item[x-1]
            x = x-1
    return item

print(insertionSort(myList))
