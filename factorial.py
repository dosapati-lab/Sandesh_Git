def f1(num):
    fact=1
    while num!=0:
        fact=fact*num
        print(num)
        num=num-1
        print(fact)
    
n1=int(input("Enter a number :"))
f1(n1)
