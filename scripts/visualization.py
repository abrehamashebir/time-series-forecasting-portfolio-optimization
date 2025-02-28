import matplotlib.pyplot as plt
def plot_eda(data):
    plt.figure(figsize=(14,6))
    for ticker in data.keys():
        plt.plot(data[ticker].index, data[ticker]['Adj Close'], label=ticker)
    plt.legend()
    plt.title("Stock Prices Over Time")
    plt.show()

