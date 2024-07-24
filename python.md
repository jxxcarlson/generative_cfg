python -m venv env
source env/bin/activate

>>> import os
>>> def ls(x):
...   print(os.listdir(x))
... 
>>> ls('generative_cfg')
>>> 

## Experiment with grammar object

### Import the grammar module

```
from generative_cfg.grammar import *
```

### Initialize a grammar object

```
grammar = Grammar()
```

### Add some non-terminals

```
grammar.add_non_terminal("S", ["A", "B"])
grammar.add_non_terminal("A", ["a"])
grammar.add_non_terminal("B", ["b"])
```

The rule below will have double the weight

```
grammar.nt("C", ["c"], weight=2)
```

### Now add some terminals 

```
grammar.add_terminal("T", lambda state: print("Terminal reached"))
```

### Set the start symbol

```
grammar.start_symbol = "S"
```

### Run the grammar

```
state = {}  # You might need to initialize this based on your specific needs
depth = 10  # Set the maximum depth for expansion
grammar.run(state, depth)
```

### Notes

To expand a specific symbol: `grammar.expand("A", state, depth)`

#### Create more complex rules
grammar.add_non_terminal("S", ["A", "B", "C"])
grammar.add_non_terminal("B", ["b", "B"])

#### Run the grammar multiple times to see different outcomes
for _ in range(5):
    state = {}
    grammar.run(state, 10)
    print(state)  # This will show you the final state after each run


### To paste in

```
grammar = Grammar()
grammar.add_non_terminal("S", ["A", "B"])
grammar.add_non_terminal("A", ["a"])
grammar.add_non_terminal("B", ["b"])
grammar.nt("C", ["c"], weight=2)
grammar.add_terminal("T", lambda state: print("Terminal reached"))
grammar.start_symbol = "S"
state = {}  # You might need to initialize this based on your specific needs
depth = 10  # Set the maximum depth for expansion
grammar.run(state, depth)
```



