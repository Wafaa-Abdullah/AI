#!/usr/bin/env python
# coding: utf-8

# 1

# In[1]:



for i in range(1500,2701):
    if (i%7==0 and i%5==0):
        print(i)


# 2

# In[ ]:


def f_to_c(f):
    c = (f-32/9)*5
    return float(c)
    
def c_to_f(c):
    f = c/5+32/9
    return f
    
c= input()
f= c_to_f(c)
print(f)
    
f= input()
c= f_to_c(f)
print(c)


# 3

# In[ ]:


n=5;
for i in range (n):
    for j in range (i):
        print ('* ',end="")
    print(' ')
    
for i in range (n,0,-1):
    for j in range (i):
        print ('* ',end="")
    print(' ')


# 4

# In[ ]:


word = input("Enter the word: ")
for i in range(len(word)-1,-1,-1):
    print (word[i])


# 5

# In[ ]:


x1=input("Enter first numbers: ")
x2=input("Enter second number: ")
x3=input("Enter third number: ")
if x1>x2 and x1>x3:
    print (x1)
elif x2>x1 and x2>x3:
    print (x2)
else:
    print (x3)


# 6

# In[ ]:


l =[2,3,4]
sum=0
for i in l:
  sum+=i
print(sum)


# 7

# In[ ]:


#for i in range(0,7):
#   if (i%3!=0):
#       print(i)


for i in range (0,7):
  if (i==3 or i==6):
    continue
  print(i) 


# 8

# In[ ]:


def fact(i):
  if i==0:
    return 1
  else:
    return i * fact(i-1)

i=int(input("Enter number:"))
print(fact(i))


# 9

# In[ ]:


def li(l):
    w=[]
    for i in l:
        if i not in w:
            w.append (i)
    return w     
l=[]
l=input("Enter a list")
print(li(l))


# 10
# A lambda function can take any number of arguments, but can only have one expression.

# In[ ]:


m=lambda a : a + 15
print(m(5))
m=lambda x, y : x * y
print(m(10, 2))

