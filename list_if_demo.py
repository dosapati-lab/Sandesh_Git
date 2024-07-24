l1=[10,21,10,33,43,27,10,10]
print(l1)
l2=[95 if x==10 else x for x in l1]
print(l2)
l3=["even" if x%2==0 else x  for  x in l1]
print(l3)
l4=["odd" if x%2!=0 else x  for  x in l1]
print(l4)
l5=["even" if x%2==0 else "odd" for  x in l1]
print(l5)


l6=[10,21,30,41,50]
l7=[]
l8=[]
for i in l6:
    if i%2==0:
        l7.append(i)
    else:
        l8.append(i)    
print(l7)
print(l8)
