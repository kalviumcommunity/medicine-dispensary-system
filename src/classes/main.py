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

# # Create instances of the classes
user1 = User("user123", "Admin", "admin_user", "admin_pass")
# prescription1 = Prescriptions("presc12", "2023-02-26", 150.0, "user123")
# medicine1 = Medicines("med123", "Aspirin", "Appollo Pharma", 5.99, "2023-12-31")
# inventory1 = Inventories("med123", 100)

# # Access and modify instance attributes
# print(user1.UserId)  # Access the UserId attribute of the User instance
# print(prescription1.TotalCost)  # Access the TotalCost attribute of the Prescriptions instance

# user1.UserName = "new_username"  # Modify the UserName attribute of the User instance
# # Demonstrate relationships between objects
# prescription_detail1 = PrescriptionDetails("presc123", "Take one tablet", "med123", 2, 1)
# print(prescription_detail1.Dosage)  # Access the Quantity attribute of the PrescriptionDetails instance


# # Proof of concept for Array of objects
# # Create instances of User
# user1 = User(1, 'Admin', 'admin_user', 'admin_password')
# user2 = User(2, 'Doctor', 'doctor_user', 'doctor_password')

# # Create instances of Medicines
# medicine1 = Medicines(101, 'Medicine A', 'Manufacturer X', 10.0, '2024-01-01')
# medicine2 = Medicines(102, 'Medicine B', 'Manufacturer Y', 8.0, '2023-12-31')

# # Create instances of Inventories
# inventory1 = Inventories(101, 100)
# inventory2 = Inventories(102, 50)


# # Create instances of PrescriptionDetails
# prescription_details1 = PrescriptionDetails(1, 'Take after meals', 101, 2, '2 tablets/day')
# prescription_details2 = PrescriptionDetails(2, 'Take before bedtime', 102, 1, '1 tablet/day')

# # Create instances of Prescriptions and associate with User
# prescription1 = Prescriptions(101, '2023-10-10', 20.0, user1)
# prescription2 = Prescriptions(102, '2023-10-11', 8.0, user2)

# # Create an array (list) of Prescriptions instances
# prescriptions_array = [prescription1, prescription2]

# # Create an array (list) of PrescriptionDetails instances 
# prescription_details_array = [prescription_details1, prescription_details2]

