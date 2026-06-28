-- استعلام حساب الشركات الأسرع والأرخص
SELECT carrier, 
       ROUND(AVG(lead_time_days), 2) AS avg_days, 
       ROUND(AVG(shipping_cost), 2) AS avg_cost 
FROM logistics_data 
GROUP BY carrier 
ORDER BY avg_days ASC;
