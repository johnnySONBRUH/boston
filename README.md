# Boston Housing Price Predictor

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-app-red.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-model-orange.svg)

This is a Streamlit web application that predicts Boston housing prices based on various housing features using a pre-trained machine learning model (`predictor.pkl`).

## Model Performance
The Random Forest Regressor model achieved the following performance metrics on the test set:

| Metric | Value |
| :--- | :--- |
| R2 Score | 0.8811 |
| Mean Absolute Error (MAE) | 2.02 |
| Mean Squared Error (MSE) | 8.712 |
| Root Mean Squared Error (RMSE) | 2.951 |
| Mean Absolute Percentage Error (MAPE) | 0.1111 |

## Features
- Interactive web interface built with Streamlit.
- Predicts housing prices based on:
    - Crime Rate (CRIM)
    - Residential Land Zoned (ZN)
    - Non-Retail Business (INDUS)
    - Nitric Oxides (NOX)
    - Average Rooms (RM)
    - Age of houses (AGE)
    - Distance to Employment Centers (DIS)
    - Property Tax Rate (TAX)
    - Pupil-Teacher Ratio (PTRATIO)
    - % Lower Status (LSTAT)

## Prerequisites
- Python 3.x
- `requirements.txt` dependencies installed

## Installation
1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To launch the app, run the following command in your terminal:
```bash
streamlit run streamlit_app.py
```
This will start a local web server and open the app in your default browser.

---
Data source: [Boston Housing Dataset](https://www.kaggle.com/datasets/barkataliarbab/boston-housing-dataset-for-regression-modeling/data)
