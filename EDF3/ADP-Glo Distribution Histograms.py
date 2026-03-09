#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


excel_file_path = 'Compiled 1536 Screens for Plotting_I45_included_Div0_removed_caliper_normalise_sp_mean_QC_ADP_Div0_Correct_Caliper.xlsx'
sheet_name = 'Extracted_Key_Data'
sheet_name2 = 'Selected Condtion_ADP-Glo_ALIS'


# In[7]:


xls = pd.ExcelFile(excel_file_path)
print(xls.sheet_names)


# In[8]:


# Read the first sheet
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df2 = pd.read_excel(excel_file_path, sheet_name=sheet_name2) 


# In[9]:


print(df.columns)


# In[48]:


# Choose the column for the histogram
column_name = 'Av QC Conv'  # Replace with the actual column name


# In[49]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[51]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Conversion / %', fontsize=20, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=20, fontweight='bold', labelpad=10)  # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('Conversion of 3072 Nanoscale Reactions', fontsize=20, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Remove gridlines
plt.grid(False)

# Show the plot
#plt.show()

plt.savefig('Conversion of 3072 Nanoscale Reactions3 - 01252026',dpi=900)


# In[53]:


# Choose the column for the histogram
column_name = 'SM Corrected ADP-Glo_inhib'  # Replace with the actual column name

# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]

# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Inhibition / %', fontsize=20, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=20, fontweight='bold', labelpad=10)  # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('ADP-Glo Inhibition of 3072 Nanoscale Reactions', fontsize=20, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Remove gridlines
plt.grid(False)

# Show the plot
#plt.show()

plt.savefig('ADP-Glo Inhibition of 3072 Nanoscale Reactions4 - 01252026',dpi=900)


# In[54]:


print(df2.columns)


# In[61]:


# Choose the column for the histogram
column_name = 'SM Corrected ADP-Glo Inhibition'  # Replace with the actuAverage QC Conversional column name


# In[56]:


# Specify the bin edges
bin_edges = [0, 20, 40, 60, 80, 100, 120]


# In[59]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df2[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Conversion / %', fontsize=20, fontweight='bold', labelpad=5)  # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=20, fontweight='bold', labelpad=10) # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('Conversion of 691 Nanoscale Reactions Selected for ASMS Binding Assay', fontsize=20, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Set the maximum y-axis tick to 400
plt.ylim(top=400)

# Disable y-axis tick labels
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350])

# Remove gridlines
plt.grid(False)

# Show the plot
#plt.show()

plt.savefig('Conversion of 691 Nanoscale Reactions Selected for ASMS Binding Assay2 - 01252026',dpi=900)


# In[63]:


# Plot the histogram
plt.figure(figsize=(14, 10))
plt.hist(df2[column_name], bins=bin_edges, color='#33628D', edgecolor='black')

# Set font to Arial for ticks and axis labels
plt.rcParams['font.family'] = 'Arial'

# Set axis titles
plt.xlabel('Inhibition / %', fontsize=20, fontweight='bold', labelpad=5) # Replace with your X-axis title
plt.ylabel('Frequency', fontsize=20, fontweight='bold', labelpad=10) # Y-axis title is "Frequency"

# Set the histogram title at the top center
plt.title('ADP-Glo Inhibition of 691 Nanoscale Reactions Selected for ASMS Binding Assay', fontsize=20, fontweight='bold', ha='center', va='bottom', y=1)

# Increase the size of x-axis tick labels
plt.xticks(fontsize=20, fontweight='bold')
plt.yticks(fontsize=20, fontweight='bold')

# Set the maximum y-axis tick to 400
plt.ylim(top=320)

# Disable y-axis tick labels
plt.yticks([0, 50, 100, 150, 200, 250, 300])

# Remove gridlines
plt.grid(False)

# Show the plot
#plt.show()

plt.savefig('ADP-Glo Inhibition of 691 Nanoscale Reactions Selected for ASMS Binding Assay2 - 01252026',dpi=900)


# In[ ]:




