from generative_cfg import *

backend = SVGBackend()
turtle = Turtle(backend)

grammar = Grammar()

grammar.add_non_terminal('S', [
    # lambda turtle: turtle.forward(1),
    'H',
    'Scale',
    lambda turtle: turtle.turn_left(60),
    lambda turtle: turtle.forward(1),
    
    'S'
])

scale = 0.99
grammar.add_non_terminal('Scale', [
    lambda turtle: turtle.scale(scale)
])


grammar.add_non_terminal('H', [
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    lambda turtle: turtle.forward(1),
    lambda turtle: turtle.turn_right(60),
    'S'
])

grammar.expand('S', turtle, 5)
backend.write('x1.svg')
