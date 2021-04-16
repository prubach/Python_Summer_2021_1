f = 'num_vars.py'
i = 0
with open(f, 'r') as my_file:
    lines = my_file.readlines()
    for line in lines:
        i = i + 1
        print("%i: %s" % (i, line.replace('\n', '')))