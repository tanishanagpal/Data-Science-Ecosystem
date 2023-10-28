#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data Science Tools and Ecosystem are summarized.

# Some of the popular languages that Data Scientists use are:
#     1.Python
#     2.SQL
#     3.R
#     4.JavaScript

# Some of the commonly used libraries used by Data Scientists include:
#     1.Numpy
#     2.Tensorflow
#     3.Keras
#     4.Pandas

# # Table

# | x-poistion (m) || y-position (m) || Time (s)   vx v v|
# | -------------- || :------------- ||:------- |

# |Name |Gender|Age  |Origin | 
# |-----|:-----|:---:|:-----:|
# |Jack |Male  |23   |USA    |
# |Susan|Female|22   |Canada |
# 

# import pandas as pd
# 
# a_list = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# 
# pd.DataFrame(a_list, columns=["First", "Second", "Third"])
# 

# ### Data Science Tools
# 
# | Data Science Tool | Description |
# |---|:---|:---:|
# | Jupyter Notebook | A web-based interactive development environment for creating and sharing documents that contain live code, equations, visualizations, and narrative text. |
# | RStudio | An integrated development environment for R, a programming language and free software environment for statistical computing and graphics. |
# | Visual Studio Code | A cross-platform code editor by Microsoft with support for debugging, syntax highlighting, intelligent code completion, snippets, and refactoring. |
# 

# Below are a few examples of evaluating arithmetic expressions in Python

# In[2]:


# Multiply two numbers
product = 5 * 10

# Add two numbers
sum = 5 + 10

# Print the results
print("The product is", product)
print("The sum is", sum)


# In[3]:


def convert_minutes_to_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return hours, minutes

# Example usage:

minutes = 190
hours, minutes = convert_minutes_to_hours(minutes)

print(f"{minutes} minutes is equal to {hours} hours and {minutes} minutes.")


# Objectives:
#     1.Create markdown cell with title of the notebook
#     2.Create a markdown cell for an introduction
#     3.Create a markdown cell for an introduction
#     4.Create a markdown cell to list data science languages
#     5.Create a markdown cell to list data science libraries
#     6.Create a markdown cell with a table of Data Science tools
#     7.Create a markdown cell introducing arithmetic expression examples
#     8.Create a code cell to multiply and add numbers
#     9.Create a code cell to convert minutes to hours

# # Author

# Tanisha Nagpal

# In[ ]:




