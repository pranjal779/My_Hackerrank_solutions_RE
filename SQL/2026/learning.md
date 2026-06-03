# 15 Days of Learning SQL

SELECT p1.*, h.hacker_id, h.name
FROM
(
    SELECT submission_date, count(hacker_id)
    FROM (
        SELECT s3.submission_date, s3.hacker_id, Count(DISTINCT S4.submission_date)
        FROM submissions S3
        LEFT JOIN submissions S4 on (s3.hacker_id=s4.hacker_id and s4.submission_date<s3.submission_date )
        GROUP BY 1,2
        HAVING Count(DISTINCT S4.submission_date)= Datediff(S3.submission_date, '2016-03-01')
        ) t
    GROUP BY 1) p1
LEFT JOIN
    ( SELECT submission_date, 1000000-SUBSTRING_INDEX(h_id,'_',-1) hh_id
        from (
            SELECT submission_date, max(concat(cs,'_',(1000000-hacker_id))) h_id
            from (
                SELECT submission_date, hacker_id, count(submission_id) cs
                FROM submissions
                WHERE submission_date between '2016-03-01' and '2016-03-16'
                GROUP BY 1,2
                ORDER BY 1,3 desc, 1) k
            GROUP BY 1
    ) s ) p2 Using (submission_date)
JOIN hackers h ON h.hacker_id=p2.hh_id
ORDER BY 1
