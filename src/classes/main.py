class User:
    def __init__(self, UserId, Role, UserName, Password):
        self.UserId = UserId
        self.Role = Role
        self.UserName = UserName
        self.Password = Password

class Prescriptions:
    def __init__(self, PrescriptionId, PrescriptionDate, TotalCost, UserId):
        self.PrescriptionId = PrescriptionId
        self.PrescriptionDate = PrescriptionDate
        self.TotalCost = TotalCost
        self.UserId = UserId

class PrescriptionDetails:
    def __init__(self, PrescriptionId, PrescriptionDetails, MedicineId, Quantity, Dosage):
        self.PrescriptionId = PrescriptionId
        self.PrescriptionDetails = PrescriptionDetails
        self.MedicineId = MedicineId
        self.Quantity = Quantity
        self.Dosage = Dosage

class Medicines:
    def __init__(self, MedicineId, MedicineName, Manufacturer, Price, ExpiryDate):
        self.MedicineId = MedicineId
        self.MedicineName = MedicineName
        self.Manufacturer = Manufacturer
        self.Price = Price
        self.ExpiryDate = ExpiryDate

class Inventories:
    def __init__(self, MedicineId, QuantityInStock):
        self.MedicineId = MedicineId
        self.QuantityInStock = QuantityInStock

# Create instances of the classes
user1 = User("user123", "Admin", "admin_user", "admin_pass")
prescription1 = Prescriptions("presc12", "2023-02-26", 150.0, "user123")
medicine1 = Medicines("med123", "Aspirin", "Appollo Pharma", 5.99, "2023-12-31")
inventory1 = Inventories("med123", 100)

# Access and modify instance attributes
print(user1.UserId)  # Access the UserId attribute of the User instance
print(prescription1.TotalCost)  # Access the TotalCost attribute of the Prescriptions instance
print(user1.UserName)
user1.UserName = "new_username"  # Modify the UserName attribute of the User instance
# Demonstrate relationships between objects
print(user1.UserName) 
prescription_detail1 = PrescriptionDetails("presc123", "Take one tablet", "med123", 2, 1)
print(prescription_detail1.Dosage)  # Access the Quantity attribute of the PrescriptionDetails instance
