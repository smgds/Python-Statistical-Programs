# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes
PROGRAMMING ASSIGNMENT #4
'''
# =============================================================================
print("\n")
print("CPSC-51100, Summer II 2019", "NAME: Amy Noyes", \
      "PROGRAMMING ASSIGNMENT #4", sep="\n")
      
print("\n")

# Computing conditional probabilities

import pandas as pd

def main():

    # Import data and load into dataframe
    cars_data = pd.read_csv("cars.csv")
    aspiration = cars_data["aspiration"]
    make = cars_data["make"]
    
    # Identify unique values for aspiration and make
    aspirations = pd.unique(aspiration)
    makes = pd.unique(make)
    
    for make in makes:
        combine_data = cars_data['aspiration'][cars_data['make'] == make]
        for aspiration in aspirations:
            # Iterate through aspiration column data and count the matches for each aspiration type
            count_asp = len([item for item in combine_data if item == aspiration])
            # Total matching make of each type          
            make_total = len(cars_data.loc[cars_data['make'].isin([make])]) 
            # Calculates the conditional probability and limits to two decimal places
            cond_prob = count_asp/make_total
            print("Prob(aspiration={0:s}|make={1:s}) = {2:.2f}%".format(aspiration, make, 100*cond_prob))
  
    print('\n')     
    
    for make in makes:
        # Calculates probability of each make and limits to two decimal places    
        combine_data = cars_data['aspiration'][cars_data['make'] == make]
        make_prob = len(combine_data)/len(cars_data)            
        print("Prob(make={0:s} = {1:.2f}%".format(make, 100*make_prob))
        
main()
  