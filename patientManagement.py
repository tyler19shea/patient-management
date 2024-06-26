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
                    "first name" TEXT NOT NULL,
                    "last name" TEXT NOT NULL,
                    DOB DATE NOT NULL,
                    diagnosis TEXT NOT NULL,
                    insurance TEXT NOT NULL,
                    visits INTEGER NOT NULL,
                    "amount due" REAL NOT NULL
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
            return None
        else:
            return number

    def add_patient_data(self, patient):
        with self.conn:
            self.conn.execute("INSERT INTO patients (\"first name\", \"last name\", id, DOB, diagnosis, insurance, visits, \"amount due\") VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                              (patient.first_name, patient.last_name, patient.id, patient.birthday, patient.diagnosis, patient.insurance, patient.visits, patient.amount_due))

    def update_patient_data(self, id, update_item, update_value):
        with self.conn:
            cursor = self.conn.execute("SELECT id FROM patients WHERE id=?", (id,))
            if cursor.fetchone():
                self.conn.execute(f"UPDATE patients SET \"{update_item}\" = ? WHERE id = ?", (update_value, id))
                return True
            else:
                return False

    def get_patient_data(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                return None

    def patient_visit(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM patients WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                patient = Patient(row[1], row[0], row[2], row[3], row[4], row[5], row[6])
                patient.visit_increase()
                self.conn.execute("UPDATE patients SET visits = ?, \"amount due\" = ? WHERE id = ?", 
                                  (patient.visits, patient.amount_due, id))
                return True
            else:
                return False
        
    def patient_payment(self, id, amount_paid):
        row = self.get_patient_data(id)
        if row:
            updated_amount = row[-1] - amount_paid
            self.conn.execute("UPDATE patients SET \"amount due\" = ? WHERE id = ?", 
                            (updated_amount, id))
            return True
        else:
            return False

    def remove_patient(self, id):
        with self.conn:
            cursor = self.conn.execute("SELECT id FROM patients WHERE id=?", (id,))
            if cursor.fetchone():
                self.conn.execute("DELETE FROM patients WHERE id=?", (id,))
                return True
            else:
                return False           
