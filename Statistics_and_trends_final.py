# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:36:31 2023

@author: HP
"""

#importing the required packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics


file_name = 'world_bank_data.csv'

# Function to process the datas in csv file
def process_data(data_in):
   
    """
    function to read the file and to process the data
    data_in - name of the dataframe for processing.
   
    """
    datas = pd.read_csv(data_in,on_bad_lines='skip',skiprows=4)
    df_countries = datas["Country Name"].unique()
    df_years = datas.columns[4:]
   
    return df_countries,df_years,datas

# function definition for graphical analysis and visualisation of Methane emissions (kt of CO2 equivalent)
def methane_analysis(data):
   
    """
    this function produces line graphs plotting the Methane emissions across the world(1990-2020)
    with Methane emissions and year in the x and y-axis respectively.
    data:- name of the dataframe.
    """
   
    fetch_data=[]
    years=[]
    countries=[]

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_data.append(data[year][(data['Indicator Name'] == 'Methane emissions (kt of CO2 equivalent)') & (data['Country Name']==country)].to_string(index=False))

    initial_data = {
                'Year': years,
                'Country': countries,
                'Methane emissions (kt of CO2 equivalent)':fetch_data
                   }

    fetch_data = pd.DataFrame(initial_data, columns = ['Year','Country','Methane emissions (kt of CO2 equivalent)'])
       
    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]
   

    for year in years_choosen:
        data1.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Bangladesh') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data2.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Brazil') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data3.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Canada') & (fetch_data['Year']==year)].to_string(index=False)))


    for year in years_choosen:
        data4.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Ecuador') & (fetch_data['Year']==year)].to_string(index=False)))


    for year in years_choosen:
        data5.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='India') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data6.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Nigeria') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data7.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='South Africa') & (fetch_data['Year']==year)].to_string(index=False)))

   
       
    # Setting the width and height for the plot - width:8, height:8
    plt.figure(figsize=(8,8))

    plt.plot(years_choosen, data1, label = "Bangladesh")
    plt.plot(years_choosen, data2, label = "Brazil")
    plt.plot(years_choosen, data3, label = "Canada")
    plt.plot(years_choosen, data4, label = "Ecuador")
    plt.plot(years_choosen, data5, label = "India")
    plt.plot(years_choosen, data6, label = "Nigeria")
    plt.plot(years_choosen, data7, label = "South Africa")

    # naming the x axis
    plt.xlabel('Year')

    # naming the y axis
    plt.ylabel('Methane emissions (kt of CO2 equivalent)')

    # giving a title to the plot
    plt.title('Methane emissions across the world (1990 - 2020)')
     
    # show a legend on the plot
    plt.legend(title="Year", loc='upper left',bbox_to_anchor=(1,1))
     
    # function to show the plot
    plt.show()
    return

# function definition for graphical analysis and visualisation of CO2 emissions (kt)
def co2_analysis(data):
   
    """
    this function produces multiple barchart plotting the CO2 emissions around the world(1990-2020)
    with CO2 emissions and Country in the x and y-axis respectively.
    data:- name of the dataframe.
    """

    fetch_data=[]
    years=[]
    countries=[]

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_data.append(data[year][(data['Indicator Name'] == 'CO2 emissions (kt)') & (data['Country Name']==country)].to_string(index=False))

    initial_data = {
                'Year': years,
                'Country': countries,
                'CO2 emissions (kt)':fetch_data
               }

    fetch_data = pd.DataFrame(initial_data, columns = ['Year','Country','CO2 emissions (kt)'])
       
    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]

    for country in countries_choosen:
        data1.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='1990')].to_string(index=False)))

    for country in countries_choosen:
        data2.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='1995')].to_string(index=False)))

    for country in countries_choosen:
        data3.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2000')].to_string(index=False)))

    for country in countries_choosen:
        data4.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2005')].to_string(index=False)))

    for country in countries_choosen:
        data5.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2010')].to_string(index=False)))

    for country in countries_choosen:
        data6.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2015')].to_string(index=False)))

    for country in countries_choosen:
        data7.append(float(fetch_data['CO2 emissions (kt)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2020')].to_string(index=False)))
               
    width=0.1
    values=np.arange(len(countries_choosen))

    # Setting the width and height for the plot - width:8, height:8
    plt.figure(figsize=(8,8))

    plt.bar(values,data1,width,label='1990', )
    plt.bar(values+width,data2,width,label='1995')
    plt.bar(values+width*2,data3,width,label='2000')
    plt.bar(values+width*3,data4,width,label='2005')
    plt.bar(values+width*4,data5,width,label='2010')
    plt.bar(values+width*5,data6,width,label='2015')
    plt.bar(values+width*6,data7,width,label='2020')


    # naming the x axis
    plt.xlabel('Country')

    # naming the y axis
    plt.ylabel('CO2 emissions (kt)')

    # giving a title to the plot
    plt.title('CO2 emissions around the world (1990 - 2020)')

    # show a legend on the plot
    plt.legend(title="Year", loc='upper left',bbox_to_anchor=(1,1))

    plt.xticks(values+.3,countries_choosen,rotation = 90)

    # function to show the plot
    plt.show()
    return

# function definition for graphical analysis and visualisation of Forest area (% of land area)
def forest_analysis(data):
   
    """
    this function produces line chart plotting the average forest area across the world(1990-2020)
    with Average forest area and Country in the x and y-axis respectively.
    data:- name of the dataframe.
    """

    fetch_data=[]
    years=[]
    countries=[]

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_data.append(data[year][(data['Indicator Name'] == 'Forest area (% of land area)') & (data['Country Name']==country)].to_string(index=False))

    initial_data = {
                'Year': years,
                'Country': countries,
                'Forest area (% of land area)':fetch_data
               }

    fetch_data = pd.DataFrame(initial_data, columns = ['Year','Country','Forest area (% of land area)'])

    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]

    for year in years_choosen:
        data1.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='Bangladesh') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data2.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='Brazil') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data3.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='Canada') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data4.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='Ecuador') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data5.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='India') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data6.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='Nigeria') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data7.append(float(fetch_data['Forest area (% of land area)'][(fetch_data['Country']=='South Africa') & (fetch_data['Year']==year)].to_string(index=False)))
       
    # Setting the width and height for the plot - width:8, height:8
    plt.figure(figsize=(8,8))
   
    average_forest_area=[]
    average_forest_area.append(statistics.mean(data1))
    average_forest_area.append(statistics.mean(data2))
    average_forest_area.append(statistics.mean(data3))
    average_forest_area.append(statistics.mean(data4))
    average_forest_area.append(statistics.mean(data5))
    average_forest_area.append(statistics.mean(data6))
    average_forest_area.append(statistics.mean(data7))    
   
    plt.plot(countries_choosen,average_forest_area)
   
    # naming the x axis
    plt.xlabel('Countries')

    # naming the y axis
    plt.ylabel('Average Forest area (% of land area)')
   

    # giving a title to the plot
    plt.title('Average Forest area across the world (1990 - 2020)')
           
    # function to show the plot
    plt.show()
    return

# function definition for graphical analysis and visualisation of Population growth (annual %)
def population_analysis(data):
   
    """
    this function produces multiple bar chart plotting the Anual Population growth around the world(1990-2020)
    with Population growth and Country in the x and y-axis respectively.
    data:- name of the dataframe.
    """

    fetch_details=[]
    years=[]
    countries=[]

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_details.append(data[year][(data['Indicator Name'] == 'Population growth (annual %)') & (data['Country Name']==country)].to_string(index=False))

    initial_data = {
                'Year': years,
                'Country': countries,
                'Population growth (annual %)':fetch_details
               }

    fetch_data = pd.DataFrame(initial_data, columns = ['Year','Country','Population growth (annual %)'])
       
    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]

    for country in countries_choosen:
        data1.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='1990')].to_string(index=False)))

    for country in countries_choosen:
        data2.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='1995')].to_string(index=False)))

    for country in countries_choosen:
        data3.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2000')].to_string(index=False)))

    for country in countries_choosen:
        data4.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2005')].to_string(index=False)))

    for country in countries_choosen:
        data5.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2010')].to_string(index=False)))

    for country in countries_choosen:
        data6.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2015')].to_string(index=False)))

    for country in countries_choosen:
        data7.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country']==country) & (fetch_data['Year']=='2020')].to_string(index=False)))

       
    width=0.1
    values=np.arange(len(countries_choosen))

    # Setting the width and height for the plot - width:8, height:8
    plt.figure(figsize=(8,8))  

    plt.bar(values,data1,width,label='1990')
    plt.bar(values+width,data2,width,label='1995')
    plt.bar(values+width*2,data3,width,label='2000')
    plt.bar(values+width*3,data4,width,label='2005')
    plt.bar(values+width*4,data5,width,label='2010')
    plt.bar(values+width*5,data6,width,label='2015')
    plt.bar(values+width*6,data7,width,label='2020')

    # naming the x axis
    plt.xlabel('Country')

    # naming the y axis
    plt.ylabel('Population growth (annual %)')

    # giving a title to the plot
    plt.title('Annual Population Growth around the world (1990 - 2020)')

    # show a legend on the plot
    plt.legend(title="Year", loc='upper left',bbox_to_anchor=(1,1))

    plt.xticks(values+.3,countries_choosen,rotation = 90)

    # function to show the plot
    plt.show()

    return

# function definition for graphical analysis and visualisation of Total greenhouse gas emissions (% change from 1990)
def greenhouse_analysis(data):
   
    """
    this function produces line chart plotting the Total greenhouse gas emissions across the world(1990-2020)
    with Total greenhouse gas emissions and Year in the x and y-axis respectively.
    data:- name of the dataframe.
    """

    fetch_data=[]
    years=[]
    countries=[]

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_data.append(data[year][(data['Indicator Name'] == 'Total greenhouse gas emissions (% change from 1990)') & (data['Country Name']==country)].to_string(index=False))

    initial_data = {
                'Year': years,
                'Country': countries,
                'Total greenhouse gas emissions (% change from 1990)':fetch_data
               }

    fetch_data = pd.DataFrame(initial_data, columns = ['Year','Country','Total greenhouse gas emissions (% change from 1990)'])
       

    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]
   

    for year in years_choosen:
        data1.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='Bangladesh') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data2.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='Brazil') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data3.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='Canada') & (fetch_data['Year']==year)].to_string(index=False)))


    for year in years_choosen:
        data4.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='Ecuador') & (fetch_data['Year']==year)].to_string(index=False)))


    for year in years_choosen:
        data5.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='India') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data6.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='Nigeria') & (fetch_data['Year']==year)].to_string(index=False)))

    for year in years_choosen:
        data7.append(float(fetch_data['Total greenhouse gas emissions (% change from 1990)'][(fetch_data['Country']=='South Africa') & (fetch_data['Year']==year)].to_string(index=False)))


    # Setting the width and height for the plot - width:8, height:8
    plt.figure(figsize=(8,8))

               
    plt.plot(years_choosen, data1, label = "Bangladesh")
    plt.plot(years_choosen, data2, label = "Brazil")
    plt.plot(years_choosen, data3, label = "Canada")
    plt.plot(years_choosen, data4, label = "Ecuador")
    plt.plot(years_choosen, data5, label = "India")
    plt.plot(years_choosen, data6, label = "Nigeria")
    plt.plot(years_choosen, data7, label = "South Africa")


    # naming the x axis
    plt.xlabel('Year')

    # naming the y axis
    plt.ylabel('Total greenhouse gas emissions')

    # giving a title to the plot
    plt.title('Total greenhouse gas emissions across the world (1990 - 2020)')

    # show a legend on the plot
    plt.legend(title="Country", loc='upper left',bbox_to_anchor=(1,1))
     
    # function to show the plot
    plt.show()
       
    return


# Calling the function process_data
countries_list,years_list,datas=process_data(file_name)

#List of Years choosen for data visualization
years_choosen = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']


#List of Countries choosen for data visualization
countries_choosen = ['Bangladesh','Brazil','Canada','Ecuador','India','Nigeria','South Africa']

"""
Calling the defined function to plot the graphs for graphical analysis and visualisation

"""

# Calling the function for graphical analysis and visualisation of Methane emissions (kt of CO2 equivalent)
methane_analysis(datas)

# Calling the function for graphical analysis and visualisation of CO2 emissions (kt)
co2_analysis(datas)

# Calling the function for graphical analysis and visualisation of Forest area (% of land area)
forest_analysis(datas)

# Calling the function for graphical analysis and visualisation of Total greenhouse gas emissions (% change from 1990)
greenhouse_analysis(datas)

# Calling the function for graphical analysis and visualisation of Population growth (annual %)
population_analysis(datas)
