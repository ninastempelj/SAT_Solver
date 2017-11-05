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

setValuations = set()


def main(vhod, izhod):
    start_time = time.time()
    formula = read_dimacs(vhod)
    resitev = dpll(formula)
    koncna_resitev = str()
    for element in resitev:
        koncna_resitev += "{} ".format(element)
    print(koncna_resitev)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
    file = open(izhod, "w")
    file.write(koncna_resitev)
    file.close()


def step12(formula):
    """ Funkcija formulo poenostavi, vrne pa True in novo formulo,
    če je spremembna potrebna, sicer False in staro formulo"""
    changed = False
    changes = set()
    #print(formula)
    if isinstance(formula, Variable):
        print(str(formula) + " dodal Variable1 step12")
        return changed, formula.simplify(), {formula}
    if len(formula.terms) == 1:
        return changed, formula.simplify(), set()
    for ali in formula.terms:
        tip = type(ali)
        if tip == Variable:
            if ali.x not in {T,F}:
                formula.simplify_by(ali)
                changed = True
                print(str(ali) + " dodal Variable2 step12")
                changes.add(ali)
        elif tip == Not:
            if not ali.x in {T, F}:
                formula.simplify_by(ali)
                changed = True
                print(str(ali) + " dodal Not step12")
            changes.add(ali)
        elif len(ali.terms) == 1:
            for term in ali.terms:
                if not term == T or term == F:
                    formula.simplify_by(term)
                    changed = True
                    changes.add(term)
    return changed, formula.simplify(), changes


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
            valuation = valuation | changes
            changed, formula, changes = step12(formula)
    if formula == T:
        return valuation
    if formula == F:
        return None
    literal = moms(formula)

    formula1 = copy.deepcopy(formula)
    formula1.simplify_by(literal)
    valuation1 = copy.deepcopy(valuation)
    valuation1.add(literal)
    print(str(literal) + "dodal v dpll2")
    result1 = dpll(formula1, valuation1)
    if result1 is None:
        formula2 = copy.deepcopy(formula)
        formula2.simplify_by(Not(literal).flatten())  # flatten zato, da nimamo dvojne negacije
        valuation2 = copy.deepcopy(valuation)
        print(str(literal) + "dodal v dpll2")
        valuation2.add(Not(literal).flatten())
        result2 = dpll(formula2, valuation2)
        if result2 is None:
            return None
        else:
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
        raise NameError("Ni and v MOMSiju")
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


# main("Examples/tester.txt", "Examples/tester_r.txt")
main("Examples/primer3.txt", "Examples/primer3_r.txt")
