'''
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+


# 第 N 大问题，计算机 idx 从 0 开始，需要手动 -1 符合阅读习惯
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee GROUP BY Salary
      ORDER BY Salary DESC LIMIT 1 OFFSET N
  );
END


# 如果重新给变量，需要DECLEARE一下
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      IFNULL((SELECT DISTINCT Salary FROM Employee
      ORDER BY Salary DESC LIMIT 1 OFFSET M), NULL)
  );
END
'''
