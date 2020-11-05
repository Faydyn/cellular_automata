# cellular_automata
Some exercises on Cellular Automata, inspired by university module

It primaryly should be able to generate new states 1-dimensional CAs from the former state by applying Wolframs Rules, which are just the decimal numbers from 0-255 (inclusive).

## TODO
- start programming by entering:
  - a) a binary string, that represents the initial state, where 0 is dead and 1 is alive
  - b) a number from 0..255 to define the rule applied for the simulation 
  - c) an option to choose, if the CA should behave like a torus
- implement rule maker, which takes an integer (from b)) (unsigned byte rather), and return a dict (\[bool\],bool). E.g. ```rules = { [0,0,0]:1, ..., [1,1,1]:1 }```. Need the unique Binary Sum Represation. The "active" Exponents encoded in Binary make the next cell a 1, else 0.  E.g. ```Rule 10: 10 = 8 + 2 = 2^3 + 2^1 -> Exponents: {3,1} -> {011,001} -> rules = { [0,1,1]:1, [0,0,1]:1, [X,X,X]:0 }``` 
  
- generate a starting state of any length > 2 ()
