/*
LeetCode 183. Customers Who Never Order

Problem summary:
- Report the names of customers who never placed an order.
*/

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.id IS NULL;
