# Write your MySQL query statement below
SELECT product_name , sum(unit) as unit
FROM Products INNER JOIN Orders USING(product_id)
where month(order_date) = 2 and year(order_date)= 2020
group by product_name
having unit>= 100