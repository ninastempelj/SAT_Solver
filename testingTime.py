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
    print ("fertik")

#Test
testirej("Grafi/graf4.txt", "Grafi/rezultati_testiranj.txt",1)
