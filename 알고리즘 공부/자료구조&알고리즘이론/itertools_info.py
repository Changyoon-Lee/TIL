import itertools
print('--')
# a = [(1,2),(3,4)]
# l1=product(a, repeat=1)
# l2=product(*a, repeat=1)
# l3=product(a, repeat=2)
# l4=product(*a, repeat=2)

# for l in [l1,l2,l3,l4]:
#     res = list(i for i in l)
#     print('{}\n{}\n---'.format(len(res), res))
#################################################

# data = [100, 200, 300, 400]
# daily_data = list(zip(range(10), data))
# daily_data2 = list(itertools.zip_longest(range(10), data))
# print(daily_data)
# print(daily_data2)

##########3
# cycle = itertools.cycle(('on','off'))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))
# print(next(cycle))

#############

# squares = list(map(pow, range(10), itertools.repeat(2)))
# squares2 = list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)]))
# print(squares)
# print(squares2)

######################

# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2]
# names = ['Corey', 'Nocole']

# result = [i for i in itertools.combinations(numbers, 2)]
# result2 = [i for i in itertools.permutations(numbers, 2)]
# result3 = [i for i in itertools.product(numbers, repeat = 3)]
# result4 = [i for i in itertools.combinations_with_replacement(numbers, 3)]

# print('combination\n', result, sep='', end='\n\n')
# print('permutation\n', result2, sep='', end='\n\n')
# print('product\n', result3, sep='', end='\n\n')
# print('combination with replacement\n', result4, sep='', end='\n\n')

#####################

# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2]
# names = ['Corey', 'Nocole']

# combined = [i for i in itertools.chain(letters, numbers, names)]
# print(combined)

# result1 = [i for i in itertools.islice(range(10), 5)]
# result2 = [i for i in itertools.islice(range(10), 1, 5)]
# result3 = [i for i in itertools.islice(range(10), 1, 5, 2)]

# print(result1)
# print(result2)
# print(result3)

########################

# def lt_2(n):
#     if n < 2:
#         return True
    
# numbers = [0, 1, 2, 3]
# selectors = [True, True, False, True]

# result1 = [i for i in itertools.compress(numbers, selectors)]
# result2 = [i for i in filter(lt_2, numbers)] #파이썬 filter함수
# result3 = [i for i in itertools.filterfalse(lt_2, numbers)] #false만 반환한다

# print(result1, result2, result3, sep='\n')


############################

# def lt_2(n):
#     if n < 2:
#         return True
    
# numbers = [0, 1, 2, 3, 2, 1, 0]
# result1 = [i for i in itertools.dropwhile(lt_2, numbers)]
# result2 = [i for i in itertools.takewhile(lt_2, numbers)]

# print(result1, result2, sep='\n')

#######################
# import operator

# numbers = [1, 2, 3, 2, 1, 0]
# result1 = [i for i in itertools.accumulate(numbers)]
# result2 = [i for i in itertools.accumulate(numbers, operator.mul)]
# print(result1, result2, sep='\n')

########

# def get_state(person):
#     return person['state']


# people = [
#     {'name': 'John Doe', 'city': 'Gotham', 'state': 'NY'},
#     {'name': 'Jane Doe', 'city': 'Kings Landing', 'state': 'NY'},
#     {'name': 'Corey Schafer', 'city': 'Boulder', 'state': 'CO'},
#     {'name': 'Al Einstein', 'city': 'Denver', 'state': 'CO'},
#     {'name': 'John Henry','city': 'Hinton', 'state': 'WV'},
#     {'name': 'Randy Moss', 'city': 'Rand', 'state': 'WV'},
#     {'name': 'Nicole K', 'city': 'Asheville', 'state': 'NC'},
#     {'name': 'Jim Doe', 'city': 'Charlotte', 'state': 'NC'},
#     {'name': 'Jane Taylor', 'city': 'Faketown', 'state': 'NC'}
# ]

# person_group = itertools.groupby(people, get_state)

# copy1, copy2 = itertools.tee(person_group)
# print(type(copy1))
# import copy
# c= copy.copy(copy2)

# for key, group in copy1:
#     print(key)
#     for person in group:
#         print(person)
#     print()

# for key, group in copy2:
#     print(key, len(list(group)))


a = [1,2,3,4]
b, c = itertools.tee(a)
print(next(b))
print(next(c))
print(next(c))
print(next(b))

print('--')