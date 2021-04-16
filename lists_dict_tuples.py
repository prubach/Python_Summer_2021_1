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
for row in l5:
    print(row)
    for el in row:
        print(el)

print('----------------')
print(l5[0][1])

l6 = [0, 0, 0]
for j in range(len(l5)):
    for k in range(len(l5[j])):
        l6[k] += l5[j][k]
print(l6)

sum_all = 0
for row in l5:
    #sum_all += sum(row)
    sum_all = sum_all + sum(row)
print(sum_all)
#print(len(set(l4)))

import numpy as np

nl5 = np.array(l5)
print(nl5)
#print('Sum of elements: ' + str(np.sum(l5)))
print('Sum of elements: %i' % (np.sum(l5)))
print('Sum of rows: ' + str(np.sum(l5, axis=1)))
print('Sum of cols: ' + str(np.sum(l5, axis=0)))

f = 45346.6326525225
print('My float num: %.8f' % f)

s = 'My float num: %.8f' % f
print(s)
