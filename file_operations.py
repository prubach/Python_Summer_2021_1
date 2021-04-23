days_d = {1: 'Monday', 2: 'Tuesday', 7: 'Sunday'}

my_list = [3425, 25252, 46778, 4]
print(str(days_d))
f = 'data/out_days.txt'

#f = '/Users/...'
# w - write
# a - append
with open(f, 'a') as my_file:
    my_file.write(str(days_d))

import json
f = 'data/out_days.json'
#with open(f, 'w') as my_file:
#    json.dump(my_list, my_file)
    #my_file.
# alternative way instead of 'with'
my_file = open(f, 'w')
json.dump(my_list, my_file)
my_file.close()

print('----- JSON ----')
with open(f, 'r') as my_file:
    out_days_d = json.load(my_file)
    #print(out_days_d['1'])
    print(out_days_d)
    print(type(out_days_d))
    print(sum(out_days_d))

import _pickle
f = 'data/out_days.dat'
with open(f, 'wb') as my_file:
    _pickle.dump(my_list, my_file)

print('----- PICKLE ----')
with open(f, 'rb') as my_file:
    out_obj = _pickle.load(my_file)
    print(out_obj)
    print(type(out_obj))
    print(sum(out_obj))