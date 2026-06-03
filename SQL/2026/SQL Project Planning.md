# SQL Project Planning

# [reference](https://chenkaili.medium.com/hackerrank-sql-project-planning-51cf0a098f64)

```mysql
SELECT A.Start_Date, MIN(B.End_Date)
FROM 
    (SELECT Start_Date
    FROM Projects
    WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS A
    INNER JOIN
    (SELECT End_Date
    FROM Projects
    WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) AS B
WHERE A.Start_Date < B.End_Date
GROUP BY A.Start_Date
ORDER BY MIN(B.End_Date) - A.Start_Date ASC, A.Start_Date;
```

