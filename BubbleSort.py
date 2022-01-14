myList = [3, 2, 3, 5, 5, 4, 1]



def bubbleSort(item): # Vi definere funktionen og modtager en værdien item som er listen.
    for x in range(len(item)): # vi laver en for løkke hvor x indeholder lægnden af listen som værdier eks.

        for i in range(1,len(item)-x): # vi laver så endnu en for løkke hvor i indeholder længden af listen som værdier hvor den starter ved værdi 1 og trækker x fra hver gang i listens længde
            if item[i-1] > item[i]: # hvis listens værdi er størrer end værdien foran den gør vi følgende
                item[i-1], item[i] = item[i], item[i-1] # Så bytter vi på de 2 værdiers plads i listen
    return item     # så retunere vi den sorterede liste

print(bubbleSort(myList)) #
