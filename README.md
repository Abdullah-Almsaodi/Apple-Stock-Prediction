# Apple Stock Prediction

## Overview

This project focuses on predicting Apple Inc.'s stock prices using historical data. The objective is to preprocess the data, analyze trends, engineer features, and build predictive models. The project leverages **Python** and integrates tools for data exploration, visualization, and machine learning.

## Features

- Collection and preprocessing of Apple stock data
- Exploratory Data Analysis (EDA) with visualizations
- Feature engineering for improved predictive accuracy
- Training and evaluation of machine learning models
- Prediction of future stock prices
- Modular, reusable scripts for data processing, visualization, and model training

## Prerequisites

- `Python 3.9 or 3.10` is recommended for compatibility with the listed dependencies.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Abdullah-Almsaodi/apple-stock-prediction.git
   cd apple-stock-prediction
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate      # On macOS/Linux
   env\Scripts\activate         # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```plaintext
apple-stock-prediction/
├── data/
│   ├── raw/                         # Raw historical data
│   │   └── AAPL_stock_data_1980_2024.csv
│   ├── processed/                   # Cleaned and transformed data
│       └── AAPL_cleaned_data.csv
├── notebooks/
│   ├── data_exploration.ipynb       # Notebook for Exploratory Data Analysis
│   ├── model_training.ipynb         # Notebook for model training
│   └── prediction_analysis.ipynb    # Notebook for predictions and evaluation
├── models/
│   └── stock_model.pkl              # Trained model file
├── src/
│   ├── __init__.py                  # Makes `src` a package
│   ├── data_preprocessing.py        # Functions for cleaning and preparing data
│   ├── feature_engineering.py       # Functions for creating features
│   ├── model_training.py            # Functions for training and evaluating models
│   └── prediction.py                # Functions for making predictions
├── tests/
│   └── test_data_processing.py      # Unit tests for preprocessing functions
├── utils/
│   ├── file_io.py                   # Functions for reading/writing files
│   └── visualization.py             # Functions for plotting data
├── .gitignore                       # Files and folders to ignore in Git
├── README.md                        # Project overview and instructions
├── requirements.txt                 # Python dependencies
├── main.py                          # Main script to run the pipeline
└── LICENSE                          # License for the project
```

## Usage

### 1. Data Preprocessing

Run the `data_preprocessing.py` script to clean and prepare the dataset:

```bash
python src/data_preprocessing.py
```

### 2. Exploratory Data Analysis

Explore the data trends and visualize key metrics using the `data_exploration.ipynb` notebook:

```bash
jupyter notebook notebooks/data_exploration.ipynb
```

### 3. Train the Model

Train the predictive model using the `model_training.py` script:

```bash
python src/model_training.py
```

### 4. Make Predictions

Generate stock price predictions using the trained model:

```bash
python src/prediction.py
```

## Dependencies

The project requires the following Python packages:

- pandas==1.5.3
- numpy==1.23.5
- matplotlib==3.6.2
- seaborn==0.12.2
- scikit-learn==1.1.3
- joblib==1.2.0
- yfinance==0.2.12

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: add your feature"
   ```
4. Push the changes:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or collaboration:

- **Email**: Abdullah.Qaid@outlook.com
- **GitHub**: [Abdullah-Almsaodi](https://github.com/Abdullah-Almsaodi)
