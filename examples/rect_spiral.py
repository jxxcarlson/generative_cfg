import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generative_cfg.svg_backend import SVGBackend
from generative_cfg.turtle import Turtle
from generative_cfg.grammar import Grammar

backend = SVGBackend()
turtle = Turtle(backend)

grammar = Grammar()

grammar.add_non_terminal('S', [
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(89.5),
    lambda turtle: turtle.scale(0.99),
    'S'
])

grammar.expand('S', turtle, 300)
backend.write('rect_spiral.svg')
