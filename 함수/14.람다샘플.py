def fn(a):
    return a + 10

def myfn(func, n):
    rst = func(n)
    print(rst)

myfn(fn, 100)
myfn(lambda a:a+10, 100)