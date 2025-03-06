from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

def arima_forecast(data, ticker, steps=365):
    series = data[ticker]['Adj Close'].dropna()
    
    # Train ARIMA model
    model = ARIMA(series, order=(5,1,2))
    model_fit = model.fit()
    
    # Forecast future prices
    forecast = model_fit.forecast(steps=steps)
    
    # Plot actual vs forecast
    plt.figure(figsize=(12,6))
    plt.plot(series.index, series, label="Actual")
    plt.plot(pd.date_range(series.index[-1], periods=steps, freq='D'), forecast, label="Forecast", color='red')
    plt.legend()
    plt.title(f"{ticker} ARIMA Forecast")
    plt.show()
    
    return forecast

# Run ARIMA Forecast
arima_forecast(data, 'TSLA')
