import os
f = os.path.join('data', 'out_days.txt')
if os.path.exists(f):
    print(f + ' exists')
    print(os.path.getsize(f))
if os.path.isfile(f):
    print(f + ' is file')

dir_list = os.listdir('data')
for el in dir_list:
    print(el)

#print(os.path.getsize('venv'))
