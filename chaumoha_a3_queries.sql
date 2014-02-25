/* Bryan Chau & Mohamed Mohamedtaki
Assignment 3 */

/* Question 1 */
SELECT pname 
FROM catalog 
JOIN parts ON catalog.pid = parts.pid 
JOIN suppliers ON catalog.sid = suppliers.sid
GROUP BY pname;
/*
pname
-----
bolt
cam
cog
nail
nut
screw
*/


/* Question 2 */
SELECT sname
FROM (select sname, count(sname) FROM catalog
	JOIN suppliers ON catalog.sid = suppliers.sid 
	JOIN parts ON catalog.pid = parts.pid
	group by sname having count(sname) = (SELECT count(pid) FROM parts)) T;
/*
sname
-----
jones
*/

/* Question 3 */
SELECT sname from (
	SELECT sname,count(sname) as cnt 
	from suppliers 
	join(
		SELECT sid 
		from catalog 
		join (
			SELECT pid from parts
			where colour = 'red'
		) redparts
		where redparts.pid = catalog.pid
	) red_suppliers
	on suppliers.sid = red_suppliers.sid
	group by sname 
) a
where cnt = (
	SELECT count(pid)
	from parts
	where colour = 'red'
);
/*
sname
-----
jones
*/

/* Question 4 */
SELECT P.pname
FROM parts P, catalog C, suppliers S
WHERE P.pid = C.pid AND C.sid = S.sid AND S.sname = "jones" AND 
NOT EXISTS ( 
	SELECT *
	FROM catalog C1, suppliers S1
	WHERE P.pid = C1.pid 
	AND C1.sid = S1.sid 
    AND S1.sname <> "jones"
);
/*
pname
-----
screw
nail
*/

/* Question 5 */
Select distinct(C.sid)
From catalog C
inner join (
	Select Cin.pid as apid, AVG(Cin.cost) AS acost
	FROM catalog Cin
	group by apid
)cavg 
ON C.pid = cavg.apid
where C.cost > cavg.acost
order by C.sid;
/*
sid
---
s1
s2
s3
s4
*/

/* Question 6 */
Select S.sname, mtemp.pid
From suppliers S, catalog C
Inner join (
	Select Cin.pid as pid, MAX(Cin.cost) AS mcost
	From catalog Cin
	Group by Cin.pid
) mtemp
on C.pid = mtemp.pid
WHERE S.sid = C.sid AND C.cost = mtemp.mcost
order by mtemp.pid;
/*
sname | pid
-----------
smith	p1
jones	p2
jones	p3
clark	p4
blake	p5
jones	p6
*/

/* Question 7 */
SELECT DISTINCT C.sid
FROM catalog C
WHERE NOT EXISTS (
	SELECT *
	FROM parts P
	WHERE P.pid = C.pid AND P.colour <> "red"
);
/*
sid
---
s1
s2
s5
*/

/* Question 8 */
SELECT distinct(sid)
FROM catalog C
WHERE sid IN (
	SELECT DISTINCT C.sid
	FROM catalog C
	WHERE NOT EXISTS (
		SELECT *
		FROM parts P
		WHERE P.pid = C.pid AND P.colour <> "green"
	)
) AND sid IN ( 
	SELECT DISTINCT C.sid
	FROM catalog C
	WHERE NOT EXISTS (
		SELECT *
		FROM parts P
		WHERE P.pid = C.pid AND P.colour <> "red"
	)
) group by sid;
/*
sid
---
s2
s3
s5
*/

/* Question 9 */
SELECT s.sname, count(*) as numP
FROM suppliers s, catalog c 
WHERE s.sid=c.sid
AND s.sid IN (
	SELECT DISTINCT(C.sid)
	FROM catalog C
	WHERE NOT EXISTS (
		SELECT *
		FROM parts P
		WHERE P.pid = C.pid AND P.colour <> "green"
	)
) GROUP BY s.sname;
/*
sname | numP
adams	2
blake	2
jones	6
*/

/* Question 10 */
SELECT s.sname, max(C.cost) as expensive
FROM suppliers s, catalog c
WHERE s.sid=c.sid
AND s.sid IN (
	SELECT distinct(sid)
	FROM catalog C
	WHERE sid IN (
		SELECT DISTINCT C.sid
		FROM catalog C
		WHERE NOT EXISTS (
			SELECT *
			FROM parts P
			WHERE P.pid = C.pid AND P.colour <> "green"
		)
	) AND sid IN ( 
		SELECT DISTINCT C.sid
		FROM catalog C
		WHERE NOT EXISTS (
			SELECT *
			FROM parts P
			WHERE P.pid = C.pid AND P.colour <> "red"
		)
	) group by sid
) GROUP BY s.sname
/*
sname | expensive
adams	200
blake	400
jones	800
*/