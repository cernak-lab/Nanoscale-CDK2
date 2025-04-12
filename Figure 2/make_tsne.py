import dill
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in data
data = dill.load(open("all_data_for_tsne.pkl", "rb"))
Z, n, n2, marked = data["Z"], data["n"], data["n2"], data["marked"]

# construct pandas dataframe
df = pd.DataFrame(Z, columns=['x', 'y'])
df.loc[:n, 'category'] = 'enumerated'
df.loc[n:n2, 'category'] = 'plate1'
df.loc[n2:, 'category'] = 'plate2'

# creat figure
fig,ax = plt.subplots(figsize=(10,8))

# define font size
csfont_title = {'fontname':'Arial','fontsize':20, 'fontweight': 'bold'}
csfont_main = {'fontname':'Arial','fontsize':16}

#fig,ax = plt.subplots(figsize=(8,8))
sns.scatterplot(x='x', y='y', data=df[df['category']=='enumerated'], color='#440154', s=10, label='virtual compound',alpha=0.01)
sns.scatterplot(x='x', y='y', data=df[df['category']=='plate1'], color='#fde725', s=20, label='plate 1',alpha=1.0,edgecolor='grey',linewidth=0.5)
sns.scatterplot(x='x', y='y', data=df[df['category']=='plate2'], color='#5cb380', s=20, label='plate 2',alpha=1.0,edgecolor='grey',linewidth=0.5)

# Customize the plot
plt.xlabel('TSNE X', labelpad=5, **csfont_title)
plt.ylabel('TSNE Y', labelpad=5, **csfont_title)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

# Add the legend with the specified font properties
legend = plt.legend(loc='upper right',
                    fontsize=16,
                    bbox_to_anchor=(1, 1),
                    borderpad=0.05,
                    handletextpad=0.05,
                    labelspacing=0.05,
                    borderaxespad=0.06)

frame = legend.get_frame()
frame.set_edgecolor('black')       # Set the frame edge color if needed
frame.set_linewidth(0.8)           # Set the frame edge width
frame.set_alpha(1.0)               # Set the frame transparency
frame.set_boxstyle('Square', pad=0.05)  # Reduce the padding inside the legend box


for lh in legend.legendHandles: 
    lh.set_alpha(1)
    
#legend.set_visible(False)
plt.savefig('tsne.png',dpi=600,pad_inches=0.1)
