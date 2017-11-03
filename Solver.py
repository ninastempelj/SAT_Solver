##########
#  DPLL algorithm:
#
# - Simplify formula
# - find unit clauses and reduce them |(on repeat)
# - Simplify formula                  |
#  - assume chosen l, repeat algorithm
# - if fail: assume ~l, repeat algorithm
######################
from boolean import *
import operator
import copy


def main(vhod, izhod):
    formula = readDimacs(vhod)
    print(dpll(formula))
    file = open(izhod,"w")
    file.write("bu")##TODO formula
    file.close()



def step12(formula):
    """ Funkcija formulo poenostavi, vrne pa True in novo formulo, če je spremembna potrebna, sicer False in staro formulo"""
    #formula.simplify()

    print(str(formula) + " Step12")
    if isinstance(formula, Variable) | len(formula.terms) == 1:
        return False, formula.simplify()
    for ali in formula.terms:
        if isinstance(ali, Variable):
            formula.simplify_by(ali)
            return True, formula.simplify()
        elif isinstance(ali, Not):
            formula.simplify_by(ali)
            return True, formula.simplify()
        elif len(ali.terms) == 1:
            for term in ali.terms:
                formula.simplify_by(term)
                return True, formula.simplify()
    return False, formula


def choose_literal(formula):
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    for term in formula.terms:
        print(term)
        if isinstance(term, Variable) | isinstance(term, Not):
            return term
       # print("ni oknc")
        return choose_literal(term)


def dpll(stara_formula, valuation={}):
    print(str(stara_formula) + " začetek dpll")
    step1 = step12(stara_formula)
    if not step1[0]:
        formula = step1[1]
    else:
        while step1[0]:
            formula = step1[1]
            step1 = step12(formula)
    print(str(formula) + " korak3 dpll")
    if formula == T:
        return valuation
    if formula == F:
        return None ##Todo dpll kliče none
    literal = choose_literal(formula)
    formula1 = copy.deepcopy(formula)
    print(str(type(literal)) + " " + str(type(formula1)))
    formula1.simplify_by(literal)
    print(str(formula1) + " po simplify dpll")
    valuation1 = copy.deepcopy(valuation) # a je to ok kopirano?
    valuation1[literal] = True
    print("tip " + str(type(formula1)))
    result1 = dpll(formula1, valuation1)
    print(str(result1) + " result1")
    print(str(formula) + " po result1")
    if result1 is None:
        #print("ugotovu da ne gre")
        formula2 = copy.deepcopy(formula)
        formula2.simplify_by(Not(literal).flatten()) # flatten zato, da nimamo dvojne negacije
        valuation2 = copy.deepcopy(valuation) # a je to ok kopirano
        valuation2[literal] = False
        result2 = dpll(formula2, valuation2)
        if result2 is None:
            return None
        else:
            return result2 #TODO nared niz
    else:
        return result1

def readDimacs(input):
    file = open(input, 'r')
    formulaAsList = []
    #dictFrequency = {}

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
##                    if number in dictFrequency:# Lahko nardiva tut samo en if, zarad lepše kode, ne nujno bolšega časa
##                        dictFrequency[number] += 1
##                    else:
##                        dictFrequency[number] = 1
                else:
                    number2 = abs(number)
                    listOfVariables.append(Not(Variable(number2)))
##                    if number2 in dictFrequency:
##                        dictFrequency[number2] += 1
##                    else:
##                        dictFrequency[number2] = 1
            formulaAsList.append(Or(*tuple(listOfVariables)))
    formula = And(*tuple(formulaAsList))
    #tupleFrequency = sorted(dictFrequency.items(), key=operator.itemgetter(1), reverse=True) #Vrne seznam tuplov(spremenljivka, število ponovitev) od najpogostejših pada
    #listFrequency = [x for (x,y) in tupleFrequency]
    #print(dictFrequency) #TODO nej returna namesto printa
    #print(listFrequency) ##TODO return namesto printa
    file.close()
    return formula

def MOMS(formula):
    if not isinstance(formula, And):
        raise NameError("Ni and v MOMSiju")
    else:
        dictFrequency ={}
        for term in formula.terms:
            if len(term.terms)==2:
                for termsek in term.terms:
                    if termsek in dictFrequency:
                        dictFrequency[termsek] += 1
                    else:
                        dictFrequency[termsek] = 1
    mostCommon = tupleFrequency = sorted(
        dictFrequency.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    return(mostCommon)


##Test
main("Examples/tester.txt", "bruh.txt")
