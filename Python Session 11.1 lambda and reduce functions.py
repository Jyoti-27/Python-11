#!/usr/bin/env python
# coding: utf-8

# - Create a List whose name is List1 with the elements from 200 to 500 with step 5.
# - Then create a Lambda Function to find if a number is divisible by 3 or not.
# - Then create a Lambda Function to find the cube of the number.
# - Then use filter the numbers that are divisible by 3 and store them into another list whose name is List_3.
# - Then using map find the cube of every element that we have in List1,and store the result into another list whose name is       List_cube.
# 
# 

# In[4]:


# Create a List whose name is List1 with the elements from 200 to 500 with step 5.
List1 = list(range(200,500,5))
print(List1)


# In[5]:


# Create a Lambda Function to find if a number is divisible by 3 or not.
div_3 = lambda x : x%3 == 0 

# Create a Lambda Function to find the cube of the number.
div_cube = lambda x : x**3


# In[7]:


# Using the Filter Function , Let's filter the numbers that are divisible by 3.
List_3 = filter(div_3,List1)
print(list(List_3))


# In[8]:


# Using the map Function ,Let's try to find the cube of each number from List1.
List_cube = map(div_cube,List1)
print(list(List_cube))


# In[11]:


List_4 = map(div_3,List1)
print(list(List_4))


# In[12]:


List1 = list(range(300,700,3))
type(List1)


# In[13]:


print(List1)


# - Sum of Elements in the List1.

# In[14]:


# Sum of Elements in the List1.
num = 0
for i in List1:
    num = num + i
print(num)


# # Reduce
# - Takes two Arguments cumulatively and reduces the sequence.

# - The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned in     the sequence passed along. This function is defined in “functools” module.

# In[15]:


# Reduce
# Takes two Arguments cumulatively and reduces the sequence.
addition = lambda x,y : x + y
print(List1)


# In[16]:


import functools
from functools import reduce


# In[17]:


reduce(addition,List1)


# In[22]:


List1 = [2,3,5,7,8]
addition = lambda x,y : x + y
# Then using we can find the sum of all elements in List1.
# reduce(functionname,data)
reduce(addition,List1)


# In[24]:


List10 = [50,55,60,65,70,72,99,54,10,201,210,98,300,110,123]


# In[28]:


find_greater = lambda x,y : x if x>y else y
find_greater(30,45)
find_greater(List10)


# In[25]:


find_greater = lambda x,y : x if x>y else y
find_greater(30,45)


# In[26]:


List11 = [50,110,100,95]
reduce(find_greater,List11)


# In[27]:


reduce(find_greater,List10)


# In[ ]:





# In[ ]:




