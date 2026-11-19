# PROJECT REPORT
## PS No. 64: Electricity Usage Predictor

---

### **Academic Information**
* **Institution:** Rungta International Skills University
* **Department:** School of Computer Science and Engineering
* **Program:** Bachelor of Technology in Computer Science and Engineering (B.Tech CSE)
* **Semester / Section:** First Semester / Section - H
* **Course Title:** Programming Fundamentals and Logic Building Using Python
* **Course Code:** RU-100-01-0021
* **Date of Allocation:** 14th October 2026
* **Date of Submission:** 16th November 2026
* **Evaluation Total:** 40 Marks (20 Internal + 20 External)

---

## 1. Executive Summary
The **Electricity Usage Predictor** is a data-driven Python console application designed to analyze historical monthly electricity consumption, fit a Simple Linear Regression model using Ordinary Least Squares (OLS) via `numpy.polyfit`, forecast future power consumption (in units/kWh), estimate the billing amount at a flat rate of ₹6.00 per unit, and visualize trend patterns using `matplotlib`.

The system incorporates robust data sanitization with `pandas`, handles minimum-sample boundary conditions, computes the Coefficient of Determination ($R^2$), and provides interactive visualization alongside an automated verification test suite.

---

## 2. Problem Statement & Scope
### 2.1 Problem Description
Electricity distribution and consumer budgeting both depend on accurate demand forecasting. Fluctuating consumption patterns require automated tools to extrapolate future demands based on preceding monthly readings.

### 2.2 Functional Requirements
1. **Console Execution:** Run as a standalone Python 3 script.
2. **Data Ingestion & Cleaning:** Ingest CSV records (`Month`, `Units`), detect non-numeric and null records, clean bad rows, and present descriptive statistics.
3. **Statistical Modeling:** Utilize `numpy.polyfit(deg=1)` to derive slope ($m$) and intercept ($c$).
4. **Boundary Validation:** Enforce that at least 2 distinct data points exist for linear regression; raise descriptive errors otherwise.
5. **Prediction & Financial Estimation:** Predict units for an arbitrary future month ($x$) and estimate billing cost:
   $$\text{Estimated Bill} = \text{Predicted Units} \times \text{₹}6.00$$
6. **Goodness of Fit ($R^2$):** Compute $R^2$ to assess trend variance and output rounded to 2 decimal places.
7. **Visualization:** Plot historical usage scatter points against the regression trend line with complete title, labels, and legend.

---

## 3. Mathematical Foundations

### 3.1 Simple Linear Regression Model
The relationship between the independent variable $x$ (Month) and dependent variable $y$ (Electricity Units) is modeled as:
$$y = mx + c$$
where:
* $m$ = Slope of the regression line (rate of change in units per month)
* $c$ = Y-intercept (baseline consumption)

### 3.2 Ordinary Least Squares (OLS) Formulation
The parameters $m$ and $c$ minimize the sum of squared residuals:
$$m = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$
$$c = \bar{y} - m\bar{x}$$
where $\bar{x}$ and $\bar{y}$ represent the sample means of Month and Units respectively.

### 3.3 Coefficient of Determination ($R^2$)
$R^2$ measures the proportion of variance in electricity consumption predictable from the month index:
$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
* $R^2 = 1.00$: Perfect linear correlation (points lie exactly on the line).
* $R^2 \approx 0.99$: High correlation (e.g., Test Case 4).

### 3.4 Tariff Calculation
$$\text{Cost} = \hat{y}_{\text{target}} \times 6.00$$

---

## 4. Software Architecture & Flowchart

### 4.1 System Flowchart
```mermaid
flowchart TD
    A([Start Program]) --> B[Load CSV via Pandas]
    B --> C{Check Missing / Non-numeric Values}
    C -->|Invalid Found| D[Drop Corrupted Rows & Log]
    C -->|Valid| E[Show Data Summary]
    D --> E
    E --> F{Display Interactive Menu}
    F -->|Option 1: Predict| G[Prompt for Future Month]
    G --> H{Record Count >= 2?}
    H -->|No (< 2 rows)| I["Display Error: At least 2 months of data are required for prediction."]
    I --> F
    H -->|Yes (>= 2 rows)| J[Compute Slope & Intercept via numpy.polyfit]
    J --> K[Compute R2 Score]
    K --> L[Calculate Predicted Units & Bill at Rs. 6/unit]
    L --> M[Display Formatted Output]
    M --> N[Render & Save Matplotlib Trend Plot]
    N --> F
    F -->|Option 2: Summary| O[Show Descriptive Statistics]
    O --> F
    F -->|Option 3: Chart| P[Plot Current Trend Line]
    P --> F
    F -->|Option 4: Reload| Q[Input New CSV Path]
    Q --> B
    F -->|Option 5: Exit| R([Terminate Program])
```

---

## 5. Implementation Details

### 5.1 Modules & Technologies Used
| Library | Version | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.12+ | Core programming runtime |
| **Pandas** | >= 2.0.0 | Tabular data reading, type coercion, cleaning & summaries |
| **NumPy** | >= 1.24.0 | Vectorized regression line fitting (`polyfit`) & $R^2$ calculations |
| **Matplotlib** | >= 3.7.0 | Scatter plots, regression lines, annotations, and export |

### 5.2 Key Algorithms
1. **Dynamic Header Detection:** Reads the first line of the CSV. If values are non-numeric strings, it handles them as column headers; if numeric, it assigns standard `['Month', 'Units']` headers.
2. **Safe Type Conversion:** Uses `pd.to_numeric(..., errors='coerce')` to gracefully identify and remove invalid corrupted rows.
3. **Regression Fitting:** `np.polyfit(x, y, deg=1)` extracts float slope and intercept with $O(n)$ complexity.
4. **Conditional $R^2$ Reporting:** If $R^2 < 1.00$, the report string includes `| R2: X.XX`; if points are collinear ($R^2 = 1.00$), output cleanly follows rubric standards.

---

## 6. Test Case Verification & Experimental Results

The project was evaluated against all 4 benchmark test scenarios specified by the university.

| Test Case | Scenario Description | Input Dataset (Month, Units) | Predict Month | Expected Output | Actual Output | Status |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: |
| **TC-1** | Normal Input (Collinear 4 months) | `(1,200), (2,220), (3,240), (4,260)` | Month 5 | Slope: 20.00 \| Intercept: 180.00<br>Predicted units: 280.00<br>Estimated bill: Rs. 1680.00 | Slope: 20.00 \| Intercept: 180.00<br>Predicted units (Month 5): 280.00<br>Estimated bill: Rs. 1680.00 | **PASSED** |
| **TC-2** | Boundary / Minimum Input (2 rows) | `(1,100), (2,150)` | Month 3 | Slope: 50.00 \| Intercept: 50.00<br>Predicted units: 200.00<br>Estimated bill: Rs. 1200.00 | Slope: 50.00 \| Intercept: 50.00<br>Predicted units (Month 3): 200.00<br>Estimated bill: Rs. 1200.00 | **PASSED** |
| **TC-3** | Invalid Input (Single row) | `(1,100)` | Month 2 | Error: At least 2 months of data are required for prediction. | Error: At least 2 months of data are required for prediction. | **PASSED** |
| **TC-4** | Scenario with Variance ($R^2 < 1$) | `(1,100), (2,120), (3,150), (4,170)` | Month 6 | Slope: 24.00 \| Intercept: 75.00 \| R2: 0.99<br>Predicted units: 219.00<br>Estimated bill: Rs. 1314.00<br>Line chart displayed | Slope: 24.00 \| Intercept: 75.00 \| R2: 0.99<br>Predicted units (Month 6): 219.00<br>Estimated bill: Rs. 1314.00<br>Line chart 'Actual vs Predicted' displayed | **PASSED** |

**Pass Rate:** 4 / 4 (100.0%)

---

## 7. Sample Visual Output
The system generates a high-definition plot (`usage_trend_plot.png`) showing:
* **Blue Scatter Markers:** Past monthly consumption points.
* **Red Dashed Line:** Linear regression trend line representing the mathematical equation.
* **Green Star Marker:** The predicted future month consumption with callout annotation.
* **Axes & Grid:** Labeled axes ("Month", "Electricity Units"), high-contrast grid, and detailed legend.

---

## 8. Viva Voce & Technical Defense Q&A

### Q1: What is Simple Linear Regression?
> **Answer:** Simple Linear Regression is a supervised learning method that models the linear relationship between a single independent explanatory variable ($x$) and a single continuous dependent variable ($y$). In this project, $x$ is the Month and $y$ is the Electricity Consumption in units.

### Q2: Why is `numpy.polyfit` used with degree 1?
> **Answer:** A 1st-degree polynomial takes the form $y = p_0 x + p_1$. `numpy.polyfit(x, y, 1)` uses the method of least squares to find the coefficients $p_0$ (slope) and $p_1$ (intercept) that minimize the squared Euclidean distance between actual and modeled points.

### Q3: What is $R^2$ and what does a value of 0.99 signify in Test Case 4?
> **Answer:** $R^2$ (Coefficient of Determination) represents the proportion of total variance in the dependent variable that is explained by the regression line. An $R^2$ of 0.99 indicates that 99% of the variability in electricity consumption is accounted for by the progression of months, demonstrating an extremely strong predictive fit.

### Q4: Why are at least 2 data points strictly required?
> **Answer:** Geometrically and mathematically, a minimum of two distinct coordinates $(x_1, y_1)$ and $(x_2, y_2)$ are necessary to define a unique straight line. With only one point, the denominator $\sum (x_i - \bar{x})^2$ becomes zero, resulting in a mathematical division-by-zero error (infinite possible slopes).

### Q5: How are missing or non-numeric values handled?
> **Answer:** We use Pandas' `pd.to_numeric(df[col], errors='coerce')` function, which replaces unparseable strings with `NaN` (Not a Number). Then `df.dropna()` purges those rows, safeguarding the mathematical functions against runtime `TypeError` or `ValueError`.

---

## 9. Conclusion
The **Electricity Usage Predictor (PS No. 64)** successfully fulfills all criteria stipulated by the School of Computer Science and Engineering, Rungta International Skills University. The application delivers robust logic, verifiable mathematical accuracy across all test scenarios, complete interactive capabilities, and clear visualization.
