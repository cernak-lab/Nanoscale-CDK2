#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


excel_file_path = 'All_Library_Data.xlsx'
sheet_name = 'All_Library_Data'
sheet_name2 = 'Selected_Condition_ADP-Glo_ALIS'


# In[3]:


# Read the first sheet
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df2 = pd.read_excel(excel_file_path, sheet_name=sheet_name2) 


# In[4]:


print(df.columns)


# In[5]:


# Choose the column for the histogram
column_name = 'Av QC Conv'  # Replace with the actual column name


# In[6]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[7]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Conversion / %', fontsize=26, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=26, fontweight='bold', labelpad=10)  # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('Reaction Conversion – Full Nanoscale Library', fontsize=26, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Remove gridlines
plt.grid(False)

plt.savefig('Nanoscale Conversion - Full Library',dpi=900)


# In[8]:


# Choose the column for the histogram
column_name = 'SM Corrected ADP-Glo_inhib'  # Replace with the actual column name


# In[9]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[10]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Conversion / %', fontsize=26, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=26, fontweight='bold', labelpad=10)  # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('ADP-Glo Inhibition – Full Nanoscale Library', fontsize=26, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Remove gridlines
plt.grid(False)

plt.savefig('ADP-Glo Inihibition - Full Library',dpi=900)


# In[11]:


print(df2.columns)


# In[12]:


# Choose the column for the histogram
column_name = 'Average QC Conversion'  # Replace with the actuAverage QC Conversional column name


# In[13]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[14]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df2[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Conversion / %', fontsize=26, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=26, fontweight='bold', labelpad=10) # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('Reaction Conversion – ASMS Selection', fontsize=26, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Set the maximum y-axis tick to 400
plt.ylim(top=400)

# Disable y-axis tick labels
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350])

# Remove gridlines
plt.grid(False)

plt.savefig('Reaction Conversion - ASMS Selection',dpi=900)


# In[15]:


# Choose the column for the histogram
column_name = 'SM Corrected ADP-Glo Inhibition'  # Replace with the actuAverage QC Conversional column name


# In[16]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[17]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df2[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Inhibition / %', fontsize=26, fontweight='bold', labelpad=5) # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=26, fontweight='bold', labelpad=10) # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('ADP-Glo Inhibition – ASMS Selection', fontsize=26, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Set the maximum y-axis tick to 400
plt.ylim(top=320)

# Disable y-axis tick labels
plt.yticks([0, 50, 100, 150, 200, 250, 300])

# Remove gridlines
plt.grid(False)

plt.savefig('ADP-Glo Inhibition - ASMS Selection',dpi=900)


# In[ ]:




