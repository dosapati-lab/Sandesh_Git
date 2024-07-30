'''
What lambda reduce fun?
with out separate funs it has perform logical operation
'''

from functools import reduce
l_list=[1,2,3,4,5]
x1=reduce(lambda x,y:x+y,l_list)
x2=reduce(lambda x,y:x-y,l_list)
x3=reduce(lambda x,y:x*y,l_list)
x4=reduce(lambda x,y:x/y,l_list)
print("add : \n",x1)
print("sub : \n",x2)
print("mul : \n",x3)
print("div : \n",x4)