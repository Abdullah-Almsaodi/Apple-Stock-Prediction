from src.data_preprocessing import preprocess_data
# from src.model_training import train_model
# from src.prediction import predict_stock

# Main pipeline
if __name__ == "__main__":
    # Step 1: Preprocess data
    data = preprocess_data("data/raw/AAPL_stock_data_1980_2024.csv")

    # # Step 2: Train model
    # model = train_model(data)

    # # Step 3: Predict stock prices
    # predict_stock(model, "data/processed/AAPL_cleaned_data.csv")
