import pandas as pd
import os

def load_data(filepath):
    """Load the dataset from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist.")
    data = pd.read_csv(filepath)
    return data

def clean_data(data):
    """Clean and preprocess the dataset."""
    # Convert Date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Drop rows with missing values
    data.dropna(inplace=True)
    
    # Ensure data is sorted by date
    data.sort_values(by='Date', inplace=True)
    
    return data

def save_cleaned_data(data, output_path):
    """Save the cleaned dataset to a CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
