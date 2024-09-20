### input(),eval()
### max(),min(),sum(),round()
### abs(),enumarate(),zip()
### sorted()
### dir(),del(),chr(),bin(),ord()

#input()

x = input("enter a number:")
print(type(x))
y = int(x)
print(type(y))

# eval()

x11 = input("enter a number:")
print(type(x11))
x1 = eval(x11)
print(type(x1))
 
print(type(eval('[1,2,34.34]')))
print(type(eval('{1,2,34.34}')))

# max()
a =12
b =13
c = 34
print(max(a,b,c))
ex = [3,4,5]
print(min(ex))

# min()
a = 12
b = 13
c = 34
print(min(a,b,c))
ex = {3,4,5}
print(min(ex))

# sum()
z = [1,2,3]
print(sum(z))

# round()
