

def sum_bowls_recursion(r):
    if r==1:
        return 1
    else:
        return r + sum_bowls_recursion(r-1)


def sum_bowls_seq(n):
    sum_num = (n * (n + 1)) / 2
    return int(sum_num)


def sumdots(h):
    x = sum(list(range(1, h+1)))
    return x


#n = 2000000000000000000000000000000000
n = 10
print('sum of seq')
print(sum_bowls_seq(n))
print('sum of list')
print(sumdots(n))
print('recursion')
print(sum_bowls_recursion(n))
