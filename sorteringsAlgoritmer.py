import random, copy


def insertionSortNyTest(item):
    for x in range(len(item)):
        while x > 0 and item[x-1] > item[x]:
            item[x-1], item[x] = item[x], item[x-1]
            x = x-1
    return item

def bubbleSort(item):
    for x in range(len(item)):
        for i in range(1,len(item)-x):
            if item[i-1] > item[i]:
                item[i-1], item[i] = item[i], item[i-1]
    return item

def selectionSort(item):
    for bog in range(len(item)):
        mindst = bog
        for search in range(bog, len(item)):
            if item[mindst] > item[search]:
                mindst = search
        item[bog],item[mindst] = item[mindst], item[bog]
    return item

def mergeSort(item):
    split = len(item)//2
    splitLow = item[:split]
    splitHigh = item[split:]

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




if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSortNyTest(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
