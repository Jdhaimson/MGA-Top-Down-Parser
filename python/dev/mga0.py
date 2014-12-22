g = [ ([],[('sel','D'),('cat','C')]),
        (['the'],[('sel','N'),('cat','D')]), 
        (['big'],[('cat','S')]),
        (['bad'],[('cat','G')]),
        (['wolf'],[('cat','N')]),
        (['woods'],[('cat','N')]),
        (['in'],[('sel','D'),('cat','P')]),
]

"""
Note: this implementation of adjunction imposes a partial ordering
      on the selectors.  Thus, we explicitly add an ordering which is represented
      as a list of (from, to) binary relations. So, given the 
      list [(a,b),(b,c)] it will be interpreted as a>=b>=c
"""
partialOrderingEdges = [
    ('D','G'),
    ('G','N'),
    ('N','P'),
    ('P','C'),
]


# This maps categories to their adjuncts
adjunctsOfCategory = {
    'N': set(['S','G','P','C']),
}
