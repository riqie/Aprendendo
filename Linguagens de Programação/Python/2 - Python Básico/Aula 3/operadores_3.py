# Operadores Lógicos: (and), (or), (not).
'''
and, verifica se os dois operadores possuem valor lógico True

or, verifica se pelo menos um dos dois operadores possuem valor lógico True

not, inverte o valor lógico do operando
'''

# and:

True and True
True and False
False and True
False and False

(3 < 4) and (" banana" > "abacaxi")
(4 < 4) and (4 == 4)

# or:

True or True
True or False
False or True
False or False

(3 < 4) or (" banana" > "abacaxi")
(4 < 4) or (4 == 4)

# not:

not True
not False
not True and False
not (True and False)
not (4 < 5)

# ordem de precedencia: 1- not, 2- and, 3- or.
