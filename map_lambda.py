'''
map() --> it has to adding  additional output
'''
l_list=[1,2,3,4,5]
sqrrt=list(map(lambda x:x**2,l_list)) # square root of each element
a=list(map(lambda x:x+10,l_list)) #adding value for each element
s=list(map(lambda x:x-1,l_list)) # substracting value from each elemet
print("sqrt::\n",sqrrt)
print("adding :: \n",a)
print("substraction :: \n",s)