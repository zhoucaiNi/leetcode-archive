# Write your MySQL query statement below
SELECT DISTINCT P1.Email FROM Person P1, Person P2

WHERE P1.id <> P2.id and P2.email=P1.email