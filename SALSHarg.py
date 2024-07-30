'''
slash (/) arguments:
it will accept only arguments
it can't accept key and values
f1(10)  valid
f1(a=10) invalid

def f1(a/):
    print(a)

def f2(a,b,/,c,d):
    print(a,b,c,d)
f2(10,20,30,40)  # valid
# f2(10,20,c=30,d=40) # invalid

* argument
it has to sending no of arguments
note : we can use exsting keys
syntax:
def f3(*a):
    print(a)
f3(10);
f3(10,20,30);
f3();
f3(10,45);

Syntax: after * only we can pass key& value

def f4(a,b,/,*,c,d):
    print(a,b,c,d)
f4(10,20,c=30,d=40)  it's valid
f4(10,20,30,40)  it's valid
f4(10,20,c=30,d=40)  it's valid

** -> first star for key and sencond * for Value
We can't use exsiting key we can define in directly
note : create user defined keys

def f5(**args):
    print(arg["ename"],"\t",args["esal"],end="")
f5('eid'=101,'ename'='san','esal'=19000)

recursion: it has to call itself is called recursion

lamda functions: anonymus functions just like name less functions

NumPy:
pandas: we are going to create diff datasets
oops:
'''

def f1(a,b,/):
    print(a,"::",b)
f1(10,20)

def f2(a,b,/,c,d):
    print(a,"::",b,"::",c,"::",d)
f2(10,20,c=30,d=40)

def f3(*args):
    print(args)
f3(10,20)
f3()

def f4(a,b,/,*,c,d):
    print(a,"::",b,"::",c,"::",d)
f4(10,20,c=30,d=40)

def f5(**args):
    print(args)
f5(eid=101,ename='san',esal=45000)

def f6(a,b,/,**args):
    print(a,"::",args)
f6(10,20,eid=101,ename='san',esal=45000)

