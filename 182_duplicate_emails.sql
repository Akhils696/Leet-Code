/*
LeetCode 182. Duplicate Emails

Problem summary:
- Report all duplicate emails from the Person table.
*/

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
