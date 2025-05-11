import quandl
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
#import yfinance as yf


quandl_api_key = "Zkb2nfV4w28DPoJ5NhWs"

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt

def pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name, data_interval = '15min'):
    """
    Pull intraday time series data by stock ticker name.
    Args:
        alpha_vantage_api_key: Str. Alpha Vantage API key.
        ticker_name: Str. Ticker name that we want to pull.
        data_interval: String. Desired data interval for the data. Can be '1min', '5min', '15min', '30min', '60min'.
    Outputs:
        data: Dataframe. Time series data, including open, high, low, close, and datetime values.
        metadata: Dataframe. Metadata associated with the time series.
    """
    #Generate Alpha Vantage time series object
    ts = TimeSeries(key = alpha_vantage_api_key, output_format = 'pandas')
    #Retrieve the data for the past sixty days (outputsize = full)
    data, meta_data = ts.get_intraday(ticker_name, outputsize = 'full', interval= data_interval)
    data['date_time'] = data.index
    return data, meta_data

def plot_data(df, x_variable, y_variable, title):
    """
    Plot the x- and y- variables against each other, where the variables are columns in
    a pandas dataframe
    Args:
        df: Pandas dataframe, containing x_variable and y_variable columns.
        x_variable: String. Name of x-variable column
        y_variable: String. Name of y-variable column
        title: String. Desired title name in the plot.
    Outputs:
        Plot in the console.
    """
    fig, ax = plt.subplots()
    ax.plot_date(df[x_variable],
                 df[y_variable], marker='', linestyle='-', label=y_variable)
    fig.autofmt_xdate()
    plt.title(title)
    plt.show()


alpha_vantage_api_key = "U6GZ50UZM6E5TOFS"

#### EXECUTE IN MAIN FUNCTION ####
ts_data, ts_metadata = pull_intraday_time_series_alpha_vantage(alpha_vantage_api_key, ticker_name = "GOOGL")
#Plot the high prices
plot_data(df = ts_data,
          x_variable = "date_time",
          y_variable = "2. high",
          title ="High Values, Microsoft Stock, 15 Minute Data")





#Use the Quandl API to pull data
quandl.ApiConfig.api_key = quandl_api_key
data = quandl.get_table('WIKI/PRICES', ticker = ['MSFT'])
print(len(data))
plot_data(df = data,
          x_variable = "date",
          y_variable = "open",
          title ="Daily Microsoft Stock Prices, Open Price")
print(data)

# Calculate daily returns
data['Returns'] = data['close'].pct_change()

# Calculate autocorrelation
autocorr = data['Returns'].autocorr(lag=1)
print(f"Autocorrelation of daily returns: {autocorr}")



