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
#sudoku2DIMACS(4,sudoku, "Exaples/sudoku_mali.txt")
#sudoku2DIMACS(9, [(0,3,7),(0,8,2),(1,3,6),(1,4,4),(1,5,3),(1,8,0),(2,1,4),(2,2,5),(2,6,8),(2,7,7),(3,5,2),(3,6,7),(3,7,8),(5,1,2),(5,2,6),(5,3,1),(6,1,5),(6,2,7),(6,6,4),(6,7,0,),(7,0,0),(7,2,1),(7,4,7),(7,5,6),(8,0,4),(8,5,5)],
    # "Examples/sudoku_evil.txt")
#sudoku2DIMACS(9, [(0,1,6),(1,0,3),(1,2,2),(1,5,8),(1,7,0),(2,0,4),(2,3,2),(2,4,7),(2,8,3),(3,1,7),(3,5,1),(4,1,3),(4,2,0),(4,6,6),(4,7,1),(5,3,7),(5,7,5),(6,0,6),(6,4,4),(6,5,3),(6,8,1),(7,1,0),(7,3,5),(7,5,3),(7,8,8),(8,7,2)],
    # "Examples/sudoku_hard2.txt")