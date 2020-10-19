#!/usr/bin/env python
# coding: utf-8

# ### File Handling
# 
# - File handling is an important part of any web application.
# 
# - Python has several functions for creating, reading, updating, and deleting file
# 
# #### File Handling
# - The key function for working with files in Python is the open() function.
# 
# - The open() function takes two parameters; filename, and mode.
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
# - In addition you can specify if the file should be handled as binary or text mode.
# 
# "t" - Text -Default Value.Text Mode.
# 
# "b"-  Binary - Binary Mode(eg. images)

# - To open the file ,use the built -in open() function.
# - The open() function returns a file object,which has a read() method for reading the content of the file.

# In[5]:


# File_name(Optional name) = Open 
file_txt = open("Sample.txt","r")
print(file_txt.read())


# In[9]:


file_txt = open("E:/Desktop/DataFolkz/SampleNew.txt")
file_txt.read()


# In[10]:


file_txt = open("C:/Users/hp/Desktop/Notebook_Datafolkz/SampleNew.txt")
file_txt.read()


# In[1]:


# Return the 10 first characters of the file.
file_txt = open("Sample.txt", "r")
print(file_txt.read(10))


# # Read Lines
# - You can return one line by using readline() method.
# - Example
# - Read one line of the file.

# In[6]:


# To read the first line
file_txt = open("Sample.txt", "r")
print(file_txt.readline())


# In[7]:


# To read the first two lines.
file_txt = open("Sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())


# In[3]:


# To read first three lines
file_txt = open("Sample.txt", "r")
print(file_txt.readline())
print(file_txt.readline())
print(file_txt.readline())


# - readlines() function would help us to read the lines of the files.
# - But using the readlines() we can also give the index and gives the specifications.

# In[10]:


# Using the index of readlines we can specify whichlines we want to read in perticular.
file_txt = open("Sample.txt", "r")
file_txt.readlines()[0]


# In[11]:


# Using the index of readlines we can specify whichlines we want to read in perticular.
# Using the index to read the second line,so the index should be one.
file_txt = open("Sample.txt", "r")
file_txt.readlines()[1]


# In[12]:


# Using the index of readlines we can specify whichlines we want to read in perticular.
# Using the index to read the third line,so the index should be two.
file_txt = open("Sample.txt", "r")
file_txt.readlines()[2]


# - By looping through the lines of the file, you can read the whole file,line by line.

# In[13]:


file_txt = open("Sample.txt", "r")
for x in file_txt:
    print(x)


# # Close Files
# - It is  a good prctice to always close the file when you are done with it.

# In[15]:


file_txt = open("Sample.txt", "r")
print(file_txt.readline())
file_txt.close()


# In[3]:


file_txt = open("Sample.txt", "r")
file_txt.close()


# In[4]:


print(file_txt.read())


# - Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# #### Write to an Existing File
# - To write to an existing file, you must add a parameter to the open() function:
# 
# "a" - Append - will append to the end of the file
# 
# "w" - Write - will overwrite any existing content
# 

# - Open the file "Sample 2.txt" and append content to the file.

# In[7]:


file_txt2 = open("Sample 2.txt", "a")
file_txt2.write("ola!Now there is new content.")
file_txt2.close()


# In[1]:


# open and read the file after appending
file_txt2 = open("Sample 2.txt", "r")
print(file_txt2.read())


# In[6]:


file_txt4 = open("Sample 2.txt","r")
print(file_txt4.read())


# In[50]:


file_txt4 = open("Sample 4.txt", "a")
file_txt4.write("Data Science is the best course!")
file_txt4.close()


# In[51]:


file_txt4 = open("Sample 4.txt", "r")
print(file_txt4.read())


# - Deep learning is a machine learning technique that teaches computers to do what comes naturally to humans: learn by example.   Deep learning is a key technology behind driverless cars, enabling them to recognize a stop sign, or to distinguish a           pedestrian from a lamppost.

# In[3]:


# When a particular file doesn't exists, it creates a file with that name
file_txt10 = open("sample 10.txt","a")
file_txt10.write("I am adding new content")
file_txt10.close()


# In[5]:


# open and read the file after appending
file_txt10 = open("Sample 10.txt", "r")
print(file_txt10.read())


# In[44]:


# When a particular file doesn't exists, it creates a file with that name
file_txt7 = open("sample 7.txt","a")
file_txt7.write("Data Science is the best course!")
file_txt7.close()


# In[45]:


# open and read the file after appending
file_txt7 = open("Sample 7.txt", "r")
print(file_txt7.read())


# - Open the file "Sample 3.txt" and overwrite the content. 

# In[26]:


file_txt3 = open("Sample 3.txt", "w")
file_txt3.write("Woops ! I have deleted the content!")
file_txt3.close()

# open and read the file after appending.
file_txt3 = open("Sample 3.txt", "r")
print(file_txt3.read())


# In[30]:


file_txt4 = open("Sample 4.txt", "w")
file_txt4.write("Best ! I am learning Data Science!")
file_txt4.close()

# open and read the file after appending.
file_txt4 = open("Sample 4.txt", "r")
print(file_txt4.read())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




