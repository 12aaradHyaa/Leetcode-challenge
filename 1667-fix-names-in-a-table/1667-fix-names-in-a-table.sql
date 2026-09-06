# Write your MySQL query statement below
SELECT user_id, 
    CONCAT( UPPER( LEFT (name,1)) , LOWER(RIGHT(name, LENGTH(name)-1))) as name
FROM Users
order by user_id