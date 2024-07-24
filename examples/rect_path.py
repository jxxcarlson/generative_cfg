import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generative_cfg.svg_backend import SVGBackend
from generative_cfg.turtle import Turtle
from generative_cfg.grammar1 import Grammar

# Create the backend and turtle
backend = SVGBackend()
turtle = Turtle(backend)

# Define the grammar
grammar = Grammar({
    'S': ['F+F+F+F'],
    'F': ['F+F-F-FF+F+F-F', 'FF']
})

# Create a state dictionary to hold both the turtle and the result
state = {'turtle': turtle, 'result': []}

# Expand the grammar with a lower depth and a maximum result length
max_length = 500 # Adjust this value as needed
grammar.expand('S', state, 10, max_length)

# Execute the commands
for command in state['result']:
    if command == 'F':
        turtle.forward(10)
    elif command == '+':
        turtle.turn_right(90)
    elif command == '-':
        turtle.turn_left(90)

# Save the result
backend.write('rect_path.svg')

print(f"Generated {len(state['result'])} commands.") 