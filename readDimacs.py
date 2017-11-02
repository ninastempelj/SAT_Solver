from boolean import *

def readDimacs(input):
    file = open(input, 'r')
    formulaAsList = []

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
                else:
                    listOfVariables.append(Not(Variable(abs(number))))
            formulaAsList.append(Or(*(tuple(listOfVariables))))
    formula = And(*(tuple(formulaAsList)))
    return formula


##Test
    # readDimacs("Examples/sudoku_easy.txt")