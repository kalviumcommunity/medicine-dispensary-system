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

CREATE Role admin;
CREATE Role Manager;
CREATE Role employee;

grant all privileges on Users to admin;
grant select,update,insert on Users to Manager;
grant select on Users to employee;
