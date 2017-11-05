def sudoku2DIMACS(N,zacetne):
    #N = velikost sudokuja
    #zacetne so podane v tuplih (vrstica, stolpec, vpisana stevilka)
    slovar = {}
    seznamVrstic = []
    for i in range(N): #vrstica
        for j in range(N): #stolpec
            for k in range(N): #stevilka
                slovar[(i,j,k)]=len(slovar)+1

    for element in zacetne:  #zacetne morajo biti res
        vrstica = "{} 0\n".format(slovar[element])
        seznamVrstic.append(vrstica)

    for i in range(N): #v nobenem kvadratku nista obe stevili hkrati
        for j in range(N):
            for k in range(N):
                for kk in range(k+1, N):
                    vrstica = "-{0} -{1} 0\n".format(slovar[(i,j,k)], slovar[(i,j,kk)])
                    seznamVrstic.append(vrstica)

            vrstica = "0\n"
            for k in range(N): #v vsaki vrstici število vsaj enkrat
                vrstica= "{} ".format(slovar[i,k,j])
            seznamVrstic.append(vrstica)

            for k in range(N):
                vrstica = "{} ".format(slovar[k, i, j])
            seznamVrstic.append(vrstica)

            velikost malega=int(sqrt(N))
            #TODO mali kvadrati
