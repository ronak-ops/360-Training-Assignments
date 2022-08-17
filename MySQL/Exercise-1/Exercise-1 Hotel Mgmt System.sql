CREATE DATABASE Hotel_Management_System;

USE Hotel_Management_System;

CREATE TABLE Customers (
						Cust_ID int NOT NULL,
                        Cust_Name VARCHAR(50),
                        Cust_City VARCHAR(50),
                        Cust_RoomNo INT,
                        CheckIn_Time DATETIME,
                        PRIMARY KEY(Cust_ID)
                        );



DESC Customers;



INSERT INTO Customers
VALUES (1011, 'John Smith', 'Chicago', 215, '2022-03-22 15:10:00'),
	   (1012, 'Jeff Burgos', 'Newark', 112, '2022-03-19 18:30:55'),
	   (1013, 'Brenda Minto', 'Clifton', 305, '2022-03-15 16:45:00'),
       (1014, 'David Hernandez', 'Fort Lee', 411, '2022-03-10 13:35:40'),
       (1015, 'Dan Bishop', 'Jersey City', 609, '2022-03-05 19:15:00');
       

SELECT * FROM Customers;
