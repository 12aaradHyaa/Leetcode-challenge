# Write your MySQL query statement below
SELECT d.name as Department,e1.name as Employee, e1.salary
FROM Employee e1 INNER JOIN Department d
ON e1.departmentId = d.id
WHERE 3 > (
    SELECT count(distinct(e2.salary))
    from Employee as e2
    where e2.salary > e1.salary and e1.departmentId = e2. departmentId
)