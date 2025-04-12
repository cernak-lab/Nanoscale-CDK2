#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import ticker


# In[2]:


# Load data from Excel spreadsheet
df = pd.read_excel('Library Conversion Data.xlsx')


# In[3]:


df.head()


# In[10]:


# Define columns for each axis
x_axis = 'TWC_Conv_QC'
y_axis = 'MS_Conv_QC'
z_axis = 'ELSD_Conv_QC'
color_column = 'SM Corrected Caliper_inhib'#adjust to desired assay as needed


# In[12]:


# Set up the 3D scatter plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(
    df[x_axis],
    df[y_axis],
    df[z_axis],
    c=df[color_column],
    cmap='viridis',
    marker='o',
    label='Inhibition / %'
)

# Set axis labels
ax.set_xlabel('UV Conversion / %', fontname='Arial', fontsize=18, fontweight='bold', labelpad=20)
ax.set_ylabel('MS Conversion / %', fontname='Arial', fontsize=18, fontweight='bold', labelpad=20)
ax.set_zlabel('ELSD Conversion / %', fontname='Arial', fontsize=18, fontweight='bold', labelpad=20)

# Set axis limits
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.set_zlim([0, 100])

#gridlines
ax.grid(False)

# Set tick labels font to Arial
ax.xaxis.set_tick_params(labelsize=17, labelrotation=0, labelcolor='black')
ax.yaxis.set_tick_params(labelsize=17, labelrotation=0, labelcolor='black')
ax.zaxis.set_tick_params(labelsize=17, labelrotation=0, labelcolor='black')

# Set tick label font properties directly
for tick in ax.get_xticklabels():
    tick.set_fontname('Arial')
for tick in ax.get_yticklabels():
    tick.set_fontname('Arial')
for tick in ax.get_zticklabels():
    tick.set_fontname('Arial')
    
# Add colorbar
cbar = fig.colorbar(scatter, pad=0.1, shrink=0.7)
cbar.set_label('Inhibition / %', fontname='Arial', fontsize=18, fontweight='bold')
cbar.ax.tick_params(labelsize=15)

# Rotate the view
ax.view_init(elev=20, azim=-60)  # Adjust the elevation and azimuth angles here

plt.savefig('Conversion Colored by Caliper Inhibition', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()


# In[ ]:




