# 📊 Supply Chain & Logistics Data Analysis Dashboard

## 🎯 Project Overview
This project is an end-to-end data analysis and automation solution designed to optimize supply chain and logistics operations. It showcases the integration of relational databases (SQL) and interactive web applications (Streamlit) to transform raw logistics data into actionable business insights.

## ⚡ The Problem & Solution
* **The Problem:** Supply chain operations generate massive tracking and inventory data, which is often difficult to interpret, leading to delays, high delivery costs, and inefficient supplier management.
* **The Solution:** Built a robust analytical pipeline that cleans raw dataset files, updates a local SQLite database, runs strategic optimization queries, and visualizes KPIs through an interactive dashboard.

## 🛠️ Project Architecture & Tech Stack
* **Database Management:** SQLite (`logistics.db`) utilized for structured storage and querying operations via `logistics_queries.sql`.
* **Data Processing:** Python (Pandas) used for standardizing data schemas and handling missing records.
* **Interactive Dashboard:** Built with **Streamlit** (`streamlit_app.py`) to create user-friendly visual analytics for logistics managers.
* **Version Control:** Git & GitHub.

## 🔍 Sample Analytical Query (SQL)
To evaluate and optimize operational efficiency, the project leverages advanced SQL querying. Below is a key query designed to identify the fastest and most cost-effective shipping carriers:

```sql
-- استعلام حساب الشركات الأسرع والأرخص
SELECT carrier,
       ROUND(AVG(lead_time_days), 2) AS avg_days,
       ROUND(AVG(shipping_cost), 2) AS avg_cost
FROM logistics_data
GROUP BY carrier
ORDER BY avg_days ASC;
