import numpy as np
import time
from itertools import zip_longest


square = u'\u25a0'
ruledict = {}

# takes a 1-d CA (np.array) and prints it. Transforms 1 to square and 0 to spaces


def print_ca_state(state):
    def asciiart(c): return square if c else ' '
    print(f'|{"".join([asciiart(x) for x in state])}|')


# takes a decimal number between 0..255 and returns a dict with each of the 2^3 Possibilities mapped to the result in the next state
def get_rule_dict(rule_number):
    binary_num = bin(rule_number)[2:]  # binary rule number
    rule_dict = {}
    """
    Reverse the Binary Rule Number and zip it with the exponents.
    If Binary Number < 128, we need to fill with 0, so just use the itertools function for that
    The Key is then the binary representation of the decimal exponent, and the next state the digit of the Binary Rule Number at the corresponding place.
    """
    for exp, status in list(zip_longest(range(8), binary_num[::-1], fillvalue='0')):
        # same as above, need to fill with 0. But no zipping, so its better this way
        key = bin(exp)[2:].rjust(3, '0')
        rule_dict[key] = bool(int(status))
    return rule_dict


def simulate_next_state(state, is_torus=0, default_value=False):
    next_state = np.copy(state)

    # lambda to transform arrayslice to dict repres
    def slice2key(slice):
        return ''.join([str(int(cell)) for cell in list(slice)])

    for index in range(len(next_state)):
        indices = range(index-1, index+2)
        # this makes it so that it changes a line at once, not step by step, because it refers to state (not next state)
        tripleslice = state.take(indices, mode='wrap')

        if (index == 0 or index == len(state)-1) and not is_torus:
            tripleslice[min(index, 2)] = default_value

        next_state[index] = ruledict[slice2key(tripleslice)]

    return next_state


start = input('Enter 0s and 1s to define the initial state!')
rule = int(input(
    'Enter a number from 0..255 (inclusive) to define the rule that will be applied!'))
is_torus = int(input(
    'Enter a number! Anything other than 0 will make this CA behave like a Torus.'))
default_val = False
if not is_torus:
    default_val = int(input(
        'Enter the default Value for the Borders, since the CA is no Torus.'))


initial_state = np.array([int(elem) for elem in start], dtype=np.bool)
ruledict = get_rule_dict(rule)

print(
    list(zip([f"|{ '|'.join(list(k.replace('0', ' ').replace('1', square))) }|" for k in ruledict.keys()], [square if v else ' ' for v in ruledict.values()])))
print('\n')
for _ in range(50000):
    print_ca_state(initial_state)
    time.sleep(0.016)
    initial_state = simulate_next_state(initial_state, is_torus, default_val)
