'''

My Solution:

DELETE
FROM Person
WHERE id NOT IN
    (SELECT id
    FROM
        (SELECT email,
         min(id) AS id
        FROM Person
        GROUP BY email) a)

Notice:
you cannot update/delete a table you use it directly in your where clause
(You can't specify target table for update in FROM clause)


Reference Solution:

DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

'''
