def fn( dt ):
    dt[0] = 100

my=[10,20,30,40]
fn( my )
print( my )
'''
my=[10,20,30,40] # my = list( [10,20,30,40])
# aa = my #shallow copy
# aa = [10,20,30,40]
aa = my.copy() #deep copy
aa[0] = 100
print( id(aa), id(my))
print( aa )
print( my )
# fn(my )
'''