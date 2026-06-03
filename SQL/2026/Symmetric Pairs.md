# Symmetric Pairs

[reference](https://github.com/BlakeBrown/HackerRank-Solutions/blob/master/SQL/5_Advanced%20Join/3_Symmetric%20Pairs/Symmetric%20Pairs.mysql)

```mysql
SELECT X, Y FROM FUNCTIONS F1
    WHERE EXISTS(SELECT * FROM FUNCTIONS F2 WHERE F2.Y = F1.X
    AND F2.X = F1.Y AND F2.X > F1.X) AND (X != Y)
UNION
SELECT X,Y FROM FUNCTIONS F1 WHERE X = Y AND 
    ((SELECT COUNT(*) FROM FUNCTIONS WHERE X = F1.X AND Y = F1.X) > 1)
      ORDER BY X;
```
