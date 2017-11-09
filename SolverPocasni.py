##########
#  DPLL algorithm:
#
# - Simplify formula
# - find unit clauses and reduce them |(on repeat)
# - Simplify formula                  |
#  - assume chosen l, repeat algorithm
# - if fail: assume ~l, repeat algorithm
######################
from booleanPocasni import *
import operator
import copy
import time
import sys

command_line = False
if len(sys.argv) == 3:
    vhod = sys.argv[1]
    izhod = sys.argv[2]
    command_line = True


def main(vhod, izhod):
    start_time = time.time()
    formula = read_dimacs(vhod)
    resitev = dpll(formula)
    if resitev is None:
        koncna_resitev = "0"
    else:
        koncna_resitev = str()
        for element in resitev:
            if isinstance(element, Not):
                koncna_resitev += "-{} ".format(Not(element).flatten())
            else:
                koncna_resitev += "{} ".format(element)

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
    file = open(izhod, "w")
    file.write(koncna_resitev)
    file.close()
    return(koncna_resitev)


def step12(formula):
    """ Funkcija formulo poenostavi, vrne pa True in novo formulo,
    če je spremembna potrebna, sicer False in staro formulo"""
    changed = False
    changes = set()
    if isinstance(formula, Variable) or isinstance(formula, Not):
        if formula.x not in {T, F}:
            return changed, T, {formula}
        else:
            assert False, "V step12 je prišla Variable(T ali F)"
    if len(formula.terms) == 0:
        return changed, formula, set()
    if len(formula.terms) == 1:
        return changed, T, {x for x in formula.terms}
    for ali in formula.terms:
        tip = type(ali)
        if tip in {Variable, Not}:
            if ali.x in {T, F}:
                assert False, "Formula ni poenostavljena " + str(formula)
            changed = True
            changes.add(ali)
        elif len(ali.terms) == 1:
            for term in ali.terms:
                if term.x in {T, F}:
                    assert False, "Formula ni poenostavljena " + str(formula)
                changed = True
                changes.add(term)
        elif ali in {T,F}:
            assert False, "Formula ni bila poenostavljena " + str(formula)
    return changed, formula, changes


def random_literal(formula):
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    for term in formula.terms:
        if isinstance(term, Variable) | isinstance(term, Not):
            return term
        return random_literal(term)


def dpll(stara_formula, valuation=set()):
    changed, formula, changes = step12(stara_formula.simplify())
    if not changed:
        valuation = valuation | changes
    else:
        while changed:
            for literal in changes:
                if type(formula) ==  Variable:
                    valuation.add(copy.deepcopy(literal))
                formula.simplify_by(literal)
                formula = formula.simplify()
                if formula in {T, F}:
                    break
                valuation.add(literal)
            changed, formula, changes = step12(formula.simplify())
        valuation = valuation | changes

    if formula == T:
        return valuation
    if formula == F:
        return None
    literal = moms(formula)

    formula1 = copy.deepcopy(formula)
    formula1.simplify_by(literal)
    valuation1 = copy.deepcopy(valuation)
    valuation1.add(literal)

    result1 = dpll(formula1.simplify(), valuation1)

    if result1 is None:
        formula2 = copy.deepcopy(formula)
        formula2.simplify_by(Not(literal).flatten())
        valuation2 = copy.deepcopy(valuation)
        valuation2.add(Not(literal).flatten())

        result2 = dpll(formula2.simplify(), valuation2)
        return result2
    else:
        return result1


def read_dimacs(vhod):
    file = open(vhod, 'r')
    formula_as_list = []
    for line in file:
        first_sign = line[0]
        if first_sign == "p" or first_sign == "c":
            pass
        else:
            list_of_variables = []
            list_of_numbers = list(map(int, line.strip().split(" ")))  # Vrne seznam števil
            list_of_numbers.remove(0)  # Odstrani ničlo na koncu
            for number in list_of_numbers:
                if number > 0:
                    list_of_variables.append(Variable(number))
                else:
                    number2 = abs(number)
                    list_of_variables.append(Not(Variable(number2)))
            formula_as_list.append(Or(*tuple(list_of_variables)))
    formula = And(*tuple(formula_as_list))
    file.close()
    return formula


def moms(formula):
    existence_of_2 = False
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    elif not isinstance(formula, And):
        print(formula)
        raise NameError("V Momsiju ni And")
    else:
        dict_frequency = {}
        for term in formula.terms:
            if len(term.terms) == 2:
                existence_of_2 = True
                for termsek in term.terms:
                    if termsek in dict_frequency:
                        dict_frequency[termsek] += 1
                    else:
                        dict_frequency[termsek] = 1
        if existence_of_2:
            most_common = sorted(dict_frequency.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            return most_common
        else:
            return random_literal(formula)

def moms1(formula):
    existence_of_2 = False
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    elif not isinstance(formula, And):
        print(formula)
        raise NameError("Ni and v MOMSiju")
    else:
        dict_frequency2 = {}
        slovar = dict_frequency3 = {}
        for term in formula.terms:
            if len(term.terms) == 2:
                existence_of_2 = True
                slovar = dict_frequency2
            for termsek in term.terms:
                if termsek in slovar:
                    slovar[termsek] += 1
                else:
                    slovar[termsek] = 1
            slovar = dict_frequency3
        if existence_of_2:
            most_common = sorted(dict_frequency2.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        else:
            most_common = sorted(dict_frequency3.items(), key=operator.itemgetter(1), reverse=True)[0][0]
        return most_common


def moms2(formula):
    existence_of_2 = False
    if isinstance(formula, Variable) | isinstance(formula, Not):
        return formula
    elif not isinstance(formula, And):
        print(formula)
        raise NameError("Ni and v MOMSiju")
    else:
        dict_frequency = {}
        for term in formula.terms:
            if len(term.terms) == 2:
                existence_of_2 = True
                for termsek in term.terms:
                    if isinstance(termsek, Variable):
                        if termsek in dict_frequency:
                            dict_frequency[termsek] += 1
                        else:
                            dict_frequency[termsek] = 1
                    else:
                        if Not(termsek).flatten() in dict_frequency:
                            dict_frequency[Not(termsek).flatten()] += 1
                        else:
                            dict_frequency[Not(termsek).flatten()] = 1


        if existence_of_2:
            most_common = sorted(dict_frequency.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            return most_common
        else:
            return random_literal(formula)

if command_line:
    print(main(vhod, izhod))


#dato = "graftester"
#print(main("Examples/sudoku_mini.txt", "Examples/sudoku_mini_resitev_test.txt"))
#print(main("Examples/{}.txt".format(dato), "Examples/{}_r.txt".format(dato)))

