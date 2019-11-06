'''
sqlzoo -- NSS_Tutorial
https://sqlzoo.net/wiki/NSS_Tutorial
'''


'''
The example shows the number who responded for:

question 1
How many stops are in the database.


SELECT count(id) FROM stops
'''


'''
2.
Find the id value for the stop 'Craiglockhart'


SELECT id FROM stops WHERE name = 'Craiglockhart'
'''


'''
3.
Give the id and the name for the stops on the '4' 'LRT' service.


SELECT id, name 
FROM stops JOIN route ON stops.id = route.stop 
WHERE num = 4 AND company='LRT'
'''


'''
4.
The query shown gives the number of routes that visit either London Road (149) or Craiglockhart (53). Run the query and notice the two services that link these stops have a count of 2. Add a HAVING clause to restrict the output to these two routes.


SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num HAVING count(*) = 2
'''


'''
5.
Execute the self join shown and observe that b.stop gives all the places you can get to from Craiglockhart, without changing routes. Change the query so that it shows the services from Craiglockhart to London Road.


SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 AND b.stop=149
'''


'''
6.
The query shown is similar to the previous one, however by joining two copies of the stops table we can refer to stops by name rather than by number. Change the query so that the services between 'Craiglockhart' and 'London Road' are shown. If you are tired of these places try 'Fairmilehead' against 'Tollcross'


SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart' AND stopb.name='London Road'
'''


'''
7.
Give a list of all the services which connect stops 115 and 137 ('Haymarket' and 'Leith')


SELECT a.company AS company, a.num AS num FROM route a, route b 
WHERE a.num=b.num AND a.company = b.company AND a.stop = 115 AND b.stop = 137 GROUP BY company, num
'''


'''
8.
Show the institution, the total sample size and the number of computing students for institutions in Manchester for 'Q01'.


SELECT a.company AS company, a.num AS num 
FROM route a, route b 
WHERE a.num=b.num AND a.company = b.company 
AND a.stop = (SELECT id FROM stops WHERE name = 'Craiglockhart') 
AND b.stop = (SELECT id FROM stops WHERE name = 'Tollcross') 
GROUP BY company, num
'''


'''
9.
Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.


SELECT (SELECT name FROM stops WHERE id = b.stop) AS name, 
    a.company AS company, 
    a.num AS num 
FROM route a, route b 
WHERE a.num = b.num AND a.company = b.company 
    AND a.stop in (SELECT id FROM stops WHERE name = 'Craiglockhart') 
GROUP BY name, company, num
'''


'''
10.
Find the routes involving two buses that can go from Craiglockhart to Lochend.
Show the bus no. and company for the first bus, the name of the stop for the transfer,
and the bus no. and company for the second bus.

Hint
Self-join twice to find buses that visit Craiglockhart and Lochend, then join those on matching stops.

S 表求路过 Craig 站点的route，L 表求路过 Loc 站点的 route，两条路线都经过的站点，就是中转站的表。
重新 JOIN stops 表是为了根据 id 求中转站的名字

SELECT DISTINCT S.num, S.company, stops.name, L.num, L.company
FROM
(SELECT a.company, a.num, b.stop
 FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
 WHERE a.stop=(SELECT id FROM stops WHERE name= 'Craiglockhart')
)S
  JOIN
(SELECT a.company, a.num, b.stop
 FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
 WHERE a.stop=(SELECT id FROM stops WHERE name= 'Lochend')
)L
ON (S.stop = L.stop)
JOIN stops ON(stops.id = S.stop)
'''
