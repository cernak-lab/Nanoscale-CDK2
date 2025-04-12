#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.ticker import FixedLocator, FuncFormatter


# In[2]:


pd.options.display.float_format = '{:,.2f}'.format


# In[3]:


df = pd.read_csv("New ALIS Scatter_All Data.csv")
df.head()


# In[4]:


def label(x, color, label):
    ax = plt.gca()
    ax.text(1.0, 0.13, label, color="black", fontsize=30, fontweight='bold', transform=ax.transAxes, ha='left')

# set up the plot aesthetics
sns.set(rc={'figure.figsize':(10,8)})
sns.set(style="white", rc={"axes.facecolor": (0, 0, 0, 0)}, font_scale=2.0)
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)

# set up the facet grid
g = sns.FacetGrid(df, row="ALIS Lowest Enzyme Conc (uM)", hue="ALIS Lowest Enzyme Conc (uM)", aspect=15, height=1, palette=pal)

# plot the kde plots with narrower ridges
g.map(sns.kdeplot, "ADP-Glo Inhibition (%)", clip_on=True, fill=True, alpha=1, lw=0.4, bw_adjust=0.5)
g.map(sns.kdeplot, "ADP-Glo Inhibition (%)", clip_on=False, color="w", lw=0.6, bw_adjust=0.5)
g.map(plt.axhline, y=0, lw=2, clip_on=False)

# put the target names on the plots
g.map(label, "ALIS Lowest Enzyme Conc (uM)")

# remove the y-axis label
g.set(ylabel='')

# a bunch of fiddling to make the plots pretty
g.despine(bottom=True, left=True)
g.fig.subplots_adjust(hspace=-0.5)
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)
# Set x-axis label and x-axis tick label font size and weight
for ax in g.axes.flatten():
    ax.set_xlabel("ADP-Glo Inhibition / %", color="black", fontsize=30, fontweight='bold', labelpad=10)
    labels = [int(label) for label in ax.get_xticks()]  # Convert labels to integers
    ax.set_xticklabels(labels, fontsize=30, fontweight='bold')  # Adjust the fontsize and fontweight as needed


# savefig
plt.savefig("Narrow Reverse Ridge Plot Labels Right Larger Font SF Bold.png", dpi=900, bbox_inches='tight', pad_inches=0)
plt.show()


# In[ ]:




