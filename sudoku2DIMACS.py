def sudoku2DIMACS(N,zacetne,izhodna):
    #N is size of sudoku,
    # zacetne is list of tuples(i,j,k) (i=row, j=column, k =number) that show the starting state
    #izhodna will be the new DIMACS file
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
            vrsticaVrsta = "0\n"
            vrsticaStolpec = "0\n"
            vrsticaKvadrat = "0\n"

            for k in range(N):

                #V vsaki vrstici/stolpcu/kvadratku ne sme biti isto število dvakrat
                for kk in range(k+1, N):
                    vrsticaKvadrat1 = "-{0} -{1} 0\n".format(slovar[(i,j,k)], slovar[(i,j,kk)])#v nobenem kvadratku nista obe stevili hkrati
                    seznamVrstic.append(vrsticaKvadrat1)
                    vrsticaVrsta1 = "-{0} -{1} 0\n".format(slovar[(i,k,j)], slovar[(i,kk,j)])
                    seznamVrstic.append(vrsticaVrsta1)
                    vrsticaStolpec1 = "-{0} -{1} 0\n".format(slovar[(k,j,i)], slovar[(kk,j,i)])
                    seznamVrstic.append(vrsticaStolpec1)

                #V vsaki vrstici/stolpcu/kvadratku more biti vsaj eno število:
                vrsticaVrsta = "{} ".format(slovar[(i,k,j)])+vrsticaVrsta #v vsaki vrstici število vsaj enkrat
                vrsticaStolpec = "{} ".format(slovar[(k,i,j)])+vrsticaStolpec
                vrsticaKvadrat = "{} ".format(slovar[(i, j, k)]) + vrsticaKvadrat

            seznamVrstic.append(vrsticaVrsta)
            seznamVrstic.append(vrsticaStolpec)
            seznamVrstic.append(vrsticaKvadrat)


    mali=int((N) ** (1 / 2))
    for k in range(N):
        for i in range(mali):
            for j in range(mali):
                malaVrstica="0\n"
                for ii in range(mali):
                    for jj in range(mali):
                        #V vsakem malem kvadratu mora biti vsaj eno število
                        kvadratek = (i*mali + ii,j*mali+jj,k)
                        malaVrstica = "{} ".format(slovar[kvadratek]) + malaVrstica

                        for iii in range(mali):
                            for jjj in range(mali):
                                if not (iii==ii and jjj==jj):
                                    kvadratek1 = (i*mali + ii, j*mali+jj,k)
                                    kvadratek2 =(i*mali + iii, j*mali+jjj,k)
                                    vrsticaMini = "-{0} -{1} 0\n".format(slovar[kvadratek1], slovar[kvadratek2])
                                    seznamVrstic.append(vrsticaMini)
                seznamVrstic.append(malaVrstica)
    file = open(izhodna,"w")
    file.write("c Sudoku2DIMACS\n")
    file.write("p cnf {0} {1}\n".format(len(slovar), len(seznamVrstic)))
    for vrstica in seznamVrstic:
        file.write(vrstica)
    file.close()


#test
#sudoku = [(0,0,0),(0,2,1),(1,1,1),(2,2,2),(3,3,3)]
#sudoku2DIMACS(4,sudoku, "Examples/sudoku_mali_boljsi.txt")
# sudoku2DIMACS(9, [(0,3,7),(0,8,2),(1,3,6),(1,4,4),(1,5,3),(1,8,0),(2,1,4),(2,2,5),(2,6,8),(2,7,7),(3,5,2),(3,6,7),(3,7,8),(5,1,2),(5,2,6),(5,3,1),(6,1,5),(6,2,7),(6,6,4),(6,7,0,),(7,0,0),(7,2,1),(7,4,7),(7,5,6),(8,0,4),(8,5,5)],
#     "Examples/sudoku_evil2.txt")
# sudoku2DIMACS(9, [(0,1,6),(1,0,3),(1,2,2),(1,5,8),(1,7,0),(2,0,4),(2,3,2),(2,4,7),(2,8,3),(3,1,7),(3,5,1),(4,1,3),(4,2,0),(4,6,6),(4,7,1),(5,3,7),(5,7,5),(6,0,6),(6,4,4),(6,5,3),(6,8,1),(7,1,0),(7,3,5),(7,5,3),(7,8,8),(8,7,2)],
#     "Examples/sudoku_hard22.txt")