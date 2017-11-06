def graphCoulouring2DIMACS(G, k, izhodna):
    ##G is list of lists of connections of certain vertex, k is the number of colours, izhodna will be the new DIMACS file
    seznamVrstic = []
    slovar = {}

    for i in range(len(G)):
        for j in range(k):
            slovar[(i,j)]=len(slovar)+1 #naredi slovar
    for i in range(len(G)):
        vrstica = "0"
        for j in range(k):
            vrstica = "{} ".format(slovar[(i,j)]) + vrstica
        seznamVrstic.append(vrstica+"\n")
        for j in range(k):
            for jj in range(j+1,k):
                vrstica = "-{0} -{1} ".format(slovar[(i,j)],slovar[(i,jj)]) + "0"
                seznamVrstic.append(vrstica+"\n")
        for ii in G[i]:
            for j in range(k):
                vrstica = "-{0} -{1} ".format(slovar[(i,j)],slovar[(ii,j)]) + "0"
                seznamVrstic.append(vrstica+"\n")
    seznamVrstic.append("{} 0\n".format(slovar[(0,0)])) #first vertex is first colour
    if G[0] !=[]:
        seznamVrstic.append("{} 0\n".format(slovar[(G[0][0],1)])) #first neighbour of the first vertex is second colour

    numbVariables = len(slovar)
    numbTerms = len(seznamVrstic)
    file = open(izhodna, "w")
    file.write("c Graph Colouring to DIMACS\n")
    file.write("p cnf {0} {1}\n".format(numbVariables, numbTerms))
    for vrstica in seznamVrstic:
        file.write(vrstica)
    file.close()
    #return slovar

##Test:
graf1=[[1,3],[0,2,3],[1,4],[0,1,4],[2,3]]


graf_veliki = [
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20],
    [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19],
    [0, 1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20],
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 17, 18, 19, 20],
    [0, 1, 2, 3, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18],
    [0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20],
    [1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 20],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19, 20],
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 17, 18, 19, 20],
    [0, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20],
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20],
    [0, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [6, 7, 8, 0, 1, 2], [6, 7, 8, 0, 1],
    [7,8,0,6,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71],
    [23,8,0,7,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,1],
    [23,24,0,8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,1,6],
    [23,24,25,0,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,1,6,7],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55],
    [23,24,25,26,30],
    [23,24,25,26,30],
    [23,24,25,26,30,34],
    [23,24,25,26,30,33],
    [23,24,25,26,30],
    [23,24,25,26,30],
    [23,24,25,26,30,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57],
    [23,24,25,26,30,37],
    [23,24,25,26,30,37],
    [23,24,25,26,30,37,41],
    [23,24,25,26,30,37,40],
    [23,24,25,26,30,37],
    [23,24,25,26,30,37],
    [23,24,25,26,30,37,45,46,47,48,49,50,51,52,53,54,55,56,57],
    [23,24,25,26,30,37,44],
    [23,24,25,26,30,37,44],
    [23,24,25,26,30,44,37,48,49,50,51,52,53,54,55,56,57],
    [23,24,25,26,30,47,44,37],
    [23,24,25,26,30,47,44,37],
    [23,24,25,26,30,47,44,37,51],
    [23,24,25,26,30,47,44,37,50],
    [23,24,25,26,30,47,44,37],
    [23,24,25,26,30,47,44,37],
    [23,24,25,26,47,44,37,30,55,56,57],
    [23,24,25,26,54,47,44,37,30],
    [23,24,25,26,54,47,44,37,57],
    [23,24,25,26,54,47,44,37,56],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26],
    [23,24,25,26,70],[23,24,25,26,69],
    [24,25,26,23,1,6,7,8]
    ]

graf_srednji = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [0,6,1,8,7,2],
    [0,6,8,7,1,23,24,25,26,27,30,29,28,31,32],
    [0,22,8,7,6,24,25,26,27,30,29,28,31],
    [0,23,22,8,7,25,26,27,30,29,28,31],
    [0,23,22,24,8,26,27,30,29,28,31,32,33,34,3,2,6],
    [23,22,25,24,0,27,30,29,28,31,32,33,34,3,2,6,7],
    [26,22,25,24,23,30,29,28,31],
    [26,22,25,24,23,27,31,32,33,34,3,2,6,7,8],
    [26,27,22,25,24,23],
    [26,27,22,25,24,23],
    [26,28,22,25,24,23,27],
    [26,28,25,22,33,34,3,2],
    [26,28,32,25,34,3],
    [26,28,32,33,25],
    ]

graf_zelo_povezan = [
    [1, 2, 3, 4, 5, 6, 8, 9, 15, 16, 17, 18, 19, 20],
    [0, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18],
    [0, 1, 3, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 18, 20],
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 17, 18, 20],
    [0, 1, 2, 3, 7, 8, 9, 13, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18],
    [0,  3, 5, 7, 8, 10, 12, 13, 15, 16, 17, 19, 20],
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 13, 15, 16, 19, 20],
    [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 16, 17, 19,],
    [0, 1, 2, 3, 4, 5, 10, 12, 13, 14, 15, 16, 17, 19, 20],
    [1, 6, 7, 8, 9, 13, 14, 15, 17, 19, 20],
    [1, 2, 3, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 2, 5, 6, 7, 8, 9, 11, 14, 15, 16, 17, 18, 20],
    [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 15, 16, 17, 19, 20],
    [1, 2, 3, 5, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20],
    [0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 18, 19],
    [0, 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 17, 18, 19],
    [0, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19],
    [0, 1, 2, 3, 4, 5, 11, 12, 14, 15, 16, 17, 19, 20],
    [0, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20],
    [0, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 18, 19]
    ]

#graphCoulouring2DIMACS(graf_zelo_povezan, 21, "Examples/graf1.txt")
#graphCoulouring2DIMACS(graf_veliki, 21, "Examples/graf11.txt")
#graphCoulouring2DIMACS(graf_srednji, 10, "Examples/graf111.txt")
