
def my_func(par_a):
    print('I am my_func')
    if callable(par_a):
        print('I am running par_a: ' + par_a())


def my_2nd_func():
    print('greetings from 2nd function')
    return 'this is the output par'


my_func(my_2nd_func())