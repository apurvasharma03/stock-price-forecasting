# 📈 Stock Price Forecasting

![Tech Stack](https://img.shields.io/badge/Built%20With-Python%2C%20Pandas%2C%20Scikit--Learn%2C%20Quandl%2C%20Alpha%20Vantage-blue)
![Last Commit](https://img.shields.io/github/last-commit/apurvasharma03/stock-price-forecasting)


This project analyzes and forecasts financial time series data using machine learning. It leverages APIs (Quandl, Alpha Vantage) for real-time and historical data, explores temporal patterns (autocorrelation, rolling averages), and applies **Linear Regression** models for short-term price prediction.

---

## 🎯 Project Goals

- Explore temporal relationships in stock prices (daily & intraday)
- Preprocess and visualize time series trends
- Forecast adjusted closing prices using machine learning
- Evaluate model accuracy across short (1–30 day) and medium (30–60 day) horizons

---

## 🗂️ Project Structure

```
stock-price-forecasting/
├── finance_ml.py         # Intraday data API functions and plotting
├── linreg.py, linreg2.py # Linear regression models (AMZN, multiple horizons)
├── test.py, test2.py     # Autocorrelation, rolling mean, and EDA scripts
├── util.py               # CSV loader, returns calculator, plotting utilities
├── dataA/                # CSV files (e.g., SPY, GLD, TLT) for backtesting
```

---

## 📡 Data Sources

- **Quandl API** – Historical daily OHLC data (e.g., AMZN, SPY)
- **Alpha Vantage API** – Intraday prices at 15–60 minute resolution (e.g., GOOGL, MSFT)
- **Local CSVs** – Supplemental data for model testing and exploration

---

## 🔍 Key Analyses

### 1. Autocorrelation & Temporal Memory

- Used `.autocorr()` and `statsmodels.plot_acf()` to examine short-term memory in SPY and TLT
- Observed higher autocorrelation at shorter lags, consistent with semi-efficient market behavior
- Scatter plots confirmed temporal dependencies

### 2. Rolling Averages

- Applied 7-day rolling mean on GLD daily close prices
- Visualized trend smoothing with `seaborn.lineplot()`
- Useful for identifying macro trends and suppressing noise

### 3. Linear Regression Forecasting

- Used adjusted close prices of AMZN for 30–60 day forward predictions
- Shifted prices to create supervised labels (`y = price_t+N`)
- Scaled features using `sklearn.preprocessing`
- Achieved high R² (~98%) on short-term windows

---

## ⚙️ Execution Workflow

1. **Data Loading**  
   - Fetch data using API keys or load local CSVs from `dataA/`

2. **Preprocessing**  
   - Feature scaling, shifting, and time-window slicing

3. **Exploratory Analysis**  
   - Autocorrelation checks and rolling average smoothing

4. **Model Training**  
   - Train/test split → `LinearRegression().fit(X_train, y_train)`

5. **Evaluation**  
   - Visualize predictions using scatter and line plots
   - Report R² and forecast deviation by horizon

---

## 💡 Key Insights

- **Linear Regression performs well** on stable, large-cap stocks for short-term forecasting
- **Autocorrelation and rolling averages** reveal valuable temporal structure
- **Forecast accuracy decreases** with increasing time horizon (60-day > 30-day)
- Proper preprocessing (shifting, scaling) is critical for effective modeling

---

## 🔮 Future Work

- Integrate **XGBoost** for nonlinear regression and benchmark vs. linear models
- Add **technical indicators** (e.g., MACD, RSI, volatility, volume)
- Automate batch model training across multiple stocks and intervals
- Deploy live forecasting to generate weekly predictions from API feeds

---

## 🛠 Technologies Used

- Python 3.8+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- statsmodels
- quandl, Alpha Vantage API

---

## 📎 Disclaimer

All data and code are for educational and non-commercial research purposes only. This project does **not** constitute financial advice.

---

## 📬 Contact

Questions or suggestions? Open an issue or contact the contributors.

