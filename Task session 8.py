#!/usr/bin/env python
# coding: utf-8

# Task 1: Why and how to use protected visibility in python.
# The members of a class that are declared protected are only accessible to a class derived from it. Data members of adding a  class are declared protected by a single underscore ‘_’ symbol before the data member of that class. 

# In[5]:


class Employee:
    _companyName = 'AI' #protected attribute
    
    def __init__(self, name, age):
        self._name=name
        self.__age=age 
        

#access protected members
x=Employee("Wafaa",21)
x._name


# Task 2 :How can I access a private member from superclass in subclass

# To access the private members of the superclass you need to use setter and getter methods and call them using the subclass object.
# can access using _SuperClass then add the attribute in subclass.

# In[11]:


class subclass (Employee):
    pass
m=subclass("Wafaa",21)
m._Employee__age

