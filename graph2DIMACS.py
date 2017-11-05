def graphCoulouring2DIMACS(G,k, izhodna):
    seznamVrstic = []
    
    slovar = {}
    for i in range(len(G)):
        vrstica = "0"
        for j in range(k):
            if not((i,j) in slovar):
                slovar[(i,j)]=len(slovar)+1
            vrstica = "{} ".format(slovar[(i,j)]) + vrstica
        seznamVrstic.append(vrstica+"\n")
        for j in range(k):
            for jj in range(j+1,k):
                vrstica = "-{0} -{1} ".format(slovar[(i,j)],slovar[(i,jj)]) + "0"
                seznamVrstic.append(vrstica+"\n")
        for ii in G[i]:
            for j in range(k):
                if not((ii,j) in slovar):
                    slovar[(ii,j)]=len(slovar)+1
                vrstica = "-{0} -{1} ".format(slovar[(i,j)],slovar[(ii,j)]) + "0"
                seznamVrstic.append(vrstica+"\n")
    numbVariables = len(slovar)
    numbTerms = len(seznamVrstic)
    file = open(izhodna, "w")
    file.write("c Graph Colouring to DIMACS\n")
    file.write("p cnf {0} {1}\n".format(numbVariables, numbTerms))
    for vrstica in seznamVrstic:
        file.write(vrstica)
    file.close()

##Test:
##graf=[[1,3],[0,2,3],[1,4],[0,1,4],[2,3]]
##graphCoulouring2DIMACS(graf,3, "graf.txt")