import pandas as pd
from random import randint


class Patient:
    def __init__(self, name, id, diagnosis, insurance, visits, amount_due) -> None:
        self.name = name
        self.id = id
        self.diagnosis = diagnosis
        self.insurance = insurance
        self.visits = visits
        self.amount_due = amount_due

    def __str__(self) -> str:
        return f'{self.name},{self.id},{self.diagnosis},{self.insurance},{self.visits},{self.amount_due}\n'
    
    def visit_increase(self):
        if self.insurance.lower() == 'anthem':
            self.amount_due += 20
        elif self.insurance.lower() == 'medicare':
            self.amount_due += 10
        else:
            self.amount_due += 60
        self.visits += 1


class PatientManagement:
    def __init__(self, filename):
        self.filename = filename

    def fetch_all_data(self):
        return pd.read_csv(self.filename)

    def get_all_ids(self):
        df = self.fetch_all_data()
        return df['ID'].tolist()

    def id_generator(self):
        patient_ids = self.get_all_ids()
        number = randint(1, 10)
        count = 1
        while number in patient_ids and count < 10:
            number = randint(1, 10)
            count += 1
        if count >= 10:
            print('Invalid amount of ids available!')
            return None
        else:
            return number

    def initial_visit(self):
        name = input('What is the patient\'s name: ')
        id = self.id_generator()
        if id:
            diagnosis = input('What is the patient\'s Diagnosis: ')
            insurance = input('What is the patient\'s Insurance: ').lower()
            visits = 1
            if insurance.lower() == 'anthem':
                amount_due = 20
            elif insurance.lower() == 'medicare':
                amount_due = 10
            else:
                amount_due = 60
            return Patient(name, id, diagnosis, insurance, visits, amount_due)
        else:
            return None

    def add_patient_data(self, patient):
        with open(self.filename, 'a') as f:
            f.write(str(patient))

    def update_data(self, id, update_item, update_value):
        df = self.fetch_all_data()
        if id in df['ID'].astype(str).values:
            df.loc[df['ID'].astype(str) == id, update_item] = update_value
            df.to_csv(self.filename, index=False)
            print(f'ID {id} was updated!')
        else:
            print('ID not in Database!')

    def get_patient_data(self, id):
        df = self.fetch_all_data()
        if id in df['ID'].astype(str).values:
            return df.loc[df['ID'].astype(str) == id]
        else:
            print(f'ID {id} not found in the database.')
            return None

    def patient_visit(self, id):
        df = self.fetch_all_data()
        if id in df['ID'].astype(str).values:
            patient_data = df.loc[df['ID'].astype(str) == id].iloc[0]
            patient = Patient(
                patient_data['Name'],
                patient_data['ID'],
                patient_data['Diagnosis'],
                patient_data['Insurance'],
                patient_data['Visits'],
                patient_data['Amount-Due']
            )
            patient.visit_increase()
            self.update_data(id, 'Visits', patient.visits)
            self.update_data(id, 'Amount-Due', patient.amount_due)
        else:
            print(f'ID {id} not found in the database.')

    def patient_payment(self, id, amount_paid):
        df = self.fetch_all_data()
        if id in df['ID'].astype(str).values:
            patient_data = df.loc[df['ID'].astype(str) == id].iloc[0]
            amount_due_updated = int(patient_data['Amount-Due']) - amount_paid
            self.update_data(id, 'Amount-Due', amount_due_updated)
            print(f'ID {id} amount due was updated!')
        else:
            print(f'ID {id} not found in the database.')

    def remove_patient(self, id):
        df = self.fetch_all_data()
        if id in df['ID'].astype(str).values:
            df = df[df['ID'].astype(str) != id]
            df.to_csv(self.filename, index=False)
            print(f'Patient with ID {id} has been removed.')
        else:
            print(f'ID {id} not found in the database.')

    def main_menu(self):
        while True:
            print('''\nWelcome to patient management!! What would you like to do?
                  1. See Patients Data
                  2. See Single Patient
                  3. Add New Patient
                  4. Update Patient Data
                  5. New Patient Visit
                  6. Patient Payment
                  7. Remove Patient
                  8. Exit''')
            selection = int(input('What would you like to do (type number): '))
            if selection == 1:
                print(self.fetch_all_data())
            elif selection == 2:
                id = input('What is the ID of the Patient you want to see: ')
                print(self.get_patient_data(id))
            elif selection == 3:
                new_patient = self.initial_visit()
                if new_patient:
                    self.add_patient_data(new_patient)
            elif selection == 4:
                id = input('What is the ID of the Patient you would like to update: ')
                update_item = input('What is the item you wish to update (Name, Diagnosis, Insurance, Visits, Amount-Due): ')
                update_value = input(f'What is the new {update_item}: ')
                self.update_data(id, update_item, update_value)
            elif selection == 5:
                id = input('What is the Patient\'s ID: ')
                self.patient_visit(id)
            elif selection == 6:
                id = input('What is the Patient\'s ID: ')
                amount_paid = int(input('How much was paid: '))
                self.patient_payment(id, amount_paid)
            elif selection == 7:
                id = input('What is the Patient\'s ID: ')
                self.remove_patient(id)
            elif selection == 8:
                print('Exiting...')
                break
            else:
                print('Invalid selection. Please try again.')


# Example usage
if __name__ == "__main__":
    patient_management = PatientManagement('./patient-management.csv')
    patient_management.main_menu()
