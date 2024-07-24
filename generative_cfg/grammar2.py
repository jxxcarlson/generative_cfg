import random

class Grammar():
    def __init__(self):
        self.terminals = {}
        self.non_terminals = {}
        self.start_symbol = None

    # TODO: I've added this as a kind of syntax sugar,
    # to make programs more concise
    def nt(self, name, body, weight=1):
        self.add_non_terminal(name, body, weight)

    def add_non_terminal(self, name, body, weight=1):
        for i in range(0, weight):
            self.non_terminals.setdefault(name, []).append(body)

    def add_terminal(self, name, body):
        self.terminals[name] = body

    def run(self, state, depth):
        if self.start_symbol is None:
            raise RuntimeError('The grammar\'s start symbol must be set')

        self._expand(self.start_symbol, state, depth)  # Changed to self._expand

    def _lookup(self, symbol):  # Changed from __lookup to _lookup
        if symbol in self.non_terminals:
            return random.choice(self.non_terminals[symbol])
        else:
            return self.terminals[symbol]

    def _expand(self, symbol, state, depth):  # Changed from expand to _expand
        if depth > 0:
            element = self._lookup(symbol)

            # element is either a list (non-terminal) or a lambda
            if isinstance(element, list):
                for e in element:
                    if isinstance(e, str):
                        self._expand(e, state, depth - 1)
                    else:
                        e(state)
            else:
                element(state)
                
