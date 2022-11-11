# -*- coding: utf-8 -*-
"""
Program to get the visualisation of average death rate for various diseases 
over the years from 1990 to 2019. 
"""

import pandas as pd
import matplotlib.pyplot as plt
 
x = []
y = []
result = []

dataframe = pd.read_csv('data.csv')

#Function to process the dataframe and return the required data for visualisation
def processing(data):
   
    x = data.columns[3:]

    for row in x:
        y.append(data[row].mean())
     
    initial_data = {
                'diseases': x,
                'death': y
               }
   
    result = pd.DataFrame(initial_data, columns = ['diseases', 'death'])
   
    sorted_result=result.sort_values(by=['death'], ascending=False)
   
    y_axis=sorted_result['death'].head(10)
   
    x_axis=sorted_result['diseases'].head(10)
   
    return x_axis,y_axis

#Calling function processing
x_axis,y_axis=processing(dataframe)


plt.title('Percentage of death rate caused by diseases in world wide( 1990 - 2019 )')
plt.pie(y_axis, labels = x_axis,autopct='%.0f%%')
plt.legend(title="Diseases" ,loc='upper center', bbox_to_anchor=(2.3,1), ncol=2)
plt.show()




