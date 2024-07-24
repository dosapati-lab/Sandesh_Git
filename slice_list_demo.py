l1=[10,20,30,40]
l1[1]=45
print("after update  from 1th index",l1)
l1[1:3] = [45,78]
print("after update 1,2nd index",l1)
l1[1:] = [21,22,23]
print("after update from 1-last index",l1)
l1[3:] = [78]
print("after update from 3rd - last index",l1)
l1[-1:] = [98]
print("after update from  -1th index",l1)
l1[-3:-1] = [91,92]
print("after update from -1 to -3 index",l1)