'''
# Write your MySQL query statement below

SELECT d.Name AS Department,
         e.Name AS Employee,
         a.s AS Salary
FROM
    (SELECT DepartmentId,
         max(Salary) AS s
    FROM Employee
    GROUP BY  DepartmentId) a
JOIN Employee e
    ON a.DepartmentId = e.DepartmentId
JOIN Department d
    ON d.id = e.DepartmentId
WHERE a.s = e.Salary



Reference(save one outer join, but use sub join ):

SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)

'''
