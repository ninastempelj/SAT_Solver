def sudoku2DIMACS(N,zacetne,izhodna):
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
                vrstica= "{} ".format(slovar[(i,k,j)])+vrstica
            seznamVrstic.append(vrstica)

            vrstica = "0\n"
            for k in range(N):
                vrstica = "{} ".format(slovar[(k, i, j)])+vrstica
            seznamVrstic.append(vrstica)

    mali=int((N) ** (1 / 2))
    for k in range(N):
        for i in range(mali):
            for j in range(mali):
                malaVrstica="0\n"
                for ii in range(mali):
                    for jj in range(mali):
                        kvadratek = (i*mali + ii,j*mali+jj,k)
                        malaVrstica = "{} ".format(slovar[kvadratek]) + malaVrstica
                seznamVrstic.append(malaVrstica)
    file = open(izhodna,"w")
    file.write("c Sudoku2DIMACS\n")
    file.write("p cnf {0} {1}\n".format(len(slovar), len(seznamVrstic)))
    for vrstica in seznamVrstic:
        file.write(vrstica)
    file.close()


#test
#sudoku = [(0,0,0),(0,2,1),(1,1,1),(2,2,2),(3,3,3)]
#slovar = sudoku2DIMACS(4,sudoku, "Exaples/testSudoku.txt")
