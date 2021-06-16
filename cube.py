"""
Define a Rubiks cube that is fast to manipulate and extendable to various sizes

The important part here is that a "move" is fast and determination of
correctness is fast so that the agent can evaluate states quickly and
converge on an acceptable strategy.
"""

class Cube:
    