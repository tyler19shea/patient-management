import tkinter as tk
from tkinter import messagebox, simpledialog
from patientManagement import PatientManagement
from patient import Patient

class PatientManagementGUI:
    def __init__(self, db_name):
        self.patient_management = PatientManagement(db_name)
        self.create_gui()

    def create_gui(self):
        root = tk.Tk()
        root.title("Patient Management System")
        root.minsize(300, 300)

        tk.Button(root, text="See Patients Data", command=self.display_data).pack(fill=tk.X)
        tk.Button(root, text="See Single Patients Data", command=self.display_single_data).pack(fill=tk.X)
        tk.Button(root, text="Add New Patient", command=self.add_new_patient).pack(fill=tk.X)
        tk.Button(root, text="Update Patient Data", command=self.update_patient_data).pack(fill=tk.X)
        tk.Button(root, text="Add Patient Visit", command=self.record_patient_visit).pack(fill=tk.X)
        tk.Button(root, text="Patient Payment", command=self.patient_pay).pack(fill=tk.X)
        tk.Button(root, text="Remove Patient", command=self.remove_patient_data).pack(fill=tk.X)
        tk.Button(root, text="Exit", command=root.quit).pack(fill=tk.X)

        root.mainloop()

    def display_data(self):
        data = self.patient_management.fetch_all_data()
        if data:
            display_text = '\n'.join([f"\nID: {row[0]} \nName: {row[1]} {row[2]} \nDOB: {row[3]} \nDiagnosis: {row[4]} \nInsurance: {row[5]} \nVisits: {row[6]} \nAmount Due: {row[7]}" for row in data])
        else:
            display_text = "No data found"
        messagebox.showinfo('Patient Data', display_text)
    
    def display_single_data(self):
        id = simpledialog.askstring("Input", "What is the Patients ID?")
        if id in self.patient_management.get_all_ids(): 
            data = list(self.patient_management.get_patient_data(id))
            if data:
                display_text = f'ID: {data[0]} \nName: {data[1]} \nDiagnosis: {data[2]} \nInsurance: {data[3]} \nVisits: {data[4]} \nAmount Due: {data[5]}'
            else:
                display_text = f"No data found for {id}"
        else:
            display_text = f'{id} not found in database'
        messagebox.showinfo('Patient Data', display_text)
    
    def add_new_patient(self):
        first_name = simpledialog.askstring("Input","What is the new Patients First Name?")
        if not first_name:
            return
        last_name = simpledialog.askstring("Input", "What is the new Patients Last Name?")
        if not last_name:
            return
        id = self.patient_management.id_generator()
        if not id:
            messagebox.showerror('Error', 'Invalid amount of IDs available!')
            return
        birthday = simpledialog.askstring("Input", "What is their birthday? (MM/DD/YYYY)")
        if not birthday:
            return
        diagnosis = simpledialog.askstring("Input", "What is the new Patients Diagnosis?")
        if not diagnosis:
            return
        insurance = simpledialog.askstring("Input", "What is the new Patient\'s Insurance").lower()
        visits = 1
        if insurance == 'anthem':
            amount_due = 20
        elif insurance == 'medicare':
            amount_due = 10
        else:
            amount_due = 60
        patient = Patient(first_name, last_name, id, birthday, diagnosis, insurance, visits, amount_due)
        self.patient_management.add_patient_data(patient)
        messagebox.showinfo('Success', f'Patient {first_name} {last_name} added with an id of {id} successfully!')
    
    def update_patient_data(self):
        id = simpledialog.askinteger("Input", "What is the ID of the Patient you would like to update?")
        if not id:
            return
        update_item = simpledialog.askstring("Input", "What is the item you wish to update (name, diagnosis, insurance, visits, amount_due)?").lower()
        if not update_item or update_item not in ['name', 'diagnosis', 'insurance', 'visits', 'amount_due']:
            return
        update_value = simpledialog.askstring("Input", f"What is the new {update_item}")
        if not update_value:
            return
        if self.patient_management.update_patient_data(id, update_item, update_value):
            messagebox.showinfo('Success', f'Patient with ID {id} has been updated.')
        else:
            messagebox.showerror('Error', f'ID {id} not in Database!')
    
    def record_patient_visit(self):
        id = simpledialog.askstring("Input", "Whats the ID of the Patient?")
        if not id:
            return
        if self.patient_management.patient_visit(id):
            messagebox.showinfo('Success', f'Patient with ID {id} has been updated.')
        else:
            messagebox.showerror('Error', f'ID {id} not in Database!')

    def patient_pay(self):
        id = simpledialog.askstring("Input", "Whats the ID of the Patient that paid?")
        if not id:
            return
        amount_paid = simpledialog.askfloat("Input", "How much was paid?")
        if not amount_paid:
            return
        if self.patient_management.patient_payment(id, amount_paid):
            messagebox.showinfo("Success", f"Patient with ID {id} has been updated.")
        else:
            messagebox.showerror("Error", f"ID {id} not in database!")
        
    def remove_patient_data(self):
        id = simpledialog.askstring("Input", "What is the Patients ID?")
        if not id:
            return
        if self.patient_management.remove_patient(id):
            messagebox.showinfo("Success", f"Patient with ID {id} has been removed.")
        else:
            messagebox.showerror("Error", f"ID {id} was not found in database!")
    
    
    

