-- Drop Table
-- Drop Table Address, Cart, Category, Employee, Order_Item, Orders, Product, Shipment, User_Account, Customer;

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
    State VARCHAR(100),
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

-- Alter Customer table to add foreign key constraints
ALTER TABLE Customer
ADD CONSTRAINT fk_customer_user_account
FOREIGN KEY (User_Acc_ID) REFERENCES User_Account(User_Acc_ID);