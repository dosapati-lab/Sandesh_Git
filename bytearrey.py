"""
b1=([65,66,67])
b2=([97,98,99])
b3=bytearray(b1)
b4=bytearray(b2)
print(b3)
print(b4)
b=(["hello"])
print(b.decode(hello))
print(b7)
"""

a = 'This is a bit möre cömplex sentence.'
 
print('Original string:', a)
 
print('Encoding with errors=ignore:', a.encode(encoding='ascii', errors='ignore'))
print('Encoding with errors=replace:', a.encode(encoding='ascii', errors='replace'))
