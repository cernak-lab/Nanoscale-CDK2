import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pycirclize import Circos
import matplotlib.patches as patches

# Read the CSV file
df1 = pd.read_excel("Exp.xlsx",sheet_name='Conversion all Conditions')
df2 = pd.read_excel("Exp.xlsx",sheet_name='Selected Condtion_ADP-Glo_ALIS')
scaleup = pd.read_csv('ScaledUp_Compounds.csv')
scaleup = scaleup['Product Name']

# define name map
name_map = {'Relay-FFS-493-1':'5','Relay-FFS-493-2':'6','Relay-FFS-493-3':'7','Relay-FFS-493-4':'8','Relay-FFS-493-5':'9','Relay-FFS-493-6':'10'}

# Get a lit of Amines and Acids
Amines = sorted(list(set(df1.Amine)))
Acids  = sorted(list(set(df1.Acid)))

# group fata by Amines
grouped  = df1.groupby('Amine')
amine_df = {name_map[name]: group for name, group in grouped}

# Initialize Circos
sectors = {amine:len(dfi)//4 for amine,dfi in amine_df.items()}
circos  = Circos(sectors, space=5, start=14, end=346, endspace=False)
Icircos = Circos(sectors, space=0)

# draw for each amines
for sector in circos.sectors:
    ############################# LOAD DATA #########################
    df = amine_df[sector.name]

    ############################# ANALYZE DATA #########################
    reshaped_df = pd.DataFrame(columns=['Amine', 'Acid', 'Condition', 'Average QC Conversion'])
    # Iterate through the acid sequence
    for acid in Acids:
        # Iterate through the condition sequence
        for condition in ['A','B','C','D']:
            # Filter the rows for the current acid and condition and append them to the reshaped DataFrame
            acid_condition_row = df[(df['Acid'] == acid) & (df['Condition'] == condition)]
            reshaped_df = pd.concat([reshaped_df, acid_condition_row])

    # convert into a 4*128 dimention array
    pivoted_df = reshaped_df.pivot(index='Condition', columns='Acid', values='Average QC Conversion')
    conversion = pivoted_df.to_numpy()

    # find 'SM Corrected ADP-Glo Inhibition' for each acid
    inhibition = []
    NT_index   = []
    y_labels   = []
    s_condition= {}
    cat_map = {0.05:0,0.1:1,0.5:2,1:3,2:4,5:5,10:6,20:7,0:8,-1:9} # NT--10
    for count,acid in enumerate(Acids):
        product = df[(df['Acid'] == acid) & (df['Condition'] == 'A')]['Product Name'].item()
        try:
            itemi = df2[df2['Product Name']==product]
            inhib = itemi['SM Corrected ADP-Glo Inhibition'].item()
            laec  = itemi['Lowest ALIS Enzyme Concentration'].item()
            s_condition[acid] = itemi['Condition'].item()
            inhibition.append(min(110.0,inhib))
            y_labels.append(cat_map[laec])
        except:
            inhibition.append(-20.0)
            y_labels.append(10)
            NT_index.append(count)
    inhibition = np.array(inhibition).reshape(1,len(inhibition))

    # find scaled up acids
    selected_rows = df[df['Product Name'].isin(scaleup)]
    selected_Acid = list(set(selected_rows['Acid']))
    selected_index= [Acids.index(i) for i in selected_Acid]

    ############################# OUTTER LAYER #########################
    outer_track = sector.add_track((90, 100))
    outer_track.text(sector.name, size=14, color="white", fontweight='bold',adjust_rotation=True,orientation='vertical')
    outer_track.axis(fc='black')

    ############################# HEATMAP #########################
    track1 = sector.add_track((78, 88))
    scatter_track = sector.add_track((10, 70), r_pad_ratio=0.1)
    
    # make heatmap1
    track1.axis()
    track1.xticks_by_interval(16,outer=False,label_orientation='vertical',label_size=7)
    if sector.name == name_map[Amines[0]]:
        track1.yticks([0.5, 1.5, 2.5, 3.5], list("DCBA"), vmin=0, vmax=4, side='left', label_size=7)
    track1.heatmap(conversion, vmin=0, vmax=100, cmap="viridis")

    # highlight selected conditions
    position_map = {'A':(85.5,88), 'B':(83,85.5), 'C':(80.5,83), 'D':(78,80.5)}
    index_map = {'A':0,'B':1,'C':2,'D':3}
    cmap = plt.get_cmap("viridis")
    norm = plt.Normalize(vmin=0, vmax=100)
    for count,acid in enumerate(Acids):
        if acid in s_condition.keys():
            condition = s_condition[acid]
            color = cmap(norm(conversion[index_map[condition],count]))
            if acid not in selected_Acid:
                track1.rect(start=count, end=count+1, r_lim=position_map[condition], ec="black", lw=0.5, color=color)

    # highlight scaled-up conditions
    for count,acid in enumerate(Acids):
        if acid in s_condition.keys():
            condition = s_condition[acid]
            color = cmap(norm(conversion[index_map[condition],count]))
            if acid in selected_Acid:
                track1.rect(start=count, end=count+1, r_lim=position_map[condition], ec="black", lw=0.5, color=color)

    # make scatter plot
    cmap = plt.get_cmap("plasma")
    norm = plt.Normalize(vmin=-20, vmax=110)
    colors = [cmap(norm(inhibition[0,count])) if val != 10 else "grey" for count,val in enumerate(y_labels)]

    scatter_track.axis()
    labels = ['0.05','0.1','0.5','1','2','5','10','20', 'NB', 'BT', 'NT']
    if sector.name == name_map[Amines[-1]]:
        yticks = [i*1.1 for i in range(len(labels))]
        scatter_track.yticks(yticks, ['0.05','0.1','0.5','1','2','5','10','20', 'NB', 'BT', 'NT'], vmin=0, vmax=len(labels), side='right', label_size=7)

    # split into scaled-up and not scaled-up entries
    scaledup_index,scaledup_label = zip(*[(index,label) for index, label in enumerate(y_labels) if index in selected_index])

    # make scatter plots
    scatter_track.scatter(range(len(y_labels)), y_labels, vmin=0, vmax=len(labels)-1, c=colors, marker='o', s=30, alpha=0.5) 
    #scatter_track.scatter(scaledup_index, scaledup_label, vmin=0, vmax=len(labels)-1, c='none', marker='o', edgecolor='red', linewidth=.8, s=30)
    scatter_track.grid(y_grid_num=11)

circos.colorbar(bounds=(0.46, 0.92, 0.06, 0.01), vmin=0, vmax=100, orientation="horizontal",cmap="viridis")#,colorbar_kws=dict(label="Conversion / %"))
circos.colorbar(bounds=(0.475, 0.83, 0.06, 0.01), vmin=-90, vmax=110, orientation="horizontal",cmap="plasma")#,colorbar_kws=dict(label="Inhibition / %"))
circos.text(text="Conversion / %", r=93, deg=-0.6,fontsize=8)
circos.text(text="Inhibition / %", r=74, deg=1.5,fontsize=8)
circos.text(text=r"($\mu$M)", r=70, deg=-10.5,fontsize=7,adjust_rotation=True)
circos.rect((0,8),(0,360),fc='black')

# Create a black sphere using an Ellipse patch
#fig, ax = plt.subplots()
#sphere = patches.Circle((0.5, 0.5), radius=0.05, color='black')
#ax.add_patch(sphere)

#fig = circos.plotfig()
circos.plotfig()
#plt.show()
#exit()
plt.savefig('main.png',dpi=600) 
