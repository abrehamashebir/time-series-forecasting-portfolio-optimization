def preprocess_data(data):
    for ticker in data.keys():
        df = data[ticker]
        
        # Keep relevant columns
        df = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']].dropna()
        
        # Compute daily returns
        df['Daily Return'] = df['Adj Close'].pct_change()
        
        # Rolling statistics (20-day moving average & volatility)
        df['Rolling Mean'] = df['Adj Close'].rolling(window=20).mean()
        df['Rolling Std'] = df['Adj Close'].rolling(window=20).std()
        
        # Fill missing values if any
        df.fillna(method='bfill', inplace=True)
        
        # Save cleaned data
        data[ticker] = df
    
    return data

