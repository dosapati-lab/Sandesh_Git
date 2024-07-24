l=[]
for x in range(5,20,3):
    l.append(x)
print(l)

l1=(x for x in range(5,20,2))
l2=list(l1)
print(l2)

l3=(x for x in range(5,20,2))
[*x1]=l3
print(x1)

l4=[i for i in range(10,0,-1)] 
l5=tuple(l4) # conveeting into tuple
print(l5)

l4=[i for i in range(10,0,-1)]
l5=tuple(l4)
[*r1]=l5 # unpacking
print(r1)


for i in range(5):
    for j in range(0,i+1):
        print("*",end="")
    print()

for i in range(5+1):
    print("*" *i)

for i in range(5,0,-1):
    print("*" *i)

    