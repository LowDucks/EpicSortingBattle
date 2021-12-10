myList = [3, 2, 3, 5, 5, 4, 1]

def selectionSort(item):
    for bog in range(len(item)):
        mindst = bog
        for search in range(bog, len(item)):
            if item[mindst] > item[search]:
                mindst = search
        item[bog],item[mindst] = item[mindst], item[bog]
    return item

print(selectionSort(myList))
