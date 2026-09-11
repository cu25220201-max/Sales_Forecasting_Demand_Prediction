# 📊 Sales Forecasting & Demand Prediction Analysis

An end-to-end Data Analytics project that analyzes historical retail sales data, identifies sales trends and seasonal demand patterns, and forecasts future sales to support better business and inventory planning.

## 🎯 Project Objective

The objective of this project is to help a retail company understand historical sales performance and predict future demand.

The analysis focuses on:

- Sales trend identification
- Product and category performance
- Seasonal demand patterns
- Future sales forecasting
- Inventory and demand planning
- Business decision-making

## 📌 Business Problem

The retail company is facing challenges such as:

- Sudden increase or decrease in product demand
- Poor sales planning
- Inefficient inventory management
- Difficulty identifying peak sales periods

This project uses historical sales data to generate actionable business insights.

## 📂 Dataset

A self-generated retail sales dataset containing **12,000+ sales records** was used for this project.

### Main Columns

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Customer_ID | Unique customer identifier |
| Order_Date | Date of the order |
| Product | Product name |
| Category | Product category |
| Region | Sales region |
| Sales_Channel | Online, Store or Marketplace |
| Quantity | Units sold |
| Unit_Price | Price per unit |
| Discount | Applied discount |
| Sales | Total sales value |

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Plotly**
- **Streamlit**
- **SQL**
- **Excel**
- **Time Series Analysis**

## 🔄 Project Workflow

```text
Data Collection
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Trend Analysis
      ↓
Seasonal Demand Analysis
      ↓
Product & Category Analysis
      ↓
Sales Forecasting
      ↓
Interactive Dashboard
      ↓
Business Insights & Recommendations

````

## 🧹 Data Cleaning & Preprocessing

Before analysis, the sales dataset was prepared for reliable analysis.

#### The workflow includes:

Loading the sales dataset
Converting the Order_Date column into datetime format
Checking data quality
Handling duplicate records
Preparing categorical variables
Filtering data using dashboard selections
Creating monthly sales aggregations
Preparing the dataset for forecasting

## 🔎 Exploratory Data Analysis

Exploratory analysis was performed to understand the major sales patterns in the dataset.

#### Key Analysis
Total Sales
Units Sold
Total Orders
Average Order Value
Monthly Sales Trend
Sales by Product
Sales by Category
Seasonal Demand Pattern
Regional Analysis
Sales Channel Analysis

## 📦 Product & Category Analysis

The project analyzes sales performance at product and category levels.

#### Product Analysis
Identify high-performing products
Compare product-level sales
Support inventory planning
Identify products requiring closer monitoring

#### Category Analysis
Compare category contribution
Identify strong-performing categories
Support category-level growth strategies

## 🌦️ Seasonal Demand Pattern

Sales are grouped by calendar month to identify recurring demand patterns.

This analysis can help businesses:

Prepare inventory before high-demand periods
Plan marketing campaigns
Improve resource allocation
Identify seasonal opportunities
Reduce the risk of stock-outs

## 🔮 6-Month Sales Forecast
````txt
The project generates a 6-month future sales forecast based on historical monthly sales.

Forecasting Approach

A basic linear trend forecasting method is applied to monthly historical sales.

The forecasting workflow is:

Historical Monthly Sales
          ↓
Create Time Index
          ↓
Fit Linear Trend
          ↓
Predict Future Periods
          ↓
Generate 6-Month Forecast
````

## 💡 Business Recommendations

Based on the analysis, the following recommendations can be considered:

1. Prepare Inventory for High-Demand Periods

Historical seasonal patterns can be used to plan inventory before expected demand increases.

2. Monitor High-Performing Products

Products generating strong sales should be monitored regularly to maintain availability and avoid stock-outs.

3. Focus on High-Performing Categories

Categories with strong sales contribution can be prioritized for future growth and promotional strategies.

4. Improve Reorder Planning

Businesses can use demand forecasts, supplier lead time, and safety-stock levels to improve reorder decisions.

5. Monitor Actual vs Forecast Sales

Forecasted sales should be compared with actual sales every month to evaluate forecast performance and improve future predictions.

## 🚀 Practical Implementation
````txt
The Streamlit application performs the complete dashboard workflow.

The dashboard:

Load Clean Dataset
       ↓
Apply User Filters
       ↓
Calculate KPIs
       ↓
Generate Monthly Analysis
       ↓
Analyze Products & Categories
       ↓
Identify Seasonal Patterns
       ↓
Generate 6-Month Forecast
       ↓
Display Business Recommendations
````

## 📊 Project Outcome
````txt
This project demonstrates how raw retail sales data can be transformed into meaningful business insights through an end-to-end analytics workflow.

The project combines:

Python
+
SQL / MySQL
+
Excel
+
Data Analysis
+
Forecasting
+
Streamlit

````
## 🔮 Future Scope

The project can be further enhanced by:

Implementing advanced forecasting models
Comparing multiple forecasting algorithms
Adding MAE, RMSE and MAPE evaluation
Incorporating holidays and promotional events
Adding pricing and discount information
Including external demand drivers
Automating data refresh
Connecting the dashboard to a live database
Adding forecast confidence intervals
Deploying the dashboard online

#### Screenshots

<img width="960" height="443" alt="image" src="https://github.com/user-attachments/assets/87bed6f1-8557-426c-9789-bd72e59db48f" />

<img width="743" height="409" alt="image" src="https://github.com/user-attachments/assets/731f952d-1a32-4d99-a74b-e94539c67723" />

<img width="643" height="421" alt="image" src="https://github.com/user-attachments/assets/8f5070dd-ee71-48ee-849c-bfb86aab6fb2" />

<img width="716" height="419" alt="image" src="https://github.com/user-attachments/assets/27dfbf2b-a467-4bfa-8275-cde09755c632" />

<img width="727" height="430" alt="image" src="https://github.com/user-attachments/assets/0690ac98-e551-45ab-b41f-46f9d7a11e08" />

<img width="960" height="485" alt="image" src="https://github.com/user-attachments/assets/d30a2ca1-31f2-4036-8a37-180d773c2a79" />


## 👩‍💻 Author
Pratiksha Tomar

B.Tech AI/ML Student | Aspiring Data Analyst

#### Technical Skills

Python • SQL • MySQL • Power BI • Pandas • NumPy • Matplotlib • Plotly • Streamlit • Data Analytics • Machine Learning

Learning

## 🎓 Internship

#### 3Skill Training — Data Analytics Internship

This project was developed as part of practical project-based learning during the internship.
