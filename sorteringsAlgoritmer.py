import random, copy
"""
def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items
"""


def insertionSortGammel(item):
    for round in range(len(item)):
        x = round

        while x > 0:
            if item[x-1] > item[x]:
                item[x-1], item[x] = item[x], item[x-1]
                #print(item)
            x = x-1

    return item


def insertionSortNyTest(item):
    for round in range(len(item)):
        x = round

        while x > 0 and item[x-1] > item[x]:
            item[x-1], item[x] = item[x], item[x-1]
            #print(myList)
            x = x-1
    return item

def insertionNyIgen(item):
    for round in range(len(item)):






def insertionSortStolen(liste):
    for item in range(1, len(liste)):
        værdi = liste[item]
        j = item - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and værdi < liste[j]:
            liste[j + 1] = liste[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        liste[j + 1] = værdi
    return liste


if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionNyTest(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
