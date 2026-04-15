/*
LeetCode 177. Nth Highest Salary

Problem summary:
- Return the nth highest distinct salary from the Employee table.
- If there are fewer than n distinct salaries, return null.
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
    RETURN (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET N
    );
END
