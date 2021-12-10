myList = [4, 3, 3, 2, 5, 7, 5, 3, 2, 6, 8, 9, 6, 5, 4, 4]


def mergeSort(item):

    if len(item) > 2:

        split = len(item)//2
        splitLow = item[:split] # List Comprehension
        splitHigh = item[split:] # List comprehension
        print(splitLow, splitHigh)

        mergeSort(splitLow)

        mergeSort(splitHigh)

    return item


print(mergeSort(myList))
