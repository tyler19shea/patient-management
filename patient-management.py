import sqlite3
from patient import Patient
from random import randint

class PatientManagement:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    diagnosis TEXT NOT NULL,
                    insurance TEXT NOT NULL,
                    visits INTEGER NOT NULL,
                    amount_due REAL NOT NULL
                )
            """)

    def fetch_all_data(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients")
            return cursor.fetchall()

    def display_headers(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients")
            header_list = []
            for item in cursor.description:
                header_list.append(item[0])
            return header_list

    def get_all_ids(self):
        with self.conn:
            cursor = self.conn.execute("SELECT id FROM patients")
            return [row[0] for row in cursor.fetchall()]

    def id_generator(self):
        patient_ids = self.get_all_ids()
        number = randint(1, 10000)
        count = 1
        while number in patient_ids and count < 10000:
            number = randint(1, 10000)
            count += 1
        if count >= 10000:
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
            if insurance == 'anthem':
                amount_due = 20
            elif insurance == 'medicare':
                amount_due = 10
            else:
                amount_due = 60
            return Patient(name, id, diagnosis, insurance, visits, amount_due)
        else:
            return None

    def add_patient_data(self, patient):
        with self.conn:
            self.conn.execute("INSERT INTO patients (name, id, diagnosis, insurance, visits, amount_due) VALUES (?, ?, ?, ?, ?, ?)",
                              (patient.name, patient.id, patient.diagnosis, patient.insurance, patient.visits, patient.amount_due))

    def update_patient_data(self, id, update_item, update_value):
        with self.conn:
            cursor = self.conn.execute("SELECT id FROM patients WHERE id=?", (id,))
            if cursor.fetchone():
                self.conn.execute(f"UPDATE patients SET {update_item} = ? WHERE id = ?", (update_value, id))
                print(f'Patient with ID {id} has been updated.')
            else:
                print('ID not in Database!')

    def get_patient_data(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                print(f'ID {id} not found in the database.')
                return None

    def patient_visit(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                patient = Patient(row[1], row[0], row[2], row[3], row[4], row[5])
                patient.visit_increase()
                self.conn.execute("UPDATE patients SET visits = ?, amount_due = ? WHERE id = ?", 
                                  (patient.visits, patient.amount_due, id))
                print(f'Visit for patient with ID {id} has been updated.')
            else:
                print(f'ID {id} not found in the database.')
        
    def patient_payment(self, id, amount_paid):
        row = self.get_patient_data(id)
        if row:
            updated_amount = row[5] - amount_paid
            self.conn.execute("UPDATE patients SET amount_due = ? WHERE id = ?", 
                            (updated_amount, id))
            print(f"Patient with id = {id} balance has been updated")
        else:
            print('Payment update Failed.')

    def remove_patient(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT id FROM patients WHERE id=?", (id,))
            if cursor.fetchone():
                self.conn.execute("DELETE FROM patients WHERE id=?", (id,))
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
                  5. Patient Visit
                  6. Patient Payment
                  7. Remove Patient
                  8. Exit''')
            selection = int(input('What would you like to do (type number): '))
            if selection == 1:
                print(f'Headers: {self.display_headers()}')
                data = self.fetch_all_data()
                for row in data:
                    print(f'Data: {row}')
            elif selection == 2:
                id = input('What is the ID of the Patient you would like to see: ')
                print(f'Headers: {self.display_headers()}')
                print(f'Data: {self.get_patient_data(id)}')
            elif selection == 3:
                new_patient = self.initial_visit()
                if new_patient:
                    self.add_patient_data(new_patient)
            elif selection == 4:
                id = input('What is the ID of the Patient you would like to update: ')
                update_item = input('What is the item you wish to update (name, diagnosis, insurance, visits, amount_due): ')
                update_value = input(f'What is the new {update_item}: ')
                self.update_patient_data(id, update_item, update_value)
            elif selection == 5:
                id = input('What is the Patient\'s ID that visited: ')
                self.patient_visit(id)
            elif selection ==6:
                id = input('What is the Patients\'s ID that has paid: ')
                amount_paid = float(input('How much was paid: '))
                self.patient_payment(id, amount_paid)
            elif selection == 7:
                id = input('What is the ID of the Patient you would like to remove: ')
                self.remove_patient(id)
            elif selection == 8:
                print('Exiting...')
                break
            else:
                print('Invalid selection. Please try again.')


# Example usage
if __name__ == "__main__":
    patient_management = PatientManagement('patient_management.db')
    patient_management.main_menu()
