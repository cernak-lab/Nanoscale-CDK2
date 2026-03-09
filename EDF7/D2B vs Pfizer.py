#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import ScalarFormatter, MultipleLocator
import matplotlib.patches as patches
import matplotlib as mpl


# In[3]:


# Set the global font to Arial
mpl.rcParams['font.family'] = 'Arial'


# In[4]:


# Load data from the Excel spreadsheet (replace 'your_data.xlsx' with your file path)
df = pd.read_excel('D2B vs Pfizer.xlsx')


# In[5]:


# Print all column names in the DataFrame
print(df.columns)


# In[12]:


# Define the variables
x_variable = 'Lowest ALIS Enzyme Concentration'
y_variable = 'Ki'
z_variable = 'SM Corrected ADP-Glo Inhibition'
size_variable = 'Average QC Conversion'  # Added variable for dot size

# Create a logarithmic x-axis
plt.figure(figsize=(10, 6))
cmap = plt.get_cmap('viridis', 100)

# Create a numerical representation for categories
unique_categories = df[x_variable].unique()
category_mapping = {cat: idx + 1 for idx, cat in enumerate(unique_categories)}
df['CategoryNumeric'] = df[x_variable].map(category_mapping)

# Create the scatter plot with size variable
sc = plt.scatter(
    df['CategoryNumeric'], df[y_variable],
    c=df[z_variable],
    cmap=cmap,
    marker='o',
    s=df[size_variable],
    alpha=0.62,
    vmin=0  # <-- sets the colorbar minimum to 0
)

# Customize the plot
plt.xlabel(r'ASMS Lowest Enzyme Conc. / $\mathbf{\it{\mu}}$M', labelpad=0, fontweight='bold', fontname='Arial', fontsize=14)
plt.ylabel(r'Reported Ki', labelpad=4.5, fontweight='bold', fontname='Arial', fontsize=14)

# Set the x-axis ticks and labels
plt.xticks(list(category_mapping.values()), list(category_mapping.keys()), rotation=45, ha='right', fontsize=12)

plt.xlim(df['CategoryNumeric'].min() - 0.5, df['CategoryNumeric'].max() + 0.5)

ax = plt.gca()

# Major ticks (labelled)
yticks_major = plt.yticks()[0]
ax.set_yticks(yticks_major)

# Minor ticks (unlabeled) halfway between major ticks
yticks_minor = (yticks_major[:-1] + yticks_major[1:]) / 2
ax.set_yticks(yticks_minor, minor=True)

# Style major ticks
ax.tick_params(axis='y', which='major', labelsize=12, length=7, width=1.0, color='black')
# Style minor ticks: shorter, thinner, gray
ax.tick_params(axis='y', which='minor', length=4, width=0.8, color='black')

# Add a color bar
cbar = plt.colorbar(sc, orientation='vertical', pad=0.02)
cbar.set_label('ADP-Glo Inhibition / %', fontweight='bold', fontsize=14)  # Set colorbar label to bold
cbar.ax.tick_params(labelsize=12)  # Set colorbar tick labels to fontsize 12
cbar.solids.set_alpha(1.00)

# Show the plot
plt.tight_layout()
#plt.show()
plt.savefig('D2B vs Pfizer',dpi=900)


# In[9]:


# Define the variables
x_variable = 'Lowest ALIS Enzyme Concentration'
y_variable = 'pKi'
z_variable = 'SM Corrected ADP-Glo Inhibition'
size_variable = 'Average QC Conversion'  # Added variable for dot size

# Create a logarithmic x-axis
plt.figure(figsize=(10, 6))
cmap = plt.get_cmap('viridis', 100)

# Create a numerical representation for categories
unique_categories = df[x_variable].unique()
category_mapping = {cat: idx + 1 for idx, cat in enumerate(unique_categories)}
df['CategoryNumeric'] = df[x_variable].map(category_mapping)

# Create the scatter plot with size variable
sc = plt.scatter(
    df['CategoryNumeric'], df[y_variable],
    c=df[z_variable],
    cmap=cmap,
    marker='o',
    s=df[size_variable],
    alpha=0.62,
    vmin=0  # <-- sets the colorbar minimum to 0
)

# Customize the plot
plt.xlabel(r'ASMS Lowest Enzyme Conc. / $\mathbf{\it{\mu}}$M', labelpad=0, fontweight='bold', fontname='Arial', fontsize=14)
plt.ylabel(r'Reported pKi', labelpad=4, fontweight='bold', fontname='Arial', fontsize=14)

# Set the x-axis ticks and labels
plt.xticks(list(category_mapping.values()), list(category_mapping.keys()), rotation=45, ha='right', fontsize=12)

plt.xlim(df['CategoryNumeric'].min() - 0.5, df['CategoryNumeric'].max() + 0.5)

ax = plt.gca()

# Major ticks (labelled)
yticks_major = plt.yticks()[0]
ax.set_yticks(yticks_major)

# Minor ticks (unlabeled) halfway between major ticks
yticks_minor = (yticks_major[:-1] + yticks_major[1:]) / 2
ax.set_yticks(yticks_minor, minor=True)

# Style major ticks
ax.tick_params(axis='y', which='major', labelsize=12, length=7, width=1.0, color='black')
# Style minor ticks: shorter, thinner, gray
ax.tick_params(axis='y', which='minor', length=4, width=0.8, color='black')

# Add a color bar
cbar = plt.colorbar(sc, orientation='vertical', pad=0.02)
cbar.set_label('ADP-Glo Inhibition / %', fontweight='bold', fontsize=14)  # Set colorbar label to bold
cbar.ax.tick_params(labelsize=12)  # Set colorbar tick labels to fontsize 12
cbar.solids.set_alpha(1.00)

# Show the plot
plt.tight_layout()
#plt.show()
#plt.savefig('EDF6 Scatter Plot',dpi=900)


# In[ ]:




