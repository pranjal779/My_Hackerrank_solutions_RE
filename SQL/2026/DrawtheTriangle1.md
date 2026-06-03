```mysql
/*
Enter your query here.
*/
-- DELIMITER $$
-- CREATE PROCEDURE draw_triangle()
-- BEGIN
--     DECLARE i INT DEFAULT 20;
--     WHILE i > 0 DO
--         SELECT REPEAT('* ', i);
--         SET i = i - 1;
--     END WHILE;
-- END$$
-- DELIMETER ;

-- CALL draw_triangle();

SELECT REPEAT('* ', @NUMBER := @NUMBER - 1) FROM information_schema.tables, 
(SELECT @NUMBER:=21) t 
LIMIT 20;
```

<img width="2322" height="1147" alt="image" src="https://github.com/user-attachments/assets/e733d9da-1b98-4718-8bfc-77e3755670a3" />
