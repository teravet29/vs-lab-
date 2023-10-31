x=int(input("massivin sol serhedi:"))
y=int(input("massivin sag serhedi:"))
n=int(input("massivin elementlerinin sayi:"))
a=[0]*n
k=0
s=0
from random import randint
for i in range(n):
    a[i]=randint(x,y)
print(a)
for x in a:
    s=s+a[i]
    k=k+1
print(S=s/len(a))
