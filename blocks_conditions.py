
def sum_numbers(aa, bb):
    print('aa inside sum=' + str(aa))
    cc = 646
    return aa+bb


a = 30
b = True

print(type(b))

if b:
    print('b is True')
    c = 60
    print('a=' + str(a))
    print('c=' + str(c))

print(c)
print(sum_numbers(58, 90))
print('a=' + str(a))
#print(cc)


if a>=40 and b:
    print('a>=40 and b is True')

d = 100 if not a>40 else -100
print(d)

b1 = True
b2 = True

''' 
mulit line 
comment

'''

# XOR
if b1 ^ b2:
    print('xor on b1 and b2 is True')
else:
    print('xor is not true')

# Rest of the division
c = 10 % 3
print(c)