/*
LeetCode 181. Employees Earning More Than Their Managers

Problem summary:
- Find employees whose salary is greater than their manager's salary.
- Return the employee names.
*/

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
    ON e.managerId = m.id
WHERE e.salary > m.salary;
