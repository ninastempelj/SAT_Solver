class Formula:
    def __ne__(self, other):
        return not (self == other)

    def flatten(self):
        return self

    def get_variable(self, mapping):
        if self not in mapping:
            mapping[self] = fresh_variable()
        return mapping[self]


class Variable(Formula):
    def __init__(self, x):
        self.x = x

    def __str__(self, parentheses=False):
        return str(self.x)

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        if isinstance(other, Formula):
            return isinstance(other, Variable) and self.x == other.x
        else:
            return self.x == other

    def evaluate(self, values):
        if self in values:
            return True
        if Not(self) in values:
            return False
        if self.x == T:
            return True
        if self.x == F:
            return False
        assert False, "haha čudno je"

    def simplify(self, literal):
        if self.x in {T, F}:
            return self.x
        if literal == self:
            return T
        if literal == Not(self):
            return F
        return self

    def equiv(self, variable):
        return And(Or(variable, Not(self)), Or(Not(variable), self))


class Not(Formula):
    def __init__(self, x):
        self.x = make_formula(x)
        self.terms = frozenset({self.x})

    def __str__(self, parentheses=False):
        return "~" + self.x.__str__(True)

    def __hash__(self):
        return hash(("~", self.x))

    def __eq__(self, other):
        return isinstance(other, Not) and self.x == other.x

    def evaluate(self, values):
        return not self.x.evaluate(values)

    def flatten(self):
        if isinstance(self.x, Not):
            return self.x.x
        else:
            return self

    def simplify(self, literal):
        return Not(self.x.simplify(literal))

    def equiv(self, variable):
        return And(Or(variable, self.x), Or(Not(variable), self))


class Multi(Formula):
    def __init__(self, *args):
        self.terms = frozenset(make_formula(x) for x in args)

    def __str__(self, parentheses=False):
        if len(self.terms) == 0:
            return self.empty
        elif len(self.terms) == 1:
            return next(iter(self.terms)).__str__(parentheses)
        out = self.connective.join(x.__str__(True) for x in self.terms)
        if parentheses:
            return "(%s)" % out
        else:
            return out

    def __hash__(self):
        return hash((self.connective, self.terms))

    def __eq__(self, other):
        return isinstance(other, self.get_class()) \
            and self.terms == other.terms

    def evaluate(self, values):
        return self.fun(x.evaluate(values) for x in self.terms)

    def flatten(self):
        this = self.get_class()
        terms = (x.flatten() for x in self.terms)
        out = this(*sum([list(x.terms) if isinstance(x, this)
                         else [x] for x in terms], []))
        if len(out.terms) == 1:
            return next(iter(out.terms))
        else:
            return out

class And(Multi):
    empty = "T"
    connective = r" /\ "
    fun = all

    def get_class(self):
        return And

    def get_dual_class(self):
        return Or

    def equiv(self, variable):
        return And(Or(variable, *(Not(x).flatten() for x in self.terms)),
                   *(Or(Not(variable), x) for x in self.terms))

    def simplify(self, literal=Or()):
        terms = []
        for term in self.terms:
            if term == F:
                return F
            elif term == T:
                pass
            elif not term == literal:
                term.simplify(literal)
                if term == F:
                    return F
                elif term == T:
                    pass
                else:
                    terms.append(term)
        return And(*terms).flatten()


class Or(Multi):
    empty = "F"
    connective = r" \/ "
    fun = any

    def get_class(self):
        return Or

    def get_dual_class(self):
        return And

    def equiv(self, variable):
        return And(Or(Not(variable), *self.terms),
                   *(Or(variable, Not(x)) for x in self.terms))

    def simplify(self, literal=And()):
        terms = []
        for term in self.terms:
            if term == T:
                return T
            elif term == F:
                pass
            elif not Not(term).flatten() == literal:
                term = term.simplify(literal)
                if term == T:
                    return T
                elif term == F:
                    pass
                else:
                    terms.append(term)
        return Or(*terms).flatten()


T = And()
F = Or()


def make_formula(x):
    if isinstance(x, Formula):
        return x
    else:
        return Variable(x)

counter = 0


def fresh_variable():
    global counter
    counter += 1
    return Variable(("__", counter))
