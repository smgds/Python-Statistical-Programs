# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes, Seth Gory, Christina Morgenstern
PROGRAMMING ASSIGNMENT #6
'''
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():

    # Load PUMS dataset into dataframe
    pums = pd.read_csv('ss13hil.csv')
    df = pd.DataFrame(pums)
    # Create figure with 2x2 subplots
    fig = plt.figure(figsize=(11, 8.5))
    
    # Pie chart containing the number of household records for different values of the HHL (household language) attribute
    def pie(ax):
        hhl = df['HHL'].value_counts()
        languages = ['English only','Spanish','Other Indo-European','Asian and Pacific Island languages','Other']
        ax.pie(hhl,startangle=242)
        ax.set_title('Household Languages',fontsize=8)
        ax.legend(languages,prop={'size':8},bbox_to_anchor=(0.285,0.85),loc='center right',bbox_transform=fig.transFigure)
        ax.axis('equal')
            
    # Histogram of HINCP (household income) with KDE plot superimposed.
    def hist(ax):
        hincp = df['HINCP']
        hincp.plot(kind='kde',color='k',ls='dashed')
        logspace = np.logspace(1,7,num=100,base=10.0)
        ax.hist(hincp,bins=logspace,facecolor='g',alpha=0.5,histtype='bar', density=True)
        ax.set_title('Distribution of Household Income',fontsize=8)
        ax.set_xlabel('Household Income($)- Log Scaled',fontsize=8)
        ax.set_ylabel('Density',fontsize=8)
        ax.set_xscale("log")
        ax.set_axisbelow(True)
                
    # Bar chart of Thousands of Households for each VEH (vehicles available) value 
    def bar(ax):
        grouped = df.groupby('VEH')['WGTP'].sum()/1000
        ax.bar(grouped.index,grouped.values,width=0.9,bottom=None,color='r',align='center')
        ax.set_title('Vehicles Available in Households',fontsize=8)
        ax.set_xlabel('# of Vehicles',fontsize=8)
        ax.set_ylabel('Thousands of Households',fontsize=8)
        ax.set_xticks(grouped.index)
                
    # Scatter plot of TAXP (property taxes) vs. VALP (property value)
    def scatter(ax):
        taxp = df['TAXP']
        tax_amount = convert_taxp(taxp)
        valp = df['VALP']
        ax.set_ylim([0, 11000])
        ax.set_xlim([0, 1200000])
        mappable = ax.scatter(valp,tax_amount,s=df.WGTP/2,c=df.MRGP,cmap='seismic',alpha=0.2,marker = 'o')
        cbar = fig.colorbar(mappable, ax=ax)
        cbar.ax.tick_params(labelsize=8)
        cbar.set_label('First Mortgage Payment (Monthly $)',fontsize=8)
        ax.set_title('Property Taxes vs Property Values',fontsize=8)
        ax.set_ylabel('Taxes($)',fontsize=8)
        ax.set_xlabel('Property Value($)',fontsize=8)
        ax.tick_params(axis='both', which='major', labelsize=8)
            
    # convert TAXP into the appropriate numeric value using the lower bound of the interval
    # (0=0, 2 = 1, 3-23 = 50, 24-63 = 100, 64-69 = 1000)
    def get_taxp_dict():
        taxp_dict = {}
        taxp_dict[1] = np.NaN
        taxp_dict[2] = 1
        taxp_dict[63]=5500
        counter = 50
        for key in range (3,23):
            taxp_dict[key]=counter
            counter += 50
        for key in range (23,63):
            taxp_dict[key] = counter+50
            counter += 100
        counter = counter - 50
        for key in range (64,69):
            taxp_dict[key] = counter+1000
            counter += 1000
        return taxp_dict
    
    # Convert TAXP using dict
    def convert_taxp(taxp):
        tax_amount = []
        taxp_dict = get_taxp_dict()
        for i in taxp:
            if i in taxp:
                tax_amount.append(taxp_dict[i])
            else:
                tax_amount.append(np.NaN)
        return tax_amount
       
    #Draw pie chart, histogram, bar chart, and scatter plot
    ax1 = fig.add_subplot(2,2,1)
    ax1.tick_params(axis='both', which='major', labelsize=8)
    ax1.tick_params(axis='both', which='minor', labelsize=8)
    pie(ax1)
    
    ax2 = fig.add_subplot(2,2,2)
    hist(ax2)
    ax2.tick_params(axis='both', which='major', labelsize=8)
    ax2.tick_params(axis='both', which='minor', labelsize=8)
    
    ax3 = fig.add_subplot(2,2,3)
    bar(ax3)
    ax3.tick_params(axis='both', which='major', labelsize=8)
    ax3.tick_params(axis='both', which='minor', labelsize=8)
    
    ax4 = fig.add_subplot(2,2,4)
    scatter(ax4)
    ax4.tick_params(axis='both', which='major', labelsize=8)
    ax4.tick_params(axis='both', which='minor', labelsize=8)
    
    # Display the figure and save it in a file called ‘pums.png
    fig.tight_layout()
    plt.show()
    fig.savefig('pums.png',dpi=400)

main()    
