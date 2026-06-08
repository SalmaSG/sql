CREATE DATABASE OnlineBookStore;
USE OnlineBookStore;
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    price DECIMAL(8,2) CHECK (price > 0),
    stock INT CHECK (stock >= 0),
    author_id INT,
    FOREIGN KEY (author_id)
    REFERENCES Authors(author_id)
);
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18)
);
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id)
    REFERENCES Customers(customer_id)
);
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10,2) CHECK (amount > 0),
    payment_method VARCHAR(50),
    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id)
);

INSERT INTO Authors
VALUES
(1,'R.K. Narayan','rk@gmail.com'),
(2,'Chetan Bhagat','chetan@gmail.com');

INSERT INTO Customers
VALUES
(101,'Amit Kumar','amit@gmail.com',25),
(102,'Priya Sharma','priya@gmail.com',30);

INSERT INTO Books
VALUES
(1001,'Malgudi Days',299,50,1),
(1002,'Five Point Someone',350,40,2);

INSERT INTO Orders
VALUES
(5001,101,'2026-06-05'),
(5002,102,'2026-06-06');

INSERT INTO Payments
VALUES
(9001,5001,299,'UPI'),
(9002,5002,350,'Credit Card');
Constraint Violation Queries
1. PRIMARY KEY Violation
INSERT INTO Authors
VALUES
(1,'New Author','new@gmail.com');

Error: Duplicate Primary Key.

2. UNIQUE Constraint Violation
INSERT INTO Customers
VALUES
(103,'Rahul','amit@gmail.com',22);

Error: Duplicate Email.

3. NOT NULL Constraint Violation
INSERT INTO Books
VALUES
(1003,NULL,250,20,1);

Error: Title cannot be NULL.

4. CHECK Constraint Violation
INSERT INTO Books
VALUES
(1004,'SQL Guide',-100,10,1);

Error: Price must be greater than 0.

5. CHECK Constraint Violation
INSERT INTO Customers
VALUES
(104,'Rohan','rohan@gmail.com',15);

Error: Age must be 18 or above.

6. FOREIGN KEY Constraint Violation
INSERT INTO Books
VALUES
(1005,'Python Basics',450,15,99);

Error: Author ID 99 does not exist.
Practice Questions
Add a UNIQUE constraint on book title.
Create a table Publishers with PRIMARY KEY and UNIQUE constraints.
Add a CHECK constraint to ensure stock is less than 1000.
Create a Reviews table with FOREIGN KEY references to Books and Customers.
Insert records that violate each constraint and observe the error messages.
Drop and recreate a constraint using ALTER TABLE.
Add a DEFAULT value for payment_method as 'UPI'.
Create a composite PRIMARY KEY in a BookOrders table.
Add ON DELETE CASCADE to Orders and Customers tables.
Display all constraints using:
SHOW CREATE TABLE Books;