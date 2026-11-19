# ⚡ Electricity Usage Predictor (PS No. 64)

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=flat)](https://matplotlib.org/)
[![Test Status](https://img.shields.io/badge/Tests-4%2F4%20Passing%20(100%25)-success?style=flat)]()

---

### **Academic Details**
* **Institution:** Rungta International Skills University
* **Department:** School of Computer Science and Engineering
* **Program:** Bachelor of Technology in Computer Science & Engineering (B.Tech CSE)
* **Semester / Section:** First Semester / Section - H
* **Course:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)
* **Problem Statement No.:** 64
* **Allocation Date:** 14th October 2026
* **Submission Date:** 16th November 2026

---

## 📖 Project Overview
The **Electricity Usage Predictor** is a scientific console application written in Python 3. It models historical monthly power consumption data using Simple Linear Regression via Ordinary Least Squares (`numpy.polyfit`), computes the goodness-of-fit statistic ($R^2$), predicts future monthly electricity demand, estimates the projected bill at ₹6.00/unit, and visualizes historical usage against the trendline using `matplotlib`.

---

## 🎯 Key Features
* **Data Ingestion & Sanitization:** Automatically detects CSV headers, parses numeric records, coerces unparseable values, and prunes missing data rows.
* **Ordinary Least Squares Regression:** Determines optimal slope ($m$) and intercept ($c$) using `numpy.polyfit(Month, Units, deg=1)`.
* **Reliability Metric ($R^2$):** Calculates the Coefficient of Determination to measure model accuracy.
* **Financial Forecasting:** Estimates total power expenditure at the standard tariff of **₹6.00 per unit**.
* **Interactive Visualization:** Plots actual data points, linear regression trend line, and future forecasted coordinates with annotations.
* **Full Test Automation:** Comes pre-packaged with an automated test suite verifying all 4 benchmark cases.

---

## 🗂️ Project Directory Structure
```text
Electricity_Usage_Predictor_PS64/
│
├── electricity_predictor.py    # Main application (interactive console & prediction engine)
├── test_runner.py              # Automated test suite (runs and asserts all 4 test cases)
├── usage.csv                   # Default dataset (Month vs Units)
│
├── testcase1_normal.csv        # Benchmark Test Case 1 data
├── testcase2_boundary.csv      # Benchmark Test Case 2 data (minimum 2 rows)
├── testcase3_invalid.csv       # Benchmark Test Case 3 data (single row error handling)
├── testcase4_scenario.csv      # Benchmark Test Case 4 data (R2 variance scenario)
│
├── usage_trend_plot.png        # Generated high-resolution Matplotlib trend chart
├── PROJECT_REPORT.md           # Formal Academic Project Report (Markdown)
├── PROJECT_REPORT.html         # Printable formatted HTML Project Report
├── requirements.txt            # Python dependencies (pandas, numpy, matplotlib)
├── run_project.bat             # 1-Click Windows batch launcher for the application
└── run_tests.bat               # 1-Click Windows batch launcher for the test runner
```

---

## 🚀 Quick Start Guide

### 1. Requirements & Installation
Make sure Python 3.8+ is installed on your system. Open terminal or command prompt inside the project folder:
```bash
pip install -r requirements.txt
```

### 2. Run the Main Application
```bash
python electricity_predictor.py
```
Or simply double-click `run_project.bat`.

### 3. Run Automated Tests
```bash
python test_runner.py
```
Or simply double-click `run_tests.bat`.

---

## 🧪 Benchmark Test Cases

| Case | Scenario | Input Data | Target Month | Expected Output |
| :---: | :--- | :--- | :---: | :--- |
| **TC 1** | Normal Input | `(1,200), (2,220), (3,240), (4,260)` | Month 5 | Slope: 20.00 \| Intercept: 180.00<br>Predicted units (Month 5): 280.00<br>Estimated bill: Rs. 1680.00 |
| **TC 2** | Minimum Input (2 rows) | `(1,100), (2,150)` | Month 3 | Slope: 50.00 \| Intercept: 50.00<br>Predicted units (Month 3): 200.00<br>Estimated bill: Rs. 1200.00 |
| **TC 3** | Invalid Input (1 row) | `(1,100)` | Month 2 | Error: At least 2 months of data are required for prediction. |
| **TC 4** | Variance Scenario ($R^2 < 1$) | `(1,100), (2,120), (3,150), (4,170)` | Month 6 | Slope: 24.00 \| Intercept: 75.00 \| R2: 0.99<br>Predicted units (Month 6): 219.00<br>Estimated bill: Rs. 1314.00<br>Line chart 'Actual vs Predicted' displayed |

---

## 📊 Mathematical Formulae
* **Regression Formula:** $\text{Units} = \text{Slope} \times \text{Month} + \text{Intercept}$
* **Slope ($m$):** $\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$
* **Intercept ($c$):** $\bar{y} - m\bar{x}$
* **Goodness of Fit ($R^2$):** $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$
* **Billing Formula:** $\text{Bill} = \text{Predicted Units} \times \text{₹}6.00$

---

## 📤 GitHub Submission Guide
To upload this project to your GitHub account:
```bash
# 1. Initialize git repository
git init

# 2. Add all files
git add .

# 3. Create initial commit
git commit -m "feat: complete Electricity Usage Predictor (PS No. 64)"

# 4. Set main branch
git branch -M main

# 5. Link to your GitHub repo (replace with your repo URL)
git remote add origin https://github.com/<your-username>/Electricity-Usage-Predictor.git

# 6. Push to GitHub
git push -u origin main
```
