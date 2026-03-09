import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

def return_properties(smiles):
    from rdkit import Chem
    from rdkit.Chem import Descriptors, rdMolDescriptors, Crippen
    # read in smiles
    mol = Chem.MolFromSmiles(smiles)  # Replace 'CCO' with your molecule's SMILES
    # compute features
    HBD = rdMolDescriptors.CalcNumHBD(mol)
    HBA = rdMolDescriptors.CalcNumHBA(mol)
    charge = Chem.GetFormalCharge(mol)
    PSA = rdMolDescriptors.CalcTPSA(mol)
    logP = Crippen.MolLogP(mol)
    fsp3 = rdMolDescriptors.CalcFractionCSP3(mol)
    return [HBD, HBA, charge, PSA, logP, fsp3]

def select_compounds_1(conc):
    if conc in [0.05,0.1]: return True
    else: return False

def select_compounds_2(conc):
    if conc in [0.05,0.1,0.5]: return True
    else: return False

# load in data
df = pd.read_excel("EXP_smiles.xlsx", sheet_name='Selected Condtion_ADP-Glo_ALIS')
selected = pd.read_csv('ScaledUp_Compounds_v3.csv')

# compute features
features = ['HBD', 'HBA', 'Charge', 'PSA', 'LogP', 'Fsp3']
df[features] = df['Smiles'].apply(lambda x: pd.Series(return_properties(x)))

# create tsne
tsne = TSNE(n_components=2, perplexity=10)
embedding = tsne.fit_transform(df[['HBD', 'HBA', 'Charge', 'PSA', 'LogP', 'Fsp3']])
df.loc[:, 'tsne_x'] = embedding[:, 0]
df.loc[:, 'tsne_y'] = embedding[:, 1]

# define font size
csfont_title = {'fontname':'Arial','fontsize':20, 'fontweight': 'bold'}
csfont_main = {'fontname':'Arial','fontsize':16}

# select compounds based on Lowest ALIS Enzyme Concentration
product_list_1 = df[df['Lowest ALIS Enzyme Concentration'].apply(select_compounds_1)]
product_list_2 = df[df['Lowest ALIS Enzyme Concentration'].apply(select_compounds_2)]
selected_list_1= product_list_1[product_list_1['Product Name'].isin(selected['Product Name'])]
selected_list_2= product_list_2[product_list_2['Product Name'].isin(selected['Product Name'])]

plt.figure(figsize=(10, 8))
sns.scatterplot(x='tsne_x', y='tsne_y', data=product_list_1, color='#440154', s=120, label='tight',alpha=0.6)
sns.scatterplot(x='tsne_x', y='tsne_y', data=selected_list_1, color='#fde725', s=200, label='isolated',alpha=0.6)

# Customize the plot
plt.xlabel('TSNE X', labelpad=0, **csfont_title)
plt.ylabel('TSNE Y', labelpad=0, **csfont_title)

# Set the x-axis ticks and labels
plt.xticks(**csfont_main)

# Set the y-axis to a logarithmic scale with whole integer labels
plt.yticks(**csfont_main)

legend = plt.legend()#prop=csfont_main)
legend.set_visible(False)
plt.savefig('tsne_new.png',dpi=600)
