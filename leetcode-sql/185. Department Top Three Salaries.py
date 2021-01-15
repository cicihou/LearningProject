'''

SELECT d.Name AS Department,
         e.Name AS Employee,
         e.Salary AS Salary
FROM Employee e
JOIN Department d
    ON d.id = e.DepartmentId
JOIN
    (SELECT DepartmentId,
         Salary AS s
    FROM Employee e1
    WHERE 3 >
        (SELECT count(distinct(Salary))
        FROM Employee e2
        WHERE e1.Salary < e2.Salary
                AND e1.DepartmentId = e2.DepartmentId)) a
        ON e.DepartmentId = a.DepartmentId
        AND e.Salary = a.s
GROUP BY  Department, Employee, Salary


notice the sub query
the number 3 means u need to get top 3, n for top n

count(distinct(Salary)), the 'distinct' means u can accept top 3 highest salary
if not distinct, it means you can get top 3 person with highest salary
'''
