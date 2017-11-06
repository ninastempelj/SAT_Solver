import random
from graph2DIMACS import*

def GraphGenerator(N,C, izhodna):
    #N = number of vertices, C = number of colours, Izhodna= output file (DIMACS)
    #generates a random (satisfiable) graph colouring problem
    seznam=[]
    for i in range(N):
        seznam.append([])
    for i in range(N):
        k = random.randint(2,C-3)
        for ii in range(k):
            stevilo = random.randint(0,N-1)
            if stevilo !=i:
                seznam[i].append(stevilo)
    graphCoulouring2DIMACS(seznam, C, izhodna) #itcreates a DIMACS file
    return seznam

#Test:
# GraphGenerator(38,10, "Graphs/graf.txt")


