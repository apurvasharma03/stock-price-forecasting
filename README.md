# stock-price-forecasting

This project analyzes and forecasts financial time series data using machine learning. It includes data acquisition via Quandl and Alpha Vantage APIs, autocorrelation and rolling average analysis, and predictive modeling using Linear Regression.

## Overview

The goal is to explore temporal relationships in stock prices (daily and intraday) and train machine learning models to predict future values. The workflow includes data collection, preprocessing, exploratory analysis, and model-based forecasting.

## Data Sources

- **Quandl API**: Historical daily data (e.g., AMZN, SPY)
- **Alpha Vantage API**: Intraday data (e.g., GOOGL, MSFT; 15–60 minute intervals)

## Project Structure

- `finance_ml.py`: Functions for pulling and plotting intraday time series data.
- `util.py`: Utilities for loading CSVs, plotting, computing returns, and scatter plotting.
- `linreg.py`, `linreg2.py`: Linear Regression forecasting using AMZN's adjusted close prices (1–60 day horizons).
- `test.py`, `test2.py`: Time series diagnostics (autocorrelation, rolling mean, exploratory plots).
- `dataA/`: Folder containing CSVs used for backtesting (e.g., GLD, SPY, TLT).

## Key Analyses

### 1. Autocorrelation & Temporal Structure

- Used `.autocorr()` to assess memory in SPY and TLT daily price series.
- Found higher autocorrelation at shorter lags, consistent with efficient market behavior.
- Used `plot_acf()` and scatter plots to visualize temporal dependencies.

### 2. Rolling Averages

- Calculated 7-day rolling means on GLD daily close prices.
- Visualized smoothing effects with `seaborn.lineplot()`.
- Helped isolate meaningful trends while reducing noise.

### 3. Forecasting with Linear Regression

- Used adjusted close data from AMZN.
- Shifted data 30–60 days ahead to create supervised labels.
- Scaled features and trained with `sklearn.linear_model.LinearRegression`.
- Achieved high R² values (up to ~98%) for short-term horizons.

## Execution Workflow

1. Load data from Quandl or Alpha Vantage via API keys or local CSVs.
2. Preprocess time series (e.g., shifting, scaling, slicing).
3. Analyze autocorrelation and apply rolling averages.
4. Train/test split and apply Linear Regression.
5. Visualize prediction performance using scatter and line plots.

## Key Takeaways

- Linear Regression performs strongly for short-term forecasting on stable stocks like AMZN.
- Autocorrelation and rolling averages help uncover temporal structure.
- Forecast accuracy declines as horizon increases (e.g., 60-day > 30-day).
- Feature scaling and clean label shifting are critical preprocessing steps.

## Future Work

- Add XGBoost for nonlinear regression and compare with linear models.
- Incorporate more features (volume, volatility, technical indicators).
- Automate model evaluation over multiple stocks and time intervals.
- Deploy trained models to generate weekly predictions on recent data.

---

This project is implemented in Python 3 using `pandas`, `quandl`, `scikit-learn`, `statsmodels`, and `matplotlib`. All data and code are for educational and non-commercial use only.
