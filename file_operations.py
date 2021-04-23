days_d = {1: 'Monday', 2: 'Tuesday', 7: 'Sunday'}

my_list = [3425, 25252, 46778, 4]
print(str(days_d))
f = 'out_days.txt'
with open(f, 'w') as my_file:
    my_file.write(str(days_d))

import json
f = 'out_days.json'
#with open(f, 'w') as my_file:
#    json.dump(my_list, my_file)
    #my_file.
# alternative way instead of 'with'
my_file = open(f, 'w')
json.dump(my_list, my_file)
my_file.close()


with open(f, 'r') as my_file:
    out_days_d = json.load(my_file)
    #print(out_days_d['1'])
    print(out_days_d)
    print(type(out_days_d))
    print(sum(out_days_d))
