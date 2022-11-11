
# -*- coding: utf-8 -*-
"""
Program to get the visualisation of average death rate for various diseases 
over the years from 1990 to 2019.

"""

import pandas as pd
import matplotlib.pyplot as plt

diseases = []
years = []
result =[]

dataframe = pd.read_csv('data.csv')


#Function to process the dataframe and return the required data for visualisation
def processing(data):   
    diseases = data.columns[3:]
       
    years = data.Year.unique()
   
    for year in years:
        for disease in diseases:
            death = data.loc[data['Year'] == year, disease].mean()
            result.append((disease,year,death))
   
    results = pd.DataFrame(result, columns = ['diseases','years','death'])
   
    sorted_results=results.sort_values(by=['death'], ascending=False)
     
    return sorted_results

#Calling function processing
data_set = processing(dataframe)
set1 = data_set[data_set['diseases'] =='Cardiovascular Diseases']
set2 = data_set[data_set['diseases'] =='Neoplasms']
set3 = data_set[data_set['diseases'] =='Chronic Respiratory Diseases']
set4 = data_set[data_set['diseases'] =='Lower Respiratory Infections']
set5= data_set[data_set['diseases'] =='Neonatal Disorders']
set6 = data_set[data_set['diseases'] =='Diarrheal Diseases']
set7 = data_set[data_set['diseases'] =='Digestive Diseases']
set8 = data_set[data_set['diseases'] =='Tuberculosis']
set9 = data_set[data_set['diseases'] =='Cirrhosis and Other Chronic Liver Diseases']
set10 = data_set[data_set['diseases'] =='HIV/AIDS']

plt.xlabel('Year')
plt.ylabel('Average Death Rate')
plt.title('Average death rate caused by diseases all over the world ( 1990 - 2019 )')

plt.plot(set1['years'], set1['death'], label = "Cardiovascular Diseases")
plt.plot(set2['years'], set2['death'], label = "Neoplasms")
plt.plot(set3['years'], set3['death'], label = "Chronic Respiratory Diseases")
plt.plot(set4['years'], set3['death'], label = "Lower Respiratory Infections")
plt.plot(set5['years'], set3['death'], label = "Neonatal Disorders")
plt.plot(set6['years'], set3['death'], label = "Diarrheal Diseases")
plt.plot(set7['years'], set3['death'], label = "Digestive Diseases")
plt.plot(set8['years'], set3['death'], label = "Tuberculosis")
plt.plot(set9['years'], set3['death'], label = "Cirrhosis and Other Chronic Liver Diseases")
plt.plot(set10['years'], set3['death'], label = "HIV/AIDS")

plt.legend(title="Diseases", loc='upper left',bbox_to_anchor=(1,1)) 
plt.show()

