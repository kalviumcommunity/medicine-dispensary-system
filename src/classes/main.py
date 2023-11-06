import inquirer
from getpass import getpass
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
    def __init__(self, PrescriptionId, PrescriptionDetails, Medicines, Dosage, quantity):
        self.PrescriptionId = PrescriptionId
        self.PrescriptionDetails = PrescriptionDetails
        self.Medicines = Medicines  # Medicines is a list of medicine objects
        self.Dosage = Dosage
        self.quanity = quantity


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

medicines_dict = {
    1: Medicines(1, 'Aspirin', 'Bayer', 5.99, '2023-10-31'),
    2: Medicines(2, 'Ibuprofen', 'Advil', 7.49, '2023-09-30'),
    3: Medicines(3, 'Amoxicillin', 'Pfizer', 12.75, '2024-05-15'),
    4: Medicines(4, 'Lisinopril', 'Novartis', 8.25, '2024-03-28'),
    5: Medicines(5, 'Atorvastatin', 'AstraZeneca', 14.99, '2023-12-31'),
    6: Medicines(6, 'Paracetamol', 'Johnson & Johnson', 4.50, '2023-11-30'),
    7: Medicines(7, 'Omeprazole', 'Mylan', 9.99, '2024-02-28'),
    8: Medicines(8, 'Losartan', 'Teva', 11.25, '2024-04-15'),
    9: Medicines(9, 'Metformin', 'Merck', 6.75, '2023-10-31'),
    10: Medicines(10, 'Prednisone', 'GSK', 7.99, '2023-12-15')
}

medicines_Inventory = [
    Inventories(1,300),
    Inventories(2,300),
    Inventories(3,370),
    Inventories(4,300),
    Inventories(5,300),
    Inventories(6,300),
    Inventories(7,300),
    Inventories(8,300),
    Inventories(9,300),
    Inventories(10,309)
]

print('Welcome to Our Medicine Dispensary system')

def getAllMedicines(medicines_dict, medicines_Inventory):
    for key, val in medicines_dict.items():
        print(f'The total inventory balance of {val.MedicineName} is {medicines_Inventory[key-1].QuantityInStock}')

def AddMedicines(Id, amount):
    for inventory in medicines_Inventory:
        if inventory.MedicineId == Id:
            inventory.QuantityInStock += amount
    print(f'You have successfully updated the stock of the medicine with {Id} by adding {amount} of medicines')

while True:
    print('1. View Prescriptions')
    print('2. View the Medicines Inventory')
    print('quit() to exit the system')
    user_input = input(": ")
    
    if user_input == '2':
        print('You are in  Medicine Inventories')
        print('Type the number and hit enter to see the inventories')
        print('a. View all the medicines in the Inventories....')
        print('b. update the inventory...')
        input_for_inventory = input(': ')
        if input_for_inventory == 'a':     
            getAllMedicines(medicines_dict, medicines_Inventory)
        elif input_for_inventory == 'b':
            AddMedicines(4,8)
            AddMedicines(5,21)
            AddMedicines(1,18)
            AddMedicines(6,28)
            AddMedicines(4,18)
    elif user_input == 'quit()':
        break








