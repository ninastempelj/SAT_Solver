import random
from graph2DIMACS import*

def GraphGenerator(N,C, izhodna):
    #N = number of vertices, C = number of colours (at least 5), Izhodna= output file (DIMACS)
    #generates a random graph colouring problem
    seznam=[]
    for i in range(N):
        seznam.append(set())
    for i in range(N):
        k = random.randint(2,C-3)
        for ii in range(k):
            stevilo = random.randint(0,N-1)
            if stevilo !=i:
                seznam[i].add(stevilo)
                seznam[stevilo].add(i)
    graphCoulouring2DIMACS(seznam, C, izhodna) #it creates a DIMACS file
    #print(seznam)

#Test:
GraphGenerator(29,19, "Graphs/graf1.txt")







