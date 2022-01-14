myList = [1, 2, 3, 4, 5, 7, 6]

def insertionSort(item): # Vi definere funktionen og modtager en værdien item som er listen.
    for x in range(len(item)): # Vi laver en for løkke for hvor x indeholder hver værdi i længden af listen
        while x > 0 and item[x-1] > item[x]: # Så laver vi en while løkke som gør at så længe x er størrer end 0 pg listens værdi af x - 1 er størrer end x så gør vi følgende
            item[x-1], item[x] = item[x], item[x-1] # så bytter vi om på listens værdier af x-1 og x
            x = x-1 # og så sætter vi x's værdi til at være x - 1
    return item # og så retunere vi listen

print(insertionSort(myList))
