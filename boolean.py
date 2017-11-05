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
        return values[self.x]

    def simplify(self):
        if self.x in {T, F}:
            return self.x
        return self

    def simplify_by(self, literal):
        if literal == self:
            self.x = T
        if literal == Not(self):
            self.x = F

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

    def simplify(self):
        if self.x == T:
            return F
        elif self.x == F:
            return T
        elif isinstance(self.x, Variable):
            return self
        else:
            return self.flatten()

    def simplify_by(self, literal):
        if literal == self:
            self.x = F
        if literal == self.x :
            self.x = T

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

    def simplify(self):
        terms = [x.simplify() for x in self.terms]
        const = self.get_dual_class()()
        if const in terms:
            return const
        # TODO: če sta dva enake vrednosti, enega vržemo ven
        return self.get_class()(*terms).flatten()


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

    def simplify_by(self, literal):
        t = set()
        for term in self.terms:
            if not term == literal:
                term.simplify_by(literal)
                t.add(term)
        self.terms = frozenset(t)


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

    def simplify_by(self, literal):
        t = set()
        for term in self.terms:
            if term == literal:
                t.add(T)
            elif not Not(term).flatten() == literal:
                term.simplify_by(literal)
                t.add(term)
        self.terms = frozenset(t)

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
