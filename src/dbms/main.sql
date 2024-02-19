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

-- -- DML - insert
-- INSERT INTO Medicines (MedicineId, MedicineName, Manufacturer, Price, ExpiryDate) VALUES 
-- (1, 'Aspirin', 'Bayer', 9.99, '2023-05-15'),
-- (2, 'Paracetamol', 'Johnson & Johnson', 5.49, '2023-08-20'),
-- (3, 'Ibuprofen', 'Pfizer', 12.75, '2023-06-30'),
-- (4, 'Amoxicillin', 'GlaxoSmithKline', 15.25, '2022-12-10'),
-- (5, 'Ciprofloxacin', 'Novartis', 18.99, '2024-02-28');
 
-- -- Delete 
-- delete from Medicines where MedicineName = 'Aspirin';
-- -- update
-- update Medicines set MedicineName = 'Paracetamol-omega' where MedicineName = 'Paracetamol';
-- -- select
-- select * from Medicines
