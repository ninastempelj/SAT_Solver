from boolean import *
import operator

def readDimacs(input):
    file = open(input, 'r')
    formulaAsList = []
    dictFrequency = {}

    for line in file:
        first_sign = line[0]
        if first_sign == "p" or first_sign == "c":
            pass
        else:
            listOfVariables = []
            listOfNumbers = list(map(int, line.strip().split(" ")))  ## Vrne seznam števil
            listOfNumbers.remove(0) ##Odstrani ničlo na koncu
            for number in listOfNumbers:
                if number > 0:
                    listOfVariables.append(Variable(number))
                    if number in dictFrequency:# Lahko nardiva tut samo en if, zarad lepše kode, ne nujno bolšega časa
                        dictFrequency[number] += 1
                    else:
                        dictFrequency[number] = 1
                else:
                    number2 = abs(number)
                    listOfVariables.append(Not(Variable(number2)))
                    if number2 in dictFrequency:
                        dictFrequency[number2] += 1
                    else:
                        dictFrequency[number2] = 1
            formulaAsList.append(Or(*(tuple(listOfVariables))))
    formula = And(*(tuple(formulaAsList)))
    tupleFrequency = sorted(dictFrequency.items(), key=operator.itemgetter(1), reverse=True) #Vrne seznam tuplov(spremenljivka, število ponovitev) od najpogostejših pada
    listFrequency = [x for (x,y) in tupleFrequency]
    #print(dictFrequency) #TODO nej returna namesto printa
    print(listFrequency) ##TODO return namesto printa
    file.close()
    return formula


##Test
readDimacs("Examples/sudoku_easy.txt")
