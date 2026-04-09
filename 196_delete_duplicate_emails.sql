/*
LeetCode 196. Delete Duplicate Emails

Problem summary:
- Delete duplicate emails from the Person table.
- Keep only the row with the smallest id for each email.
*/

DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;
