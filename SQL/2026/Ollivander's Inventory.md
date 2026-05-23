# Ollivander's Inventory

Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age.  
Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power.  
If more than one wand has same power, sort the result in order of descending age.  

Input Format  

The following tables contain data on the wands in Ollivander's inventory:  

Wands: The id is the id of the wand, code is the code of the wand, coins_needed is the total number of gold galleons needed to buy the wand, and power denotes the quality of the wand (the higher the power, the better the wand is).  

<img width="200" height="190" alt="image" src="https://github.com/user-attachments/assets/c5075ab1-64da-4e74-a19e-649c01c0bd41" />

<img width="1017" height="168" alt="image" src="https://github.com/user-attachments/assets/4939d454-1faf-481b-b814-2e1004c646d7" />
<img width="164" height="153" alt="image" src="https://github.com/user-attachments/assets/8461a935-9f16-415b-b4a1-959478a1c01e" />

Sample Input

Wands Table:

<img width="305" height="752" alt="image" src="https://github.com/user-attachments/assets/8670d938-203b-455b-aeb1-58d192225b46" />

Wands_Property Table:

<img width="194" height="227" alt="image" src="https://github.com/user-attachments/assets/3ff4fab9-bcb8-4327-b327-d4a95c00d9cc" />

Sample Output

9 45 1647 10
12 17 9897 10
1 20 3688 8
15 40 6018 7
19 20 7651 6
11 40 7587 5
10 20 504 5
18 40 3312 3
20 17 5689 3
5 45 6020 2
14 40 5408 1
Explanation

The data for wands of age 45 (code 1):
<img width="1015" height="577" alt="image" src="https://github.com/user-attachments/assets/b9fa47a1-f3ba-429a-8eb2-80610cccdab2" />
<img width="1002" height="1093" alt="image" src="https://github.com/user-attachments/assets/3fec18c2-5584-4066-8614-89906700b48f" />
<img width="1007" height="826" alt="image" src="https://github.com/user-attachments/assets/244a0cdc-694f-4ada-b8e8-99bc84995a57" />
<img width="1027" height="581" alt="image" src="https://github.com/user-attachments/assets/bab83c92-bca0-4bda-8805-6a3b8bc54121" />

```sql

SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands AS w
JOIN Wands_Property AS p ON w.code = p.code
WHERE w.coins_needed = (
    SELECT MIN(coins_needed)
    FROM Wands w2
    INNER JOIN Wands_Property p2 ON w2.code = p2.code
    WHERE p2.is_evil = 0 AND p.age = p2.age AND w.power = w2.power
)
ORDER BY w.power DESC, p.age DESC;

```
