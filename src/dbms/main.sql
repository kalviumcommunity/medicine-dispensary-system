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

update Medicines set MedicineName = 'Paracetamol123' where  MedicineId = 3;
commit;
update Medicines set MedicineName = 'new_Medcines' where  MedicineId = 5;
rollback;
INSERT INTO Medicines (MedicineId, MedicineName, Manufacturer, Price, ExpiryDate) 
VALUES 
    (41, 'Paracetamol', 'ABC Pharmaceuticals', 10.50, '2024-12-31'),
    (42, 'Amoxicillin', 'XYZ Pharma', 15.75, '2023-09-15'),
    (43, 'Omeprazole', 'PQR Drugs', 20.25, '2025-05-20'),
    (44, 'Aspirin', 'LMN Pharmaceuticals', 5.99, '2023-07-10'),
    (45, 'Ibuprofen', 'ABC Pharmaceuticals', 8.99, '2024-10-05')
   ;
commit;

 -- rollback
 update Medicines set MedicineName = 'iboprufen1234' where MedicineId = 42;
 
 savepoint
 update Medicines set MedicineName = 'iboprufen1234' where MedicineId = 41;
 savepoint X;
 update Medicines set MedicineName = 'new_medicine' where MedicineId = 41;
 savepoint Y;
 update Medicines set MedicineName = 'newMedicine1234' where MedicineId = 41;
 rollback to X;
select * from medicines;



