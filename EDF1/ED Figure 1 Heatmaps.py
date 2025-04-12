#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


def create_heatmap_from_excel(excel_file, location_column, data_column):
    # Read Excel file
    df = pd.read_excel(excel_file, sheet_name='Yields ED Figure 1')
    
# Extract row and column information from the 'location' column
    df['Row'] = df[location_column].str[0]
    df['Column'] = df[location_column].str[1:].astype(int)
    
    # Create pivot table with row as rows, column as columns, and selected data as values
    pivot_df = df.pivot_table(index='Row', columns='Column', values=data_column)
    
    # Reorder rows and columns
    rows_96well = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # Highlight: Added rows for a 96 well plate
    columns_96well = range(1, 13)  # Highlight: Adjusted columns for a 96 well plate
    pivot_df = pivot_df.reindex(index=rows_96well, columns=columns_96well)
    
    # Clip values to ensure they fall within 0 and 100
    pivot_df = pivot_df.clip(0, 100)
    
    # Create heatmap
    plt.figure(figsize=(16, 8))
    heatmap = sns.heatmap(pivot_df, cmap='viridis', annot=False, fmt=".1f", linecolor='black', linewidth='0.003', cbar=False)
    #plt.title(f'{data_column}')
    plt.xlabel('')
    plt.ylabel('')
    plt.yticks(rotation=0)
    
  # Set colorbar limits
    plt.gca().set_ylim(len(rows_96well), 0)  # Ensure colorbar matches the top of the C row
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=100))
    sm._A = []  # Fake up the array of the scalar mappable
    
    cbar = plt.colorbar(sm, ax=plt.gca())  # Use gca() to explicitly specify the current axes
    cbar.set_ticks([0, 20, 40, 60, 80, 100])  # Adjust tick positions
    cbar.set_label('Yield / %', fontname='Arial', fontsize='14')  # Set colorbar label
    
    # Adjust colorbar position
    cbar.ax.set_position([0.76, 0.111, 0.02, 0.5])  # [left, bottom, width, height]
    
    # Save the heatmap as a Tif file with 300dpi
    # Adjust the filename to include the data column name
    plt.savefig(f'{data_column}_heatmap.tif', dpi=300, bbox_inches='tight')
    
    # Show the heatmap
    plt.show()    


# In[12]:


# Modify the parameters below according to your data
create_heatmap_from_excel('Yields ED Figure 1.xlsx', 'Location', 'Plate 1 Ent Yield')


# In[ ]:




