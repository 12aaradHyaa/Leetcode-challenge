# Write your MySQL query statement below
SELECT max(e1.salary) as SecondHighestSalary 
FROM Employee e1 INNER JOIN Employee e2
ON e1.salary < e2.salary
