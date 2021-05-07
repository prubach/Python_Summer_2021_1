f = 'test.txt'
i = 0
# check 'r+' 'w+' 'a+' - all will work but differently
with open(f, 'w+') as my_file:
    lines = my_file.readlines()
    my_file.write('abc\n')
    my_file.seek(0)
    lines = my_file.readlines()
    for line in lines:
        i = i + 1
        print("%i: %s" % (i, line.replace('\n', '')))