##>>> d = {'a': 1, 'b': 2}
##>>> # CODE MISSING HERE
##>>> d
##{'a': 1, 'c': 3, 'b': 2}
##
##
##
##>>> d = {'a': 1, 'b': 2}
##>>> # CODE MISSING HERE
##>>> d
##{'a': 1, 'b': 3}


##d = {'a': [1, 3], 'b': [5, 7]}

# CODE MISSING HERE
##d['a'].append(2)
##d['a'].sort()

##d['a'].insert(1, 2)
##
##d
##{'a': [1, 2, 3], 'b': [5, 7]}

d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}

##total = 0
##for k in d:
##    total = total + len(d[k])

##L = []
##for k in d:
##    L.extend(d[k])
##
##total = len(L)
total = 0
for k in d:
    total = total + k
