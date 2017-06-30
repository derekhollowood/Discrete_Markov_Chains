# Discrete_Markov_Chains
Python class for discrete Markov chains.  Includes a few common Markov chains.

## Examples
### User-defined Markov chain
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: P = {}

-- P will represent the transition matrix

In [3]: P['A'] = dmc.dsp.dsp({'B' : 2/3, 'C' : 1/3})

In [4]: P['B'] = dmc.dsp.dsp({'C' : 2/3, 'A' : 1/3})

In [5]: P['C'] = dmc.dsp.dsp({'A' : 2/3, 'B' : 1/3})

-- "dsp" is for "discrete probability space".
-- These lines create the transition probabilities.
-- For instance from state A there is a 2/3 probability of moving to B and a 1/3 probability of moving to C.

In [6]: MC = dmc.dmc(P)

-- Create a Markov chain from P.

In [7]: walk = dmc.mcwalk(MC, 'A')

-- Initial state is A.

In [8]: walk.walk(19)

-- Go 19 steps.

In [9]: walk
Out[9]: 
A
C
A
C
A
C
A
B
C
A
B
C
B
C
A
B
C
B
C
A

In [10]: walk.sample_dist()
Out[10]: 
C : 0.4
A : 0.35
B : 0.25

-- Sample distribution from the walk.  In the long run these probabilities should all converge to 1/3.
```

### Bitstring chain
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.bitstring_chain(3)

In [3]: walk = dmc.mcwalk(MC, '000')

In [4]: walk.walk(19)

In [5]: walk
Out[5]: 
000
001
101
111
101
111
101
111
101
001
101
001
101
111
110
111
011
001
101
111

In [6]: walk.sample_dist()
Out[6]: 
001 : 0.2
000 : 0.05
011 : 0.05
101 : 0.35
110 : 0.05
111 : 0.3

-- At each step a randomly selected bit is switched.
-- This walk never hit the states 010 or 100.
```

### Simple Symmetric Random Walk
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.simple_symm_random_walk()

In [3]: walk = dmc.mcwalk(MC, 0)

In [4]: walk.walk(20)

In [5]: walk
Out[5]: 
0
1
2
3
2
1
2
1
2
3
2
1
0
-1
-2
-3
-4
-3
-2
-1
0

-- This chain goes up or down by 1 at each step with equal probability.
```

### Sliding Puzzle
```ipython3
In [1]: import Discrete_Markov_Chains as dmc

In [2]: MC = dmc.sliding_puzzle(3,3)

In [3]: a = dmc.sliding_puzzle_standard_start(3,3)

In [4]: a
Out[4]: 
[[0 1 2]
 [3 4 5]
 [6 7 8]]

In [5]: walk = dmc.mcwalk(MC, a)

In [6]: walk.walk(9)

In [7]: walk
Out[7]: 
[[0 1 2]
 [3 4 5]
 [6 7 8]]
[[1 0 2]
 [3 4 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 4 2]
 [0 3 5]
 [6 7 8]]
[[1 4 2]
 [6 3 5]
 [0 7 8]]
[[1 4 2]
 [0 3 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 0 2]
 [3 4 5]
 [6 7 8]]
[[1 4 2]
 [3 0 5]
 [6 7 8]]
[[1 4 2]
 [3 5 0]
 [6 7 8]]
 
 -- At each step the 0 switches places with one of its neighboring entries each with equal probability.
 ```
