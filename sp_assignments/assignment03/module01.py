import pandas as pd
import requests
from sklearn import preprocessing


url = 'https://think.cs.vt.edu/corgis/datasets/csv/cars/cars.csv'

def download(url, filename):
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        open(filename, 'wb').write(response.content)

#download(url, 'cars.csv')

def prepareLinReg() :
    data = pd.read_csv('cars.csv', sep=',')


    #Reducer datasettet til Honda'er med benzinmotor
    data = data.fillna(0)
    data = data[(data['Identification.Make'] == 'Honda') & (data['Fuel Information.Fuel Type'] == 'Gasoline')]
    data = data[data['Fuel Information.Highway mpg'] < data['Fuel Information.Highway mpg'].quantile(0.90)]
    data = data[data['Engine Information.Engine Statistics.Horsepower'] < data['Engine Information.Engine Statistics.Horsepower'].quantile(0.90)]

    data = data[['Fuel Information.Highway mpg', 'Engine Information.Engine Statistics.Horsepower']]

    #Normaliser data til klargøring af lineær regression.
    data = preprocessing.normalize(data)
    
    #Hestekræfter
    xs = data[:,1]
    
    #Km pr liter
    ys = data[:,0]

    return xs, ys

