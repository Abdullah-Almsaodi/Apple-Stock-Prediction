from src.data_preprocessing import load_data, clean_data, save_cleaned_data
import matplotlib.pyplot as plt

# File paths
RAW_FILEPATH = "data/raw/AAPL_stock_data_1980_2024.csv"
PROCESSED_FILEPATH = "data/processed/AAPL_cleaned_data.csv"

def main():
    print("Loading data...")
    stock_data = load_data(RAW_FILEPATH)

    print("Cleaning data...")
    cleaned_data = clean_data(stock_data)

    print("Saving cleaned data...")
    save_cleaned_data(cleaned_data, PROCESSED_FILEPATH)

    # Visualization
    print("Visualizing cleaned data...")
    plt.figure(figsize=(15, 8))
    plt.plot(cleaned_data['Date'], cleaned_data['Close'], linewidth=2, color='blue')
    plt.title('AAPL Historical Closing Prices', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('Closing Price ($)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
