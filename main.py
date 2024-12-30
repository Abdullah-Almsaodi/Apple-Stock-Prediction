from src.data_preprocessing import preprocess_data
from utils.visualization import plot_closing_prices

# File paths
RAW_FILEPATH = "data/raw/AAPL_stock_data_1980_2024.csv"
PROCESSED_FILEPATH = "data/processed/AAPL_cleaned_data.csv"

# Main pipeline
if __name__ == "__main__":
    # Step 1: Preprocess data
    cleaned_data = preprocess_data(RAW_FILEPATH, PROCESSED_FILEPATH)

    # Step 2: Visualize cleaned data
    plot_closing_prices(cleaned_data)
