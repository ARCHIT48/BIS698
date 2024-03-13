-- Create Cart table
CREATE TABLE Cart (
    Cart_ID INT AUTO_INCREMENT PRIMARY KEY,
    Quantity INT,
    Customer_ID INT,
    Product_ID INT
);

-- Create Customer table
CREATE TABLE Customer (
    Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Email_ID VARCHAR(100),
    Phone_No VARCHAR(100),
    Date_of_Birth DATE,
    User_Acc_ID INT
);

-- Create Order table
CREATE TABLE Orders (
    Order_ID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATETIME,
    Total_Price DECIMAL(10,2),
    Customer_ID INT,
    Shipment_ID INT
);

-- Create Order_Item table
CREATE TABLE Order_Item (
    Order_Item_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Quantity INT,
    Price DECIMAL(10,2),
    Order_ID INT,
    Product_ID INT
);

-- Create Product table
CREATE TABLE Product (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY,
    Description VARCHAR(100),
    Stock INT,
    Price DECIMAL(10,2),
    Category_ID INT
);

-- Create Address table
CREATE TABLE Address (
    Address_ID INT AUTO_INCREMENT PRIMARY KEY,
    Street_1 VARCHAR(100),
    Street_2 VARCHAR(100),
    City VARCHAR(100),
    State CHAR(2),
    Zip_Code INT(5),
    Phone_No VARCHAR(100),
    Address_Type VARCHAR(100),
    Customer_ID INT
);

-- Create Shipment table
CREATE TABLE Shipment (
    Shipment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Shipment_Date DATETIME,
    Street_1 VARCHAR(100),
    Street_2 VARCHAR(100),
    City VARCHAR(100),
    State CHAR(2),
    Zip_Code INT(5),
    Phone_No VARCHAR(100),
    Customer_ID INT
);

-- Create Category table
CREATE TABLE Category (
    Category_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100)
);

-- Create User_Account table
CREATE TABLE User_Account (
    User_Acc_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID VARCHAR(100),
    Password VARCHAR(100)
);

-- Create Employee table
CREATE TABLE Employee (
    Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
    First_Name VARCHAR(100),
    Last_Name VARCHAR(100),
    Email_ID VARCHAR(100),
    Phone_No VARCHAR(100),
    DOB DATE,
    Title VARCHAR(100),
    Date_of_Hire DATE,
    Hourly_Rate DECIMAL(4,2),
    User_Acc_ID INT
);


-- Alter Cart table to add foreign key constraints
ALTER TABLE Cart
ADD CONSTRAINT fk_cart_customer
FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID);

ALTER TABLE Cart
ADD CONSTRAINT fk_cart_product
FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID);

-- Alter Order table to add foreign key constraints
ALTER TABLE Orders
ADD CONSTRAINT fk_order_customer
FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID);

ALTER TABLE Orders
ADD CONSTRAINT fk_order_shipment
FOREIGN KEY (Shipment_ID) REFERENCES Shipment(Shipment_ID);

-- Alter Order_Item table to add foreign key constraints
ALTER TABLE Order_Item
ADD CONSTRAINT fk_order_item_order
FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID);

ALTER TABLE Order_Item
ADD CONSTRAINT fk_order_item_product
FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID);

-- Alter Address table to add foreign key constraints
ALTER TABLE Address
ADD CONSTRAINT fk_address_customer
FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID);

ALTER TABLE Shipment
ADD CONSTRAINT fk_shipment_customer
FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID);

-- Alter Employee table to add foreign key constraints
ALTER TABLE Employee
ADD CONSTRAINT fk_employee_user_account
FOREIGN KEY (User_Acc_ID) REFERENCES User_Account(User_Acc_ID);





-- Insert into Customer table
INSERT INTO Customer (First_Name, Last_Name, Email_ID, Phone_No, Date_of_Birth, User_Acc_ID) VALUES
('John', 'Doe', 'john@example.com', '123-456-7890', '1990-05-15', 1),
('Alice', 'Smith', 'alice@example.com', '987-654-3210', '1985-08-25', 2),
('Bob', 'Johnson', 'bob@example.com', '555-555-5555', '1992-12-10', 3),
('Emily', 'Brown', 'emily@example.com', '444-444-4444', '1988-03-20', 4),
('Michael', 'Lee', 'michael@example.com', '111-222-3333', '1995-06-30', 5);


-- Insert into Product table
INSERT INTO Product (Description, Stock, Price, Category_ID) VALUES
('Product 1', 10, 10.00, 1),
('Product 2', 20, 15.00, 2),
('Product 3', 30, 20.00, 3),
('Product 4', 40, 25.00, 4),
('Product 5', 50, 30.00, 5);


-- Insert into Cart table
INSERT INTO Cart (Quantity, Customer_ID, Product_ID) VALUES
(2, 1, 1),
(3, 2, 2),
(1, 3, 3),
(4, 4, 4),
(2, 5, 5);

-- Insert into Order table
INSERT INTO Orders (Date, Total_Price, Customer_ID, Shipment_ID) VALUES
('2023-01-01 10:00:00', 50.00, 1, 1),
('2023-01-02 11:00:00', 75.00, 2, 2),
('2023-01-03 12:00:00', 100.00, 3, 3),
('2023-01-04 13:00:00', 125.00, 4, 4),
('2023-01-05 14:00:00', 150.00, 5, 5);

-- Insert into Order_Item table
INSERT INTO Order_Item (Name, Quantity, Price, Order_ID, Product_ID) VALUES
('Item 1', 2, 10.00, 1, 1),
('Item 2', 3, 15.00, 2, 2),
('Item 3', 4, 20.00, 3, 3),
('Item 4', 5, 25.00, 4, 4),
('Item 5', 6, 30.00, 5, 5);



-- Insert into Address table
INSERT INTO Address (Street_1, Street_2, City, State, Zip_Code, Phone_No, Address_Type, Customer_ID) VALUES
('123 Main St', 'Apt 101', 'New York', 'NY', 10001, '555-123-4567', 'Home', 1),
('456 Elm St', 'Unit B', 'Los Angeles', 'CA', 90001, '555-987-6543', 'Work', 2),
('789 Oak St', 'Suite 3', 'Chicago', 'IL', 60601, '555-555-5555', 'Home', 3),
('101 Pine St', 'Floor 4', 'Houston', 'TX', 77001, '555-444-4444', 'Work', 4),
('202 Maple St', 'Unit 5', 'San Francisco', 'CA', 94101, '555-111-2222', 'Home', 5);

-- Insert into Shipment table
INSERT INTO Shipment (Shipment_Date, Street_1, Street_2, City, State, Zip_Code, Phone_No, Customer_ID) VALUES
('2023-01-01 10:00:00', '123 Main St', 'Apt 101', 'New York', 'NY', 10001, '555-123-4567', 1),
('2023-01-02 11:00:00', '456 Elm St', 'Unit B', 'Los Angeles', 'CA', 90001, '555-987-6543', 2),
('2023-01-03 12:00:00', '789 Oak St', 'Suite 3', 'Chicago', 'IL', 60601, '555-555-5555', 3),
('2023-01-04 13:00:00', '101 Pine St', 'Floor 4', 'Houston', 'TX', 77001, '555-444-4444', 4),
('2023-01-05 14:00:00', '202 Maple St', 'Unit 5', 'San Francisco', 'CA', 94101, '555-111-2222', 5);

-- Insert into Category table
INSERT INTO Category (Name) VALUES
('Category 1'),
('Category 2'),
('Category 3'),
('Category 4'),
('Category 5');

-- Insert into User_Account table
INSERT INTO User_Account (User_ID, Password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3'),
('user4', 'password4'),
('user5', 'password5');

-- Insert into Employee table
INSERT INTO Employee (First_Name, Last_Name, Email_ID, Phone_No, DOB, Title, Date_of_Hire, Hourly_Rate, User_Acc_ID) VALUES
('Employee 1', 'Smith', 'employee1@example.com', '555-111-2222', '1990-01-01', 'Manager', '2022-01-01', 20.00, 1),
('Employee 2', 'Johnson', 'employee2@example.com', '555-222-3333', '1995-02-02', 'Sales Associate', '2022-01-02', 15.00, 2),
('Employee 3', 'Williams', 'employee3@example.com', '555-333-4444', '1988-03-03', 'Cashier', '2022-01-03', 12.00, 3),
('Employee 4', 'Brown', 'employee4@example.com', '555-444-5555', '1992-04-04', 'Stock Clerk', '2022-01-04', 10.00, 4),
('Employee 5', 'Davis', 'employee5@example.com', '555-555-6666', '1985-05-05', 'Assistant Manager', '2022-01-05', 18.00, 5);



