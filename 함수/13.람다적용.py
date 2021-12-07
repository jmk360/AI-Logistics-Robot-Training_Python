data1 = [10,20,30,25]
data2 = [(10,20),(70,15),(40,50)]
data3 = [{'kor':10,'eng':20},
         {'kor':70,'eng':15},
         {'kor':40,'eng':50}]

def myfileter(func,  dt):
    # return [ n for n in dt if n>=20]
    return ( n for n in dt if func(n) )

rst = myfileter( lambda v:v<25, data1)
print( list(rst)) #[next(rst),next(rst)]
print( rst )
# print( next(rst ))

f = filter( lambda v:v<25, data1)
print( f ) #generator
for n in f: #n = next(f) ..
    print(n)
# print( next(f))