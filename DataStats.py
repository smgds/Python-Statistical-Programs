# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes
PROGRAMMING ASSIGNMENT #5
'''
# =============================================================================
print("\n")
print("CPSC-51100, Summer II 2019", "NAME: Amy Noyes", \
      "PROGRAMMING ASSIGNMENT #5", sep="\n")
      
print("\n")

import pandas as pd
import re

def main():
    # Import data and load into dataframe
    school_data = pd.read_csv("cps.csv")
    
    # Split column Grades_Offered_All and add Lowest_Grade_Offered column
    split_grade = school_data["Grades_Offered_All"].str.split(",", n = 1, expand = True) 
    school_data["Lowest_Grade_Offered"]= split_grade[0]
    
    # Split column Grades_Offered_All and add Highest_Grade_Offered column
    split_grades = school_data["Grades_Offered_All"].str.rsplit(",", n = 1, expand = True)
    school_data["Highest_Grade_Offered"]= split_grades[1]
    
    # Get starting hours for all schools
    def start_hour(row):
        sh = str(row['School_Hours'])
        if sh == 'nan':
            return sh
        else:   
            time_text = re.search('[0-9]:[0-9][0-9]', sh)  #Finds strings like "H:MM"
            if time_text:
                hour = time_text.group(0)[0] #Get the first letter of the first matching expression   
                return hour
            else:
                loose_text = re.search('[0-9] *[aA] *[mM] *-', sh)
                hour = loose_text.group(0)[0] #Get the first letter of the first matching expression   
                return hour
    # Add School_Start_Hour to dataframe
    school_data['School_Start_Hour'] = school_data.apply(lambda row: start_hour(row), axis=1)
 
    # Replace missing numeric values with mean
    school_data['College_Enrollment_Rate_School'].fillna((school_data['College_Enrollment_Rate_School'].mean()), inplace=True)
    pd.set_option('display.max_columns', None)
    
    # Dataframe with select columns       
    data = school_data[['School_ID', 'Short_Name', 'Is_High_School', 'Zip',\
                        'Student_Count_Total', 'College_Enrollment_Rate_School',\
                        'Lowest_Grade_Offered', 'Highest_Grade_Offered', 'School_Start_Hour']]
    
    # Display the first 10 rows
    print(data.head(10).to_string(index=False,))
    
    # Displays mean and standard deviation of College Enrollment Rate for High Schools
    mean = school_data.loc[school_data["Is_High_School"] == 1]["College_Enrollment_Rate_School"].mean()
    stdv = school_data.loc[school_data["Is_High_School"] == 1]["College_Enrollment_Rate_School"].std()
    print("\nCollege Enrollment Rate for High Schools = {:.2f} (sd={:.2f})".format(mean,stdv))
    
    # Displays mean and standard deviation of Student_Count_Total for non-High Schools
    mean_count = school_data.loc[school_data["Is_High_School"] == 0]["Student_Count_Total"].mean()
    stdv_count = school_data.loc[school_data["Is_High_School"] == 0]["Student_Count_Total"].std()
    print("\nTotal Student Count for non-High Schools = {:.2f} (sd={:.2f}) \n".format(mean_count,stdv_count))
    
    # Distribution of starting hours for all schools
    print("Distribution of Starting Hours")
    distrib = data.groupby('School_Start_Hour').size().sort_values(ascending=False)
    for time, value in distrib.iteritems():
        if time != 'nan':    
            print(time+'am:', value)
        
    # Number of schools outside of loop neighborhood     
    loop = [60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]
    outside_loop = len([item for item in school_data["Zip"] if item not in loop])
    print("\nNumber of schools outside the Loop: {:d}".format(outside_loop))

main()