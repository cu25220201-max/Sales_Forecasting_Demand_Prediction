CREATE DATABASE IF NOT EXISTS sales_forecasting;
USE sales_forecasting;

CREATE TABLE IF NOT EXISTS sales (
    Order_ID VARCHAR(20) PRIMARY KEY,
    Customer_ID VARCHAR(20),
    Order_Date DATE,
    Product VARCHAR(100),
    Category VARCHAR(100),
    Region VARCHAR(50),
    Sales_Channel VARCHAR(50),
    Quantity INT,
    Unit_Price DECIMAL(12,2),
    Discount_Pct DECIMAL(5,2),
    Promotion_Flag TINYINT,
    Sales DECIMAL(14,2),
    Year INT,
    Month INT,
    Month_Name VARCHAR(20),
    Week INT,
    Day_Name VARCHAR(20)
);

SELECT Year, Month, Month_Name, ROUND(SUM(Sales),2) AS Total_Sales
FROM sales GROUP BY Year, Month, Month_Name ORDER BY Year, Month;

SELECT Product, Category, ROUND(SUM(Sales),2) AS Total_Sales,
       SUM(Quantity) AS Units_Sold, COUNT(*) AS Orders
FROM sales GROUP BY Product, Category ORDER BY Total_Sales DESC;

SELECT Category, ROUND(SUM(Sales),2) AS Total_Sales, SUM(Quantity) AS Units_Sold
FROM sales GROUP BY Category ORDER BY Total_Sales DESC;

SELECT Month, Month_Name, ROUND(SUM(Sales),2) AS Total_Sales
FROM sales GROUP BY Month, Month_Name ORDER BY Total_Sales DESC;

SELECT Sales_Channel, ROUND(SUM(Sales),2) AS Total_Sales, SUM(Quantity) AS Units_Sold
FROM sales GROUP BY Sales_Channel ORDER BY Total_Sales DESC;

SELECT Region, ROUND(SUM(Sales),2) AS Total_Sales, SUM(Quantity) AS Units_Sold
FROM sales GROUP BY Region ORDER BY Total_Sales DESC;