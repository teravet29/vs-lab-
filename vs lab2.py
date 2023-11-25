Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> def printList(lst):
...     for i in range(len(lst)):
...         for j in range(len(lst[i])):
...             print(lst[i][j],end=' ')
...             print()
... 
...             
>>> s=0
>>> n=4
>>> m=4
>>> a=[]
>>> for i in range(n):
...     a.append([])
...     for j in range(m):
...         a[i].append(random.randint(10,20))
...         printList(a)
...         print()
...         for i in range(i%2==0,n):
...             for j in range(m):
...                 s=s+a[i][j]
...         print('cut setrindeki elementlerinin cemi:',s)
