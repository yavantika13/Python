# empty
my_dict = {}

#with integer
my_dict = {1: 'abc', 2: 'xyz'}
print(my_dict)

#with mixed key
my_dict = {'name': 'satish', 1: ['abc', 'xyz']}
print(my_dict)

#using dict
my_dict= dict()

#
my_dict = ([(1, 'abc'), (2, 'xyz')])
print(my_dict)

#dict access
my_dict = {'name': 'satish', 'age': '27', 'address': 'jbp'}
print(my_dict['name'])

 #print(my_dict['degree']) # not defiend key not present

print(my_dict.get('address'))
print(my_dict.get('degree'))

# add or modity element
my_dict = {'name': 'satish', 'age':
        '23', 'address':'jbp'}
my_dict['age']='27'
print(my_dict)

my_dict['degree']='M.Tech'
print(my_dict)

# del

my_dict = {'name': 'satish', 'age':'27', 'address':'jbp'}
print(my_dict.pop('age'))
print(my_dict)

my_dict = {'name': 'satish', 'age':'27', 'address':'jbp'}
my_dict.popitem()
print(my_dict)


squares = {2: 4, 3: 9, 4: 16, 5:25}
del squares[2]
print(squares)

squares.clear()
print(squares)

 #squares = {2: 4, 3: 9, 4: 16, 5:25}
# del squares
# print(squares) #nameerror because dict is deleted


# methods
squares = {2: 4, 3: 9, 4: 16, 5:25}
my_dict = squares.copy()
print(my_dict)

subjects = {}.fromkeys(['maths', 'english', 'hindi'],0)
print(subjects)


subjects = {2: 4, 3: 9, 4: 16, 5:25}
print(subjects.items())

subjects = {2: 4, 3: 9, 4: 16, 5:25}
print(subjects.values())

d = {}
print(dir(d))

# dict comprehension

d = {'a':1, 'b':2, 'c':3}
for pair in d.items():
    print(pair)

d = {'a':1, 'b':2, 'c':3, 'd':4}
new_dict = {k:v for k, v in d.items() if v > 2 }
print(new_dict)    

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
d = {k+ 'c':v * 2 for k, v in d.items() if v > 2 }
print(d)