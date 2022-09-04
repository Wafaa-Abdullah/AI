#!/usr/bin/env python
# coding: utf-8

# Read file and list each name, phone number and email.

# In[1]:


x_file=open("file.txt","r")
for x in x_file.readlines():
    print(x)
x_file.close()


# In[ ]:




