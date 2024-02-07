--  DDl commands concepts
-- Create
-- User Table
CREATE TABLE User (
    UserId INT PRIMARY KEY,
    Role VARCHAR(255),
    UserName VARCHAR(255),
    Password VARCHAR(255)
);

-- Prescriptions Table
CREATE TABLE Prescriptions (
    PrescriptionId INT PRIMARY KEY,
    PrescriptionDate DATE,
    TotalCost DECIMAL(10, 2),
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES User(UserId)
);

-- PrescriptionDetails Table
CREATE TABLE PrescriptionDetails (
    PrescriptionId INT,
    PrescriptionDetails VARCHAR(255),
    Dosage VARCHAR(255),
    Quantity INT,
    FOREIGN KEY (PrescriptionId) REFERENCES Prescriptions(PrescriptionId),
    PRIMARY KEY (PrescriptionId)
);

-- Medicines Table
CREATE TABLE Medicines (
    MedicineId INT PRIMARY KEY,
    MedicineName VARCHAR(255),
    Manufacturer VARCHAR(255),
    Price DECIMAL(10, 2),
    ExpiryDate DATE
);

-- Inventories Table
CREATE TABLE Inventories (
    MedicineId INT,
    QuantityInStock INT,
    FOREIGN KEY (MedicineId) REFERENCES Medicines(MedicineId),
    PRIMARY KEY (MedicineId)
);

INSERT INTO Medicines (MedicineId, MedicineName, Manufacturer, Price, ExpiryDate)
VALUES
(1, 'Paracetamol', 'ABC Pharmaceuticals', 5.99, '2024-12-31'),
(2, 'Ibuprofen', 'XYZ Pharmaceuticals', 8.49, '2024-10-15'),
(3, 'Aspirin', 'PQR Laboratories', 3.25, '2024-09-30'),
(4, 'Amoxicillin', 'DEF Pharmaceuticals', 12.99, '2024-06-20'),
(5, 'Loratadine', 'GHI Laboratories', 7.75, '2024-11-28'),
(6, 'Ciprofloxacin', 'JKL Pharmaceuticals', 14.50, '2024-08-15'),
(7, 'Omeprazole', 'MNO Laboratories', 6.85, '2024-02-28'),
(8, 'Metformin', 'PQR Pharmaceuticals', 9.25, '2024-07-10'),
(9, 'Losartan', 'STU Laboratories', 11.30, '2024-04-15'),
(10, 'Atorvastatin', 'XYZ Pharmaceuticals', 15.75, '2024-06-30'),
(11, 'Hydrochlorothiazide', 'UVW Laboratories', 4.99, '2024-09-20'),
(12, 'Prednisone', 'RST Pharmaceuticals', 8.25, '2024-05-25'),
(13, 'Diazepam', 'MNO Laboratories', 3.99, '2024-01-10'),
(14, 'Tramadol', 'EFG Pharmaceuticals', 6.50, '2024-12-05'),
(15, 'Warfarin', 'ABC Laboratories', 7.20, '2024-03-15'),
(16, 'Lisinopril', 'HIJ Pharmaceuticals', 5.65, '2024-04-30'),
(17, 'Fluoxetine', 'XYZ Laboratories', 4.75, '2024-08-10'),
(18, 'Levothyroxine', 'PQR Pharmaceuticals', 10.50, '2024-03-20'),
(19, 'Gabapentin', 'JKL Laboratories', 9.80, '2024-05-01'),
(20, 'Albuterol', 'UVW Pharmaceuticals', 8.15, '2024-02-15');

-- select * from Medicines; 
--  These all are the small examples of how we can perform data analysis using sql with the real world data 
-- Average price of Medicines of each Manufacturer
select Manufacturer,avg(price) from Medicines group by Manufacturer;

-- How many companies do we have business relationships with?
select count(distinct Manufacturer) from Medicines;

-- Medicines which expires in the month of march
select MedicineName, ExpiryDate from Medicines where month(ExpiryDate) = 3;
-- From whom we buy more
select Manufacturer,count(*) from Medicines group by Manufacturer order by count(*) desc
limit 1;

-- top three most expensive Medicines and their Manufacturer
select Manufacturer, MedicineName, Price from Medicines order by Price desc limit 3;


