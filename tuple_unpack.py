t1=(10,20,30,40) # it's packing
[a,b,c,d]=t1 # it's unpacking
print(a)
print(b)
print(c)
print(d)

t2=("hello","san","ram","bye","jai")
[x1,x2,*x3]=t2 # * will act as collect the remaing object
print("x1:",x1)
print("x2:",x2)
print("x3 :",x3)

[x1,*x2,x3]=t2 # here * will coleect middle objects
print("x1:",x1)
print("x2:",x2)
print("x3 :",x3)

[*x1,x2,x3]=t2 # heare * will collect first 3 objects
print("x1:",x1)
print("x2:",x2)
print("x3 :",x3)

[*x1]=t2
print("x1",x1)



