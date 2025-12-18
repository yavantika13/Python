# #empty
# t = ()


# #tuple having integer
# t = (1,2,3)
# print(t)

# #with mixed datatypes
# t = (1, 'raju', 28, 'abc')
# print(t)

# #nested tuple
# t = (1,(2, 3, 4),[1, 'raju', 28, 'abc'])
# print(t)

# #
# t=('satish',)
# print(t)

# #
# t="satish",
# print(type(t))
# print(t)

# #
# t=('satish', 'murali', 'naveen', 'brahma')
# print(t[1])

# #
# print(t[1]-1)

# #
# t=('ABC',('satish','naveen', 'srinu'))
# print(t[1])
# print(t[1][2])

# #
# t = (1,2,3,4,5,6)
# print(t[1:4])

# print(t[:-2])

# print(t[:])

# #
# t= (1,2,3,4,[5,6,7])
# # t[2]='x'
# t[4][1]= 'satish'
# print(t)

# t = (1,2,3) + (4,5,6)
# print(t)

#
# t = (('satish', ) * 4)
# print(t)


# delete tuple
# t= (1,2,3,4,5,6)
# del t

#tuple count
t = (1,2,3,4,5,6,1,2,3,1)
t.count(1)
#tuple index
t = (1,2,3,1,3,3,4,1)
print(t.index(3))


# tuple memebership
t = (1,2,3,4,5,6)
print(1 in t)

#length
t=(1,2,3,4,5)
print(len(t))

#sort
t=(4,5,1,2,3)
new_t = sorted(t)
print(new_t)

#
t= (2,4,6,8)
print(max(t))
print(min(t))
print(sum(t))