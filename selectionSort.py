myList = [3, 2, 3, 5, 5, 4, 1]

def selectionSort(item): # Vi definere funktionen og modtager en værdien item som er listen.
    for bog in range(len(item)): # Vi laver en for løkke for bog som indeholder hver værdi der er i længden af listen
        mindst = bog # Vi gemmer bog i en ekstra variabel til senere
        for search in range(bog, len(item)): # vi laver en for løkke hvor search indehold hver værdi i længden fra bog til længden af listen
            if item[mindst] > item[search]: # Hvis listen værdi mindst er størrer en listens værdi search så gør vi følgende
                mindst = search # Vi gemmer search værdien i en ny variabel mindst
            item[bog],item[mindst] = item[mindst], item[bog] # Så bytter vi om på de to værdier i listen bog og mindst hvor mindst kommer enten til at være bog eller search
    return item # så retunere vi listen

print(selectionSort(myList))
