'''
# Write your MySQL query statement below


SELECT a1.Name AS Employee
FROM employee a1
JOIN employee a2
    ON a1.ManagerId = a2.Id
WHERE a1.Salary > a2.Salary
'''
