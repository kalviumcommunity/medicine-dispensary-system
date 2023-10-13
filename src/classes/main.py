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



