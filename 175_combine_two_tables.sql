/*
LeetCode 175. Combine Two Tables

Problem summary:
- Report the first name, last name, city, and state of each person.
- If a person's address is missing, report null for city and state.
*/

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;
