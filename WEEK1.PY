
a = 10
print(a)
print(type(a))

b = 10.5
print(b)
print(type(b))

c = "andani"
print(c)
print(type(c))

d= 10 + 11j
print(d)
print(type(d))

f = True
print(f)
print(type(f))


a ="mihir"
print(a)
# 100 = "mihir"    error  variable name error
#10a =100          error  variable name error
# $ = 1245         error  variable name error
a1 = "patel"
print(a1)

_abs = 10
print(_abs)

a_b =123
print(a_b)

v = 125 + 100j
print(v)
print(type(v))
print(v.real)


a = "andani mihir"

print(a[0])
print(a[5])
print(a[7])
print(a[10])
print(a[-1])
print(a[-5])
print(a[-7])

b= [100,250,80,90,"mihir",0.45,True,100+10j,0.11]

print(b[0])
print(b[5])
print(b[7])
print(b[-1])
print(b[-5])

#mutable
b[2] = "mihit"
print(b)

#unmutebale
"""a[1] = "h"
print(a)"""


print(10+20)
print(10-20)
print(20/3)
print(20*10)
print(20//3)
print(20**2)
print(20%3)

print(20>10)
print(20<10)
print(10>=100)
print(10<=100)
print(10>=10)
print(10<=10)
print(10!=100)
print(10!=10)

print()
print("and")
print(True and False)
print(False and True)
print( False and False)
print(True and True)

print()
print("or")
print(True or False)
print(False or True)
print( False or False)
print(True or True)

print()

print(~10)
print(bin(10))
print(bin(-11))

print()
print(10 & 7)

print()
print( 10 | 5)

print()
print(10 >> 3)
print(bin(10))
print(bin(3))
print(bin(1))

print()
print(10 << 3)
print(bin(10))
print(bin(3))
print(bin(80))



print(input())

a=input("enter ")
print(a)
print(type(a))

a=int(input("enter "))
print(a)
print(type(a))


a= 45
if a > 40 :
    print ("pass")

a= 40
if a > 40 :
    print ("pass")  

a=int(input ("mark"))
if  a > 40 :
    print(a)
    print("pass")


if  a > 40 :
    print(a)
    print("pass")
else:
    print(a)
    print("fail")



if  a > 90 :
    print(a)
    print(" frist class pass")

elif a > 70 :
    print(a)
    print("second class")

elif a > 40 :
    print(a)
    print("pass")
else:
    print(a)
    print("fail")



a=5
b=0

while  b < a:
    print(b)
    b= b+1


a= 8
b= 0
while b < a:
    print(b)
    b=b+2


a=5
b=0

while  b < a:
    print(b)
    b= b+1
else:
    print("close")

a=10
b=0

while  b < a:
    print(b)
    b= b+1
    if b==3:
        break
else:
    print("close")


a=7
b=0

while  b < a:
    print(type(b))
    b= b+1
    if b==3:
        continue
    print(b)
else:
    print("close")


a= "andani"

for b in a:
    print(b)



a= "andani"

for b in a:
    print(b)
else:
    print("patel")

a= "anadaani"

for b in a:
   
    if b == "d":
        break
    print(b)
else:
    print("patel")


for c in a:
    print(c)
    if c == "d":
        continue
    print(c)

else:
    print("close")


print(range(10))

l =list(range(10))
print(l)

