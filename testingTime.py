from Solver import *

def testirej(imePrimera, rezultati, steviloPonovitev):
    ime = imePrimera.split(".")[0]
    imeResitev = "{}_resitev.txt".format(ime)
    file = open(rezultati, "a")
    file.write("{}\n".format(ime))
    for i in range(steviloPonovitev):
        start_time = time.time()
        main(imePrimera, imeResitev)
        file.write("time elapsed: {:.2f}s\n".format(time.time() - start_time))
    file.close()
    #print ("Končal sem")

#Test
#testirej("Graphs/graf1.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 10)

# testirej("Examples/sudoku_easy.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/sudoku_evil2.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/sudoku_hard.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/graf1.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/graf2.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/primer2.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Examples/sudoku_large.txt","Graphs/rezultati_testiranj_WizardDobby.txt", 5)
#
testirej("testGraph.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 1)

# testirej("Graphs/graf2.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Graphs/graf3.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Graphs/graf4.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Graphs/graf5.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Graphs/graf6.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)
# testirej("Graphs/graf7.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)

#testirej("Graphs/graf8.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 10)
#testirej("Graphs/graf9.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 10)
#testirej("Graphs/graf10.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 10)
# testirej("Graphs/graf11.txt", "Graphs/rezultati_testiranj_WizardDobby.txt", 5)













