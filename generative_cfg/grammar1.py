import random


class Grammar():
    def __init__(self, rules):
        self.rules = rules

    def nt(self, name, body, weight=1):
        self.add_non_terminal(name, body, weight)

    def add_non_terminal(self, name, body, weight=1):
        for i in range(0, weight):
            self.non_terminals.setdefault(name, []).append(body)

    def add_terminal(self, name, body):
        self.terminals[name] = body

    def run(self, state, depth):
        if self.start_symbol is None:
            raise RuntimeError('The grammars start symbol must be set')

        self.expand(self.start_symbol, state, depth)

    def __lookup(self, symbol):
        if symbol in self.non_terminals:
            return self.random.choice(self.non_terminals[symbol])
        elif symbol in self.terminals:
            return self.terminals[symbol]
        else:
            return lambda state: state.setdefault('result', []).append(symbol)

    def expand(self, symbol, state, depth, max_length):
        if depth == 0 or symbol not in self.rules or len(state['result']) >= max_length:
            state['result'].append(symbol)
            # print(state['result'])
            return

        expansion = random.choice(self.rules[symbol])
        for e in expansion:
            self.expand(e, state, depth - 1, max_length)
            # print(state['result'])
            if len(state['result']) >= max_length:
                return