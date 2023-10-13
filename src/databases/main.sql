CREATE TABLE User (
    UserId INT PRIMARY KEY,
    Role VARCHAR(255),
    UserName VARCHAR(255),
    Password VARCHAR(255)
);

CREATE TABLE Prescriptions (
    PrescriptionId INT PRIMARY KEY,
    PrescriptionDate DATE,
    TotalCost DECIMAL(10, 2),
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES User(UserId)
);

CREATE TABLE PrescriptionDetails (
    PrescriptionId INT,
    PrescriptionDetails TEXT,
    MedicineId INT,
    Quantity INT,
    Dosage VARCHAR(255),
    FOREIGN KEY (PrescriptionId) REFERENCES Prescriptions(PrescriptionId),
    FOREIGN KEY (MedicineId) REFERENCES Medicines(MedicineId)
);

CREATE TABLE Medicines (
    MedicineId INT PRIMARY KEY,
    MedicineName VARCHAR(255),
    Manufacturer VARCHAR(255),
    Price DECIMAL(10, 2),
    ExpiryDate DATE
);

CREATE TABLE Inventories (
    MedicineId INT PRIMARY KEY,
    QuantityInStock INT,
    FOREIGN KEY (MedicineId) REFERENCES Medicines(MedicineId)
);
