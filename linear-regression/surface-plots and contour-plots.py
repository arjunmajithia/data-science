#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[8]:


import matplotlib.pyplot as plt


# In[9]:


from mpl_toolkits.mplot3d import Axes3D


# In[10]:


a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])


# In[11]:


a, b = np.meshgrid(a, b)
print(a)
print(b)
# a will be repeated 4(number of elements in b) times along row
# b will be repeated 3(number of elements in a) times along column


# In[16]:


# the following will give 3d axis
fig = plt.figure()
axes = fig.gca(projection = '3d')
axes.plot_surface(a, b, a+b, cmap = 'coolwarm')
# x-values, y-values, z-values
# red denotes high z-value and blue less
plt.show()


# In[17]:


a = np.arange(-1, 1, 0.02)
b = a

a, b = np.meshgrid(a, b)


# In[18]:


fig = plt.figure()
axes = fig.gca(projection = '3d')
axes.plot_surface(a, b, a**2+b**2, cmap = 'rainbow')
plt.show()


# In[19]:


fig = plt.figure()
axes = fig.gca(projection = '3d')
axes.contour(a, b, a**2+b**2, cmap = 'rainbow')
plt.show()


# In[ ]:




