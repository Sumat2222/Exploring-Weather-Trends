#! python
# A simple program to compare and derive a statistical analysis of the average annual weather of Delhi and the World.

# Delhi data collected from wunderground datasets API
# India data collected from data.gov.in (OSD)
# Global weather data collected from _

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('Weather Analysis\localglobal-temp.csv') #Read CSV
dfmean = df.rolling(window=150, center=False, on="LOCALAVGT").mean().dropna() #Set a rolling window of 150 and drop NA values from dataset

x = dfmean.YEAR #Set x coord in dfmean (Year Values)
y = dfmean.LOCALAVGT #Set y coord in dfmeans (Delhi Temperature)
r = dfmean.GLOBALAVGT #Set r coord in dfmeans (Global temperature)

fig = plt.figure(figsize=(7,5)) # Change total size of the fig
 
plt.plot(x, y, color = 'red', linewidth = 2, label="Delhi") # Plot Delhi temperatures 
plt.plot(x,r, color='blue', linewidth=2, label="Global") # Plot global temperatures

plt.legend()
fig.suptitle('Average Temperature(°C) per Year')
plt.xlabel("Year", fontsize=14) 
plt.ylabel("Temperature (°C)", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.savefig('global-analysis.png')