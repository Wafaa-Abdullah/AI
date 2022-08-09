#!/usr/bin/env python
# coding: utf-8

# In[1]:


#binary search implementation 
def binary_search(list,n):
    low = 0
    high = len(list)-1
    mid = 0


    while low<=high:
        mid=(high + low)//2
        if list[mid]<n:
            low=mid+1
        elif list[mid]>n:
            high=mid-1
        else:
            return mid
    return False

list = [ 2, 3, 4, 10, 40 ]
n = 10
x = binary_search(list,n)
if x==False:
    print("Element is not found")
else:
    print("Element is found at index ",str(x))


# In[9]:


#iterative funcation
def Reverse_string(s):
    r=""
    for i in s:
        r = i + r
    return r

Reverse_string("wafaa") 


# In[8]:


#recursive funcation
def Reverse_string(s):
    if not s:
        return ""
    else:
        return Reverse_string(s[1:]) + s[0]

Reverse_string("wafaa") 


# In[24]:


#iterative funcation
def fact(num):
    n=1
    for i in range(num):
        n=n*(i+1)
    return n
fact(2)


# In[7]:


#recursive funcation
def fact_rec(num):
    if num<=1: #base case
        return 1
    else:
        return num*fact_rec(num-1)
fact_rec(2)


# In[ ]:




