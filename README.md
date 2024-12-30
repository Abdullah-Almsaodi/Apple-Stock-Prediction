# Apple Stock Prediction

## Overview

This project focuses on predicting Apple Inc.'s stock prices using historical data. The primary objective is to preprocess the data, analyze trends, and develop predictive models using the closing prices. The project leverages **Python** and integrates tools for data visualization, analysis, and preparation for future machine learning models.

## Features

- Historical data collection from Yahoo Finance
- Data preprocessing, including handling missing values and formatting dates
- Visualization of trends in closing prices
- Analysis of key statistics, such as average, minimum, and maximum prices

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
   env\Scripts\activate       # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
apple-stock-prediction/
├── data/
│   ├── raw/                    # Raw dataset
│   │   └── AAPL_stock_data_1980_2024.csv
│   ├── processed/              # Processed dataset
│       └── AAPL_cleaned_data.csv
├── notebooks/                  # Jupyter notebooks for EDA, etc.
├── src/
│   ├── data_preprocessing.py   # Preprocessing script
├── .gitignore                  # Ignore unnecessary files
├── README.md                   # Project overview
├── requirements.txt            # Python dependencies
└── main.py                     # Entry script

```

## Usage

### 1. Preprocessing the Data

Run the `preprocess.py` script to clean and prepare the dataset:

```bash
python python main.py

```

This script:

- Loads the data from the `data/` directory
- Cleans missing values
- Formats the dates
- Saves the processed dataset back to `data/`

## Dependencies

- Python 3.8+
- Pandas
- Matplotlib

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
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
5. Create a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or collaboration:

- **Email**: Abdullah.Qaid@outlook.com
- **GitHub**: [Abdullah-Almsaodi](https://github.com/Abdullah-Almsaodi)
