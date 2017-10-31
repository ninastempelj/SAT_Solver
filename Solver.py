##########
#  DPLL algorithm:
#
# - Simplify formula
# - find unit clauses and reduce them |(on repeat)
# - Simplify formula                  |
#  - assume chosen l, repat algorithm
# - if fail: assume ~l, repeat algorithm
######################
from boolean import *


def step12(formula):
    changed = False
    formula.simplify()
    for term in formula.terms:
        if term.isinstance(Variable):
            changed = True
            formula.simplify_by(term)
            formula.simplify()
    # TODO: če je negacija spremenljivke
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
    formula.simplyfy_by(literal)
    valuation[literal] = T
    return dpll(formula, valuation)