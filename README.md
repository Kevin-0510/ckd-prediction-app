# Chronic Kidney Disease Prediction App

## Overview

This project is a Streamlit-based application for exploring patient records from a Chronic Kidney Disease (CKD) dataset.

The application provides an interactive interface for loading the CKD dataset, identifying individual patients using a Patient ID, and displaying patient-specific information. If a Patient ID column is not available in the dataset, the application automatically generates unique Patient IDs.

The project demonstrates the use of Python, Pandas, and Streamlit to build a simple interactive healthcare data application.

## Features

- Load CKD patient data from a CSV dataset.
- Automatically create Patient IDs when they are not present.
- Search and retrieve individual patient records using Patient ID.
- Display patient-specific information through an interactive Streamlit interface.
- Use cached data loading for efficient application performance.
- Provide a simple interface for exploring CKD patient records.

## Technology Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- NumPy

## Project Structure

```text
ckd-prediction-app/
│
├── ckd-dataset-v2.csv
├── ckd_streamlit.py
├── requirements.txt
└── README.md
