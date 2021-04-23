l3 = [90825, 5625, 5625, 63, 909]
l3.insert(1, 400)

l4 = []
for el in l3:
    l4.append(el*2)

print(l4)

l5 = [el*2 for el in l3]
print(l5)

s1 = set(l5)
print(s1)

t1 = (14, 25)
print(t1)
print(t1[0])
# tuple is immutable - you can't change it
#t1[0] = 5252
a, b = (365, 3636)
print(a)
print(b)

d1 = {'a': 'abcva', 'b': 'sggsgb', 'c': 'def'}
print(d1['b'])

for k in d1.keys():
    print('Key: %s Value: %s' % (k, d1[k]))

print(list(d1.values()))

day = 7 # 1-7
if day==1:
    print('Monday')
elif day==2:
    print('Tuesday')
#...
elif day==7:
    print('Sunday')


days_d = {1: 'Monday', 2: 'Tuesday', 7: 'Sunday'}
print(days_d[day])