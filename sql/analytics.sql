-- Total revenue
SELECT SUM(revenue) AS total_revenue
FROM loads;

-- Average revenue per mile
SELECT ROUND(AVG(revenue_per_mile), 2) AS avg_revenue_per_mile
FROM loads;

-- Most profitable loads
SELECT load_id, date, miles, tons, revenue, revenue_per_mile
FROM loads
ORDER BY revenue_per_mile DESC
LIMIT 10;

-- High-value load count
SELECT COUNT(*) AS high_value_loads
FROM loads
WHERE high_value_load = TRUE;