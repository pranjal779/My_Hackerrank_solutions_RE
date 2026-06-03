<img width="648" height="475" alt="image" src="https://github.com/user-attachments/assets/590ff737-b838-4c2d-997d-29555d912d5b" />

```mysql
/*
Enter your query here.
*/
SELECT s.Name
FROM Students s
JOIN Packages p1 ON s.ID = p1.ID
JOIN Friends f ON s.ID = f.ID
JOIN Packages p2 ON f.Friend_ID = p2.ID
WHERE p2.Salary > p1.Salary
ORDER BY p2.Salary;
```
