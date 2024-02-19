from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    @abstractmethod
    def display_info(self):
        pass

class User(Entity):  # Define the User class inheriting from Entity
    def __init__(self, UserId, Role, UserName, Password):
        super().__init__(UserId)
        self.Role = Role
        self.UserName = UserName
        self._Password = Password

    def display_info(self):
        print(f"User ID: {self.entity_id}, Role: {self.Role}, UserName: {self.UserName}")


class UserBuilder:
    def __init__(self):
        self.UserId = None
        self.Role = None
        self.UserName = None
        self.Password = None

    def set_user_id(self, UserId):
        self.UserId = UserId
        return self

    def set_role(self, Role):
        self.Role = Role
        return self

    def set_user_name(self, UserName):
        self.UserName = UserName
        return self

    def set_password(self, Password):
        self.Password = Password
        return self

    def build(self):
        return User(self.UserId, self.Role, self.UserName, self.Password)




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
user_builder = UserBuilder()
user1 = user_builder.set_user_id("user123").set_role("Admin").set_user_name("admin_user").set_password("admin_pass").build()
user1.display_info()

