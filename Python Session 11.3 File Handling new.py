#!/usr/bin/env python
# coding: utf-8

# File Handling
# File handling is an important part of any web application.
# 
# Python has several functions for creating, reading, updating, and deleting file
# 
# File Handling
# The key function for working with files in Python is the open() function.
# 
# The open() function takes two parameters; filename, and mode.
# 
# -There are four different methods (modes) for opening a file:
# 
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# 
# "x" - Create - Creates the specified file, returns an error if the file exists
# 
# In addition you can specify if the file should be handled as binary or text mode.
# "t" - Text -Default Value.Text Mode.
# 
# "b"- Binary - Binary Mode(eg. images)
# 
# To open the file ,use the built -in open() function.
# The open() function returns a file object,which has a read() method for reading the content of the file.

# In[11]:


# File_name(Optional name) = Open 
file_txt = open("Data 1.txt","r")
print(file_txt.read())


# In[4]:


file_txt = open("C:/Users/Hp/Desktop/Python/Data Folkz/DS1/Data 1.txt")  
file_txt.read()


# In[42]:


# Return the 10 first characters of the file.
file_txt = open("Sample.txt", "r")
print(file_txt.read(10))


# In[44]:


# To read the first line
file_txt = open("Sample.txt", "r")
print(file_txt.readline())


# In[45]:


# To read the first two lines.
file_txt = open("Sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())


# In[47]:


# To read first three lines
file_txt = open("Sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())
print(file_txt.readline())


# In[48]:


# Using the index of readlines we can specify whichlines we want to read in perticular.
file_txt = open("Sample.txt", "r")
file_txt.readlines()[0]


# In[ ]:




