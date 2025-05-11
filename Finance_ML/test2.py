from sys import displayhook
from tkinter.tix import DisplayStyle
import pandas as pd
from util import get_data
from util import get_data2
from util import compute_daily_returns
from util import plot_scatter
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt2
import numpy as np
#from finance_ml import pull_intraday_time_series_alpha_vantage

dates = pd.date_range('2021-01-01', '2021-12-31')

alpha_vantage_api_key = "U6GZ50UZM6E5TOFS"

symbol = ['SPY']
df = get_data(symbol, dates, path="dataA")
data = df.iloc[:,0]
SPY = [data.head(1).autocorr(), data.head(2).autocorr(), data.head(3).autocorr(), data.head(5).autocorr(),
       data.head(3).autocorr(), data.head(365).autocorr()]
for num in SPY:
    print("SPY: " + str(num))
interval = [1, 2, 3, 5, 30, 365]
plt.scatter(interval, SPY)

symbol2 = ['TLT']
df2 = get_data(symbol2, dates, path="dataA")
data2= df2.iloc[:,0]
AAPL = [data2.head(1).autocorr(), data2.head(0).autocorr(), data2.head(3).autocorr(), data2.head(5).autocorr(),
       data2.head(3).autocorr(), data2.head(365).autocorr()]
for x in AAPL:
    print("AAPL: " + str(x))
plt.scatter(interval, AAPL)

plt.show()



# import the libraries 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# import the dataset 
data = pd.read_csv("./dataA/GLD.csv") 

#view the dataset 
displayhook( data.head()) 

# set figure size 
plt.figure( figsize = ( 12, 5)) 

# plot a simple time series plot 
# using seaborn.lineplot() 
sns.lineplot( x = 'Date', 
			y = 'Close', 
			data = data, 
			label = 'Rolling Mean for GLD') 

plt.xlabel( 'Days') 

# setting customized ticklabels for x axis 
"""
pos = [ '1959-01-01', '1959-02-01', '1959-03-01', '1959-04-01', 
	'1959-05-01', '1959-06-01', '1959-07-01', '1959-08-01', 
	'1959-09-01', '1959-10-01', '1959-11-01', '1959-12-01'] 

lab = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 
	'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'] 

plt.xticks( pos, lab) 
"""
plt.ylabel('Closing Price') 

# computing a 7 day rolling average 
data[ '7day_rolling_avg' ] = data.Close.rolling( 7).mean() 

# viewing the dataset 
displayhook(data.head(10)) 

# set figure size 
plt.figure( figsize = ( 12, 5)) 



# plot a simple time series plot 
# using seaborn.lineplot() 
sns.lineplot( x = 'Date', 
			y = 'Close', 
			data = data, 
			label = 'Closing Price') 

# plot using rolling average 
sns.lineplot( x = 'Date', 
			y = '7day_rolling_avg', 
			data = data, 
			label = 'Rolling Mean') 

plt.xlabel('Days') 

# setting customized ticklabels for x axis 
"""
pos = [ '1959-01-01', '1959-02-01', '1959-03-01', '1959-04-01', 
	'1959-05-01', '1959-06-01', '1959-07-01', '1959-08-01', 
	'1959-09-01', '1959-10-01', '1959-11-01', '1959-12-01'] 
"""
lab = [ '2021-01-04','2021-03-04','2021-05-04','2021-11-04','2021-12-30'] 

plt.xticks(lab) 

plt.ylabel('Closing Price') 

plt.title ("Closing Price of GLD over Time")

plt.show()


"""
symbol3 = ['GOOGL']
dates2 = [pd.date_range('2023-11-10', '2023-11-13')]
df3 = get_data2(symbol3, dates2, path= "dataA")
data3= df3.iloc[:,0]
print(data3)
GOOGL = [data3.head(1).autocorr(), data3.head(0).autocorr(), data3.head(3).autocorr(), data3.head(5).autocorr(),
       data3.head(3).autocorr(), data3.head(365).autocorr()]
for y in GOOGL:
    print("GOOGL: " + str(y))
interval2 = [15, 30, 45, 90]
plt2.scatter(interval2, GOOGL)

plt2.show()
"""
"""
ts_data, ts_metadata = pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name = "GOOGL")
GOOGL_csv_data = ts_data.to_csv('GOOGL.csv', index = True) 
print('\nCSV String:\n', GOOGL_csv_data) 
"""





