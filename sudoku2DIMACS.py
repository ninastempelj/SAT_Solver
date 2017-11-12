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
    print("naredu sudoku")


#test
#sudoku = [(0,0,0),(0,2,1),(1,1,1),(2,2,2),(3,3,3)]
#sudoku2DIMACS(4,sudoku, "Examples/sudoku_mali_boljsi.txt")
# sudoku2DIMACS(9, [(0,3,7),(0,8,2),(1,3,6),(1,4,4),(1,5,3),(1,8,0),(2,1,4),(2,2,5),(2,6,8),(2,7,7),(3,5,2),(3,6,7),(3,7,8),(5,1,2),(5,2,6),(5,3,1),(6,1,5),(6,2,7),(6,6,4),(6,7,0,),(7,0,0),(7,2,1),(7,4,7),(7,5,6),(8,0,4),(8,5,5)],
#     "Examples/sudoku_evil2.txt")
# sudoku2DIMACS(9, [(0,1,6),(1,0,3),(1,2,2),(1,5,8),(1,7,0),(2,0,4),(2,3,2),(2,4,7),(2,8,3),(3,1,7),(3,5,1),(4,1,3),(4,2,0),(4,6,6),(4,7,1),(5,3,7),(5,7,5),(6,0,6),(6,4,4),(6,5,3),(6,8,1),(7,1,0),(7,3,5),(7,5,3),(7,8,8),(8,7,2)],
#     "Examples/sudoku_hard22.txt")

#sudoku2DIMACS(9, [(0,1,0),(0,3,1),(0,6,3),(0,8,4),(1,1,2),(1,2,6),(1,6,7),(2,1,4),(2,3,5),(2,4,6),(2,8,1),(3,0,0),(3,1,7),(3,2,3),(3,3,6),(3,4,4),(3,6,5),(3,7,1),(5,1,5),(5,2,1),(5,4,0),(5,5,2),(5,6,6),(5,7,3),(5,8,8),(6,0,8),(6,4,7),(6,5,6),(6,7,2),(7,2,0),(7,6,1),(7,7,4),(8,0,2),(8,2,4),(8,5,5),(8,7,7)],
              #"Examples/sudoku_easy2.txt")#
sudoku2DIMACS(16,[(0,0,8),(0,3,7),(0,5,1),(0,6,2),(0,9,12),(0,10,0),(0,12,5),(0,15,11),
                  (1,0,3),(1,1,9),(1,3,10), (1,4,11),(1,7,14),(1,8,8),(1,11,13),(1,12,2),(1,14,7),(1,15,12),
                  (2,0,15),(2,1,11),(2,3,5),(2,4,9),(2,7,6),(2,8,2),(2,11,4),(2,12,1),(2,14,0),(2,15,8),
                  (3,1,1),(3,2,2),(3,13,4),(3,14,9),
                  (4,2,11),(4,3,14),(4,6,1),(4,7,0),(4,8,13),(4,9,7),(4,12,9),(4,13,8),
                  (5,3,12),(5,4,6),(5,6,13),(5,7,15),(5,8,9),(5,9,0),(5,11,14),(5,12,4),
                  (6,1,7),(6,5,14),(6,10,8),(6,14,6),
                  (7,2,9),(7,3,3),(7,5,11),(7,7,4),(7,8,1),(7,10,2),(7,12,14),(7,13,0),
                  (8,2,5),(8,3,1),(8,5,8),(8,7,9),(8,8,7),(8,10,11),(8,12,6),(8,13,12),
                  (9,1,8),(9,5,12),(9,10,5),(9,14,10),
                  (10,3,4),(10,4,14),(10,6,6),(10,7,7),(10,8,0),(10,9,2),(10,11,1),(10,12,11),
                  (11,2,15),(11,3,11),(11,6,10),(11,7,1),(11,8,4),(11,9,13),(11,12,7),(11,13,14),
                  (12,1,3),(12,2,13),(12,13,11),(12,14,1),
                  (13,0,1),(13,1,5),(13,3,6),(13,4,4),(13,7,2),(13,8,10),(13,11,0),(13,12,8),(13,14,13),(13,15,7),
                  (14,0,7),(14,1,14),(14,3,15),(14,4,1),(14,7,12),(14,8,3),(14,11,11),(14,12,0),(14,14,2),(14,15,6),
                  (15,0,11),(15,3,8),(15,5,3),(15,6,15),(15,9,9),(15,10,1),(15,12,12),(15,15,10)],
              "Examples/sudoku_large.txt")