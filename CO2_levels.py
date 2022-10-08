#Import packages here
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#CO2 data here
URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt"
   
#Convert page to text
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Save as a txt
with open('co2-data.txt', 'w') as f:
   f.write(soup.prettify())
   f.close()

#Open text and remove unnecessary lines
with open('co2-data.txt', 'r+') as f:
    # read an store all lines into list
    lines = f.readlines()
    key_data = lines[54:]
    f.close()

#Empty array
final_data = []

#Split array data
for i in key_data:
    final_data.append((str(i).split()))

#Convert to dataframe and keep only necessary columns and maintain floats
final_CO2_data =  pd.DataFrame(final_data, columns = ['Year','Month','Normalised Year','Monthly Average','De-seasonalised Monthly Average','#Days','Std. of Days','Uncertainty'])
final_CO2_data.drop(['Year','Month','De-seasonalised Monthly Average','#Days','Std. of Days','Uncertainty'], axis=1, inplace=True)
final_CO2_data['Monthly Average'] = final_CO2_data['Monthly Average'].astype(float)
final_CO2_data['Normalised Year'] = final_CO2_data['Normalised Year'].astype(float)

#Convert data to numpy
year = final_CO2_data.iloc[:,0].values.reshape(-1,1)
average = final_CO2_data.iloc[:,1].values.reshape(-1,1)

#Conduct linear regression (the plot is relatively linear already)
regression = LinearRegression()
regression.fit(year,average)
average_prediction = regression.predict(year)

#Collect and display the regression results
fit = "fit = " + str(np.round(regression.score(year, average_prediction),decimals=1)) + " \n"
m = "gradient = " + str(np.round(*regression.coef_[0],decimals=4)) + " \n"
b = "y-intercept = " + str(np.round(*regression.intercept_,decimals=4))
regression_results = fit + m + b

#Plot the data
final_CO2_data.plot(kind='scatter',x='Normalised Year',xlabel='Year',y='Monthly Average',ylabel='$CO_2$ concentration (ppm)',s=2.5, c='b', marker='o')
plt.plot(year, average_prediction, color='red')
plt.figtext(0.25,0.75,regression_results)
plt.show()