days_d = {1: 'Monday', 2: 'Tuesday', 7: 'Sunday'}
print(str(days_d))
f = 'out_days.txt'
with open(f, 'w') as my_file:
    my_file.write(str(days_d))

import json
f = 'out_days.json'
with open(f, 'w') as my_file:
    json.dump(days_d, f)
