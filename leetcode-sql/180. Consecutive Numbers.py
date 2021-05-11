'''
# Write your MySQL query statement below


SELECT distinct(a1.num) AS ConsecutiveNums
FROM logs a1, logs a2, logs a3
WHERE a1.id = a2.id - 1
        AND a2.id = a3.id - 1
        AND a1.num = a2.num
        AND a2.num = a3.num

'''
