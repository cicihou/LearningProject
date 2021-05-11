'''
# Write your MySQL query statement below


My Solution:
SELECT a.Email AS Email
FROM
    (SELECT Email,
         count(*) AS c
    FROM Person
    GROUP BY  Email
    HAVING c > 1) a


Reference Solution(I think it's better):

select Email
from Person
group by Email
having count(Email) > 1

'''
