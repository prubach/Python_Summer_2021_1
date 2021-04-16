l1 = [25256, 5625, 7979, 664]
for el in l1:
    print(el)

print(l1[1:3])
print(l1[-2:])

l2 = [2525, 26556, 'abcc', 543.245]
s = 0
for el in l2:
    print(el)
    if type(el) is not str:
        s += el
print(s)

l3 = [90825, 5625, 63, 909]
l4 = l1 + l3
print(l4)

print(l4.index(5625))
print(l4.count(5625))

l4.sort()
print(l4)

for i in range(len(l4)):
    print('Element %i at position %i' % (l4[i], i))

# get 'cc' from the list l2
print(l2[2][2:])

l5 = [[1, 6, 8], [8, 9, 3], [3, 9, 4]]
# sum rows, sum cols and sum of all


