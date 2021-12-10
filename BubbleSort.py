myList = [3, 2, 3, 5, 5, 4, 1]

def bubbleSort(item):
    for x in range(len(item)):
        for i in range(1,len(item)-x):
            if item[i-1] > item[i]:
                item[i-1], item[i] = item[i], item[i-1]
    return item

print(bubbleSort(myList))
