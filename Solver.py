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


def step12(formula):
    changed = False
    formula.simplify()
    for term in formula.terms:
        if term.isinstance(Variable) | (term.isinstance(Not) & term.terms.isinstance(Variable)):
            changed = True
            formula.simplify_by(term)
            formula.simplify()
    return changed


def choose_literal(formula):
    for term in formula.terms:
        if term.isinstance(Variable):
            return term
        return choose_literal(term)


def dpll(formula, valuation={}):
    while step12(formula):
        pass
    if formula == T:
        return valuation
    if formula == F:
        return None
    literal = choose_literal(formula)
    formula.simplify_by(literal)
    valuation1 = valuation.copy() # a je to ok kopirano?
    valuation1[literal] = T
    result1 = dpll(formula, valuation1)
    if result1 is None:
        formula.simplify_by(Not(literal).flatten()) # flatten zato, da nimamo dvojne negacije
        valuation2 = valuation.copy() # a je to ok kopirano
        valuation2[literal] = F
        result2 = dpll(formula, valuation2)
        if result2 is None:
            return None
        else:
            return result2
    else:
        return result1