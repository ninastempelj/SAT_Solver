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
import time

import time
start_time = time.time()

setValuations=set()

def main(vhod, izhod):
    start_time = time.time()
    formula = readDimacs(vhod)
    resitev = dpll(formula)
    koncnaResitev = str()
    for element in resitev:
        koncnaResitev = koncnaResitev + "{} ".format(element)
    print(koncnaResitev)
    print ("time elapsed: {:.2f}s".format(time.time() - start_time))
    file = open(izhod,"w")
    file.write(koncnaResitev)##TODO formula
    file.close()

def step12(formula, valuation):
    """ Funkcija formulo poenostavi, vrne pa True in novo formulo, če je spremembna potrebna, sicer False in staro formulo"""
    changed = False
    #print(str(valuation) + " Step12")
    if isinstance(formula, Variable):
        valuation.add(formula)
        print(str(formula) + " dodan v step12")
        return changed, formula.simplify(), valuation
    if len(formula.terms) == 1:
        return changed, formula.simplify(), valuation
    for ali in formula.terms:
        tip = type(ali)
        if tip == Variable:
            valuation.add(ali)
            print(str(ali) + " dodan v step12")
            formula.evaluate(valuation)
            changed = True
        elif tip == Not:
            valuation.add(ali)
            print(str(ali) + " dodan v step12")
            formula.evaluate(valuation)
            changed = True
        elif len(ali.terms) == 1:
            for term in ali.terms:
                print(str(term) + " dodan v step12")
                valuation.add(term)
                formula.evaluate(valuation)
                changed = True
    #print(valuation)
    return changed, formula.simplify(), valuation


def random_literal(formula):
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    for term in formula.terms:
        #print(term)
        if isinstance(term, Variable) | isinstance(term, Not):
            return term
       # print("ni oknc")
        return random_literal(term)


def dpll(stara_formula, valuation=set()):
    #print(" začetek dpll" )
    #print(valuation)
    changed, formula, valuation = step12(stara_formula.simplify(), valuation)
    while changed:
        #print("d")
        changed, formula, valuation = step12(formula, valuation)
    #print(str(formula) + " korak3 dpll")
    if formula == T:
        return valuation
    if formula == F:
        return None
    literal = MOMS(formula)

    formula1 = copy.deepcopy(formula)
    formula1.simplify_by(literal)
    valuation1 = copy.deepcopy(valuation) # a je to ok kopirano?
    valuation1.add(literal)
    print(str(literal) + " dodan v dpll 1")
    result1 = dpll(formula1, valuation1)
    if result1 is None:
        #print("ugotovu da ne gre")
        formula2 = copy.deepcopy(formula)
        formula2.simplify_by(Not(literal).flatten()) # flatten zato, da nimamo dvojne negacije
        valuation2 = copy.deepcopy(valuation) # a je to ok kopirano
        valuation2.add(Not(literal).flatten())
        print(str(Not(literal)) + " dodan v dpll 2")
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
    existanceOf2 = False
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    elif not isinstance(formula, And):
        #print(formula)
        raise NameError("Ni and v MOMSiju")
    else:
        dictFrequency ={}
        for term in formula.terms:
            if len(term.terms)==2:
                existanceOf2 = True
                for termsek in term.terms:
                    if termsek in dictFrequency:
                        dictFrequency[termsek] += 1
                    else:
                        dictFrequency[termsek] = 1
        if existanceOf2:
            mostCommon = tupleFrequency = sorted(dictFrequency.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            return mostCommon
        else:
            return(random_literal(formula))



##Test
main("Examples/tester.txt", "Examples/resitev_tester.txt")
