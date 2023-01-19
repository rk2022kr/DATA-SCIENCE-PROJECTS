# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:15:16 2023

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
from sklearn.cluster import KMeans
from scipy.optimize import curve_fit
from sklearn import preprocessing
import itertools as iter


def read_and_filter_csv(file_name):
    """
    This function is used to read the csv file from the directory and to import
    the data for the Density clustering.

    file_name :- the name of the csv file with data.  
    """

    file_data = pd.read_csv(file_name)
    dataFr = pd.DataFrame(file_data)
    print(dataFr)
    dataFr = dataFr[['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011']]
    dataFr = dataFr.iloc[12:21]
    return file_data, dataFr




#pair plot comparing the two data
def pair_plot():
   
    data_frame_plot = pd.DataFrame()
    forest_area= []
    co2  = []
   
    for i in forest_data :
        forest_area.extend(forest_data[i])

    for i in co2Gas_data:
        co2.extend(co2Gas_data[i])

    data_frame_plot['forest_area'] = forest_area
    data_frame_plot['co2'] = co2

    type(data_frame_plot)

    sns.pairplot(data_frame_plot[['co2','forest_area']])

    '''function for finding K means clusttering'''
    kmeans1 = KMeans(n_clusters=3, random_state=0).fit(data_frame_plot[['forest_area','co2']])

    kmeans1.inertia_
    kmeans1.cluster_centers_

    data_frame_plot['cluster'] = kmeans1.labels_
   
   
    return data_frame_plot



def scatter_plot(data_k_plot):
   
    '''plot for K means clusttering before normalisation'''
    plt.figure()
    sns.scatterplot(x = 'co2', y = 'forest_area' , hue='cluster', data = data_k_plot)
    plt.title("K-Means before normalisation")
    plt.show()

    data_k = data_fr.drop(['cluster'], axis = 1)
    
    
    '''function called for clusttering'''
    
    
    names = ['co2','forets_area']
    a = preprocessing.normalize(data_k, axis=0)
    data_aft_k = pd.DataFrame(a,columns=names)
    kmeans2 = KMeans(n_clusters=3, random_state=0).fit(data_aft_k[['co2','forest_area']])
    kmeans2.inertia_
    kmeans2.cluster_centers_
    data_aft_k['cluster'] = kmeans2.labels_
    '''cluster shown along the data'''
    
    '''plot for K means clusttering after normalisation'''
    plt.figure()
    sns.scatterplot(x = 'co2', y = 'forest_area' , hue='cluster', data = data_aft_k)
    plt.title("K-Means after normalisation")
    plt.show()
    return


'''function to calculate the error limits'''

def func(x,a,b,c):
    return a * np.exp(-(x-b)**2 / c)


def err_ranges(x, func, param, sigma):
    """
    Calculates the upper and lower limits for the function, parameters and
    sigmas for single value or array x. Functions values are calculated for
    all combinations of +/- sigma and the minimum and maximum is determined.
    Can be used for all number of parameters and sigmas >=1.
   
    """
 
   
    # initiate arrays for lower and upper limits
    lower = func(x, *param)
    upper = lower
   
    uplow = []   # list to hold upper and lower limits for parameters
    for p,s in zip(param, sigma):
        pmin = p - s
        pmax = p + s
        uplow.append((pmin, pmax))
       
    pmix = list(iter.product(*uplow))
   
    for p in pmix:
        y = func(x, *p)
        lower = np.minimum(lower, y)
        upper = np.maximum(upper, y)
    return lower, upper



