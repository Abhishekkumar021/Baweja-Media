-- 1. Total amount spent by each customer

SELECT customer_id, SUM(amount) as total_spent FROM orders GROUP BY customer_id;

-- 2. Orders placed after '2023-01-03'

SELECT * FROM orders WHERE order_date > '2023-01-03';


-- 3. Customer(s) who made more than one order

SELECT customer_id, COUNT(*) as Order_count FROM orders GROUP BY customer_id HAVING COUNT(*) > 1;
