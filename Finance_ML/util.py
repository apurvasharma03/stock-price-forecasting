""" Utility code."""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path( symbol, path="data" ):
    dir = path
    base_dir = os.path.join("", dir)
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def get_data(symbols, dates, addSPY=True, colname = 'Adj Close', path="data"):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if addSPY and 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols = ['SPY'] + symbols
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, path), index_col='Date',
                parse_dates=True, usecols=['Date', colname], na_values=['nan'])
        #print(df_temp.head(2))
        df_temp = df_temp.rename(columns={colname: symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
        #print(df.head(2))
    return df
def get_data2(symbols, dates, addSPY=True, path="data"):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, path), index_col='date',
                parse_dates=True, usecols=['date', colname], na_values=['nan'])
        #print(df_temp.head(2))
        df_temp = df_temp.rename(columns={colname: symbol})
        df = df.join(df_temp)
        
        #print(df.head(2))
    return df

def compute_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:] / df[:-1].values) - 1
	daily_returns.iloc[0, :] = 0  # set daily returns for row 0 to 0
	return daily_returns

def plot_scatter( daily_returns, SYMBOL_X, SYMBOL_Y ):
	# Scatter-plot Y vs X
	daily_returns.plot(kind='scatter', x=SYMBOL_X, y=SYMBOL_Y)

	# compute the equation of the (linear) model
	# degree of a linear polynomial is 1 - the third parameter
	linear_model = np.polyfit( daily_returns[SYMBOL_X], daily_returns[SYMBOL_Y], 1 )
	beta 	= linear_model[0]
	alpha 	= linear_model[1]

	print(f" beta of {SYMBOL_Y} = {beta:+.6f}")
	print(f"alpha of {SYMBOL_Y} = {alpha:+.6f}")

	# plot the line using the equation and SYMBOL_X as the independent variable
	plt.plot(daily_returns[SYMBOL_X], beta * daily_returns[SYMBOL_X] + alpha, '-', color='r',
			 label=f"Y = {beta:.2f}X + {alpha:.6f}")
	plt.plot(daily_returns[SYMBOL_X], beta * daily_returns[SYMBOL_X] + alpha, '-', color='r', label = f"Y = beta * X + alpha")
	plt.legend(loc = "upper left")
	#plt.legend(f"{daily_returns[SYMBOL_X], beta * daily_returns[SYMBOL_X] + alpha}")
	plt.show()
	return beta,alpha



