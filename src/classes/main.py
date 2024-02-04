from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    @abstractmethod
    def display_info(self):
        pass

class User(Entity):
    def __init__(self, UserId, Role, UserName, Password):
        super().__init__(UserId)
        self.Role = Role
        self.UserName = UserName
        self._Password = Password

    def getUserName(self):
        print('The Name of the user is',self.UserName)

    def display_info(self):
        print(f"User ID: {self.entity_id}, Role: {self.Role}, UserName: {self.UserName}")

    def getUserPassword(self):
        print('Password is', self._Password)

class Prescriptions(Entity):
    def __init__(self, PrescriptionId, PrescriptionDate, TotalCost, UserId):
        super().__init__(PrescriptionId)
        self.PrescriptionDate = PrescriptionDate
        self.TotalCost = TotalCost
        self.UserId = UserId
    

    def display_info(self):
        print(f"Prescription ID: {self.entity_id}, Date: {self.PrescriptionDate}, Total Cost: {self.TotalCost}")

class PrescriptionDetails(Entity):
    def __init__(self, PrescriptionId, PrescriptionDetails, MedicineId, Quantity, Dosage):
        super().__init__(PrescriptionId)
        self.PrescriptionDetails = PrescriptionDetails
        self.MedicineId = MedicineId
        self.Quantity = Quantity
        self.Dosage = Dosage

    def display_info(self):
        print(f"Prescription Detail ID: {self.entity_id}, Details: {self.PrescriptionDetails}, Quantity: {self.Quantity}")

class Medicines(Entity):
    def __init__(self, MedicineId, MedicineName, Manufacturer, Price, ExpiryDate):
        super().__init__(MedicineId)
        self.MedicineName = MedicineName
        self.Manufacturer = Manufacturer
        self.Price = Price
        self.ExpiryDate = ExpiryDate

    def display_info(self):
        print(f"Medicine ID: {self.entity_id}, Name: {self.MedicineName}, Price: {self.Price}")

class Inventories(Entity):
    def __init__(self, MedicineId, QuantityInStock):
        super().__init__(MedicineId)
        self.QuantityInStock = QuantityInStock

    def display_info(self):
        print(f"Inventory for Medicine ID {self.entity_id}: Quantity in Stock: {self.QuantityInStock}")

# Example usage:
user1 = User("user123", "Admin", "admin_user", "admin_pass")
prescription1 = Prescriptions("presc12", "2023-02-26", 150.0, "user123")
medicine1 = Medicines("med123", "Aspirin", "Appollo Pharma", 5.99, "2023-12-31")
inventory1 = Inventories("med123", 100)

# Display information using the abstract method
user1.display_info()
prescription1.display_info()
medicine1.display_info()
inventory1.display_info()

#  Display information using getter methods for encapsulation concept
# user1.getUserPassword()
user1.getUserName()

