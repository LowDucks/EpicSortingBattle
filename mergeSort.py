myList = [4, 3, 3, 2, 5, 7, 5, 3, 2, 6, 8, 9, 6, 5, 4, 4]


def mergeSort(item):

    split = len(item)//2
    splitLow = item[:split] # List Comprehension
    splitHigh = item[split:] # List comprehension

    if len(splitLow) > 1:
        splitLow = mergeSort(splitLow)
    if len(splitHigh) > 1:
        splitHigh = mergeSort(splitHigh)

    nyItem = []

    while len(nyItem) < len(item):
        if len(splitLow) > 0 and len(splitHigh) > 0:
            if splitLow[0] > splitHigh[0]:
                nyItem.append(splitHigh.pop(0))
            else:
                nyItem.append(splitLow.pop(0))
        elif len(splitLow) == 0:
            nyItem.append(splitHigh.pop(0))
        else:
            nyItem.append(splitLow.pop(0))
        

    return nyItem



print(mergeSort(myList))
