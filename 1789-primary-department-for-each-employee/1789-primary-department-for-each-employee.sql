# Write your MySQL query statement below
Select DISTINCT employee_id , department_id
FROM employee
WHERE employee_id In(
    SELECT employee_id 
    from employee
    GROUP  BY employee_id
    HAVING count(*)= 1
) OR primary_flag = "Y"
Order by employee_id