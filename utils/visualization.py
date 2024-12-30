import matplotlib.pyplot as plt

def plot_closing_prices(data, title="AAPL Historical Closing Prices"):
    """
    Plot the historical closing prices of the stock.

    Args:
        data (DataFrame): The cleaned stock data.
        title (str): Title for the plot.
    """
    print("Visualizing data...")
    plt.figure(figsize=(15, 8))
    plt.plot(data['Date'], data['Close'], linewidth=2, color='blue')
    plt.title(title, fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Closing Price ($)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
