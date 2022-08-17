-- Question 1 --
SELECT DISTINCT City
FROM customers;

SELECT COUNT(DISTINCT City) AS 'Count'
FROM customers;


-- Question 2 --
SELECT * FROM order_details;

SELECT OrderDetailID, OrderID, ProductID, MIN(Quantity) AS 'Least_Qty', MAX(Quantity) AS 'Highest_Qty'
FROM order_details;


-- Question 3 --
SELECT * FROM order_details;

SELECT SUM(Quantity) AS 'Total', AVG(Quantity) AS 'Average'
FROM order_details;


-- Question 4 --
SELECT * FROM products;

SELECT ProductID, ProductName 
FROM products 
LIMIT 4,11;
-- starting after position 4 till position 15 --


-- Question 5 --
SELECT *
FROM suppliers;

SELECT *
FROM suppliers
WHERE SupplierName LIKE "_a%";


-- Question 6 --
SELECT *
FROM customers
WHERE NOT Country IN ('USA','Canada');


-- Question 7 --
SELECT *
FROM orders
WHERE OrderDate BETWEEN '2020-01-01' AND '2021-12-31'
ORDER BY OrderDate DESC;


-- Question 8 --
SELECT DISTINCT City
FROM customers;

SELECT COUNT(DISTINCT City) AS 'Count'
FROM customers;


-- Question 9 --
SELECT * 
FROM employees
WHERE NOT FirstName IN ('Sanjay' , 'Soniya');


-- Question 10 --
CREATE TABLE SupplierDetail AS SELECT * FROM suppliers;

SELECT *
FROM SupplierDetail;


-- Question 11 --
DELETE FROM customers WHERE Country = 'Venezuela';

SELECT *
FROM customers;


-- END --