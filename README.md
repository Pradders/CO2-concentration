# CO2-concentration
A simple linear regression analysis of the global CO2 concentration (ppm) monthly since 1958.

The data itself was extracted from the National Oceanic and Atmospheric Administration, as re-distributed freely by NASA. See https://climate.nasa.gov/vital-signs/carbon-dioxide/.

Data found here: https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt

Packages used:
1. Beautiful Soup and Requests to extreact the data directly from online
2. Pandas to extract the relevant data and extract it to a numeric dataframe
3. Numpy and Scikit-learn for linear regressional analysis
4. Matplotlib for displaying the original plot and the linear regression

Scikit-learn utilised from here: https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d
