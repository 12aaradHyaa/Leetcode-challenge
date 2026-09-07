# Write your MySQL query statement below
SELECT sell_date,
     count(distinct product) as num_sold,
     GROUP_CONCAT(
        distinct product
        order by product
        separator ','
     ) AS products
FROM Activities
GROUP BY sell_date
order by sell_date, product