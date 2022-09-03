#!/usr/bin/env python
# coding: utf-8

# In[3]:


#implementation of destructor
class A:
  
    #Initialization of class A
    def __init__(self):
        print('Class A  created')
  
    #using destructor 
    def __del__(self):
        print('The class A deleted')
  
Wa = A() 
del Wa


# In[ ]:




