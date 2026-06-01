<img width="1022" height="1150" alt="image" src="https://github.com/user-attachments/assets/fa731900-bfd0-452a-ac70-4c01ff379bb8" />
<img width="1007" height="796" alt="image" src="https://github.com/user-attachments/assets/b4526319-5527-4929-819e-22098c5fdd15" />
<img width="573" height="760" alt="image" src="https://github.com/user-attachments/assets/060fd346-fa71-48fa-bbee-88f42cba6038" />
<img width="262" height="792" alt="image" src="https://github.com/user-attachments/assets/addb96c1-5865-4dc3-abba-687b8df861ea" />
<img width="362" height="690" alt="image" src="https://github.com/user-attachments/assets/6ca52ba7-8194-4c1d-990d-ed592e5fb679" />
<img width="355" height="1118" alt="image" src="https://github.com/user-attachments/assets/08484309-db0c-4e6f-99f0-4030c736d498" />
<img width="372" height="1137" alt="image" src="https://github.com/user-attachments/assets/cbf6aefc-130e-4212-85d0-faa5a7cab33a" />
<img width="347" height="427" alt="image" src="https://github.com/user-attachments/assets/ab847c56-67ab-4a99-b878-57b9889c64c9" />


<img width="1170" height="730" alt="image" src="https://github.com/user-attachments/assets/d606a6f8-c867-4230-9758-ec21ca5d525d" />
<img width="1888" height="877" alt="image" src="https://github.com/user-attachments/assets/22d7f1ab-433b-4490-a6a0-591015b2d38d" />




The HackerRank "Challenges" problem is one of the most prominent tasks in the Basic Join submodule of the HackerRank SQL Practice Domain. It transitions from standard table linkages into complex aggregation filtering by requiring a combination of , , and restrictive subqueries within a  clause. [1, 2, 3, 4]  
📋 The Problem Break Down 
You need to print the hacker_id, name, and the total number of challenges created by each student.The sorting and filtering rules make this problem uniquely tricky: 

1. Primary Sort: Total challenges created in descending order. 
2. Secondary Sort: hacker_id in ascending order. 
3. The Trap Condition: If multiple students created the same number of challenges, you must exclude them unless that number is the absolute maximum number of challenges created by anyone. [2, 5, 6]

```sql
SELECT 
    h.hacker_id, 
    h.name, 
    COUNT(c.challenge_id) AS total_challenges
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING 
    /* Condition 1: Keep them if their count equals the global maximum count */
    total_challenges = (
        SELECT COUNT(challenge_id) 
        FROM Challenges 
        GROUP BY hacker_id 
        ORDER BY COUNT(challenge_id) DESC 
        LIMIT 1
    )
    OR 
    /* Condition 2: Keep them if their count is unique (no other hacker shares it) */
    total_challenges IN (
        SELECT sub.cnt 
        FROM (
            SELECT COUNT(challenge_id) AS cnt 
            FROM Challenges 
            GROUP BY hacker_id
        ) sub
        GROUP BY sub.cnt
        HAVING COUNT(sub.cnt) = 1
    )
ORDER BY total_challenges DESC, h.hacker_id ASC;
```

💻 Optimized SQL Solution (MySQL) 
🔍 Step-by-Step Logic Explained 
1. Core Linkage & Aggregation: We use an INNER JOIN to link the Hackers table to the Challenges table on hacker_id. We group the records by the student's credentials to calculate their total output using COUNT(c.challenge_id). [2, 7]  
2. The Global Max Filter: The first half of the HAVING clause checks if a user hit the maximum threshold. The subquery isolates all group counts, orders them from highest to lowest, and uses LIMIT 1 to grab the peak value. Anyone reaching this peak is automatically safe from exclusion, regardless of ties.  [2, 3, 7, 8]  
3. The Uniqueness Filter: The second half handles sub-maximum ties. The deep subquery sub creates a list of challenge counts per user. The wrapper query then groups those counts and filters out any count value that appears more than once (HAVING COUNT(sub.cnt) = 1).  [2, 4, 9, 10, 11]  

🚀 Additional Basic Join Roadmaps 
If you are systematic about clearing the HackerRank Basic Join Section, prioritize practicing your joins in this specific progression: 

• Population Census & African Cities: Great for basic multi-table filtering using strict column criteria. 
• Average Population of Each Continent: Pairs a basic join with the  mathematical aggregation function. 
• The Report: Introduces non-equi joins using the  operator to link records without matching ID fields. 
• Top Competitors: A step up that requires joining four distinct tables simultaneously (Submissions, Hackers, Challenges, and Difficulty). [3, 4, 9, 12, 13]  

If you would like to map out more solutions, tell me: 

• Are you writing your queries in MySQL, MS SQL Server, or Oracle? 
• Which specific Basic Join problem from the roadmap do you want to tackle next? 


[1] https://www.hackerrank.com/domains/sql
[2] https://medium.com/@bingqianwa777/hackerrank-basic-join-challenges-f11c5d2cbd73
[3] https://www.youtube.com/watch?v=bYRjJKCJfKo
[4] https://blog.devgenius.io/preparing-for-sql-interview-with-hackerrank-part-2-d08369fc7155
[5] https://www.reddit.com/r/SQL/comments/16hp4n6/help_me_understand_the_order_by_part_of_this/
[6] https://github.com/daiphuongngo/SQL-Solutions-HackerRank
[7] https://github.com/sknsht/HackerRank/blob/master/SQL/Basic%20Join/Challenges/Solution.sql
[8] https://medium.com/@kiruthickagp/hacker-rank-sql-advanced-15-days-of-learning-sql-by-kiruthicka-gp-312ce3a02728
[9] https://www.linkedin.com/posts/peeyush-choudhary-6aa749264_solve-sql-code-challenges-activity-7405837650911404032-QLRJ
[10] https://medium.com/@datasciencewithnish/top-sql-interview-question-hackerrank-top-competitors-2fc42287dcce
[11] https://medium.com/@kiruthickagp/hacker-rank-challenges-sql-medium-fa5d25c8439e
[12] https://dailyjournal.gitbook.io/solutions/hackerrank-solutions/prepare/sql/basic-join
[13] https://my-mindpalace.tistory.com/20

