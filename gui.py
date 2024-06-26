import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from patientManagement import PatientManagement
from patient import Patient

class PatientManagementGUI:
    def __init__(self, db_name):
        self.patient_management = PatientManagement(db_name)
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Patient Management System")
        self.root.minsize(300, 300)

        ttk.Button(self.root, text="See Patients Data", command=self.display_data).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="See Single Patients Data", command=self.display_single_data_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Add New Patient", command=self.add_new_patient).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Update Patient Data", command=self.update_patient_data_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Add Patient Visit", command=self.record_patient_visit_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Patient Payment", command=self.patient_pay_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Remove Patient", command=self.remove_patient_data_window).pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(fill=tk.X, padx=5, pady=5)

        self.root.mainloop()

    def display_data(self):
        data = self.patient_management.fetch_all_data()
        display_window = tk.Toplevel(self.root)
        display_window.title("Patients Data")

        if data:
            cols = ("ID", "First Name", "Last Name", "DOB", "Diagnosis", "Insurance", "Visits", "Amount Due")
            tree = ttk.Treeview(display_window, columns=cols, show='headings')
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            for row in data:
                tree.insert("", "end", values=row)
            tree.pack(fill=tk.BOTH, expand=True)
        else:
            messagebox.showinfo('Patient Data', "No data found.")
    
    def display_single_data_window(self):
        single_patient_window = tk.Toplevel(self.root)
        single_patient_window.title("View Patient by ID")

        tk.Label(single_patient_window, text="Patient ID:").grid(row=0, column=0)
        id_entry = tk.Entry(single_patient_window)
        id_entry.grid(row=0, column=1)

        def display_single_data():
            id =  id_entry.get()
            if id in self.patient_management.get_all_ids(): 
                data = self.patient_management.get_patient_data(id)
                if data:
                    result_window = tk.Toplevel(single_patient_window)
                    result_window.title(f"Patient Data for {id}")
                    cols = ("ID", "First Name", "Last Name", "DOB", "Diagnosis", "Insurance", "Visits", "Amount Due")
                    tree = ttk.Treeview(result_window, columns=cols, show='headings')
                    for col in cols:
                        tree.heading(col, text=col)
                        tree.column(col, width=100)
                    tree.insert("", "end", values=data)
                    tree.pack(fill=tk.BOTH, expand=True)
                else:
                    messagebox.showinfo("Patient Data", f"No data found for {id}")
            else:
                messagebox.showerror("Error", f"{id} not found in database.")

        ttk.Button(single_patient_window, text="Display Single Patient", command=display_single_data).grid(row=4, columnspan=2)
    
    def add_new_patient(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Patient")

        tk.Label(add_window, text="First Name:").grid(row=0, column=0)
        first_name_entry = tk.Entry(add_window)
        first_name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Last Name:").grid(row=1, column=0)
        last_name_entry = tk.Entry(add_window)
        last_name_entry.grid(row=1, column=1)

        tk.Label(add_window, text="DOB (MM/DD/YYYY):").grid(row=2, column=0)
        dob_entry = tk.Entry(add_window)
        dob_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Diagnosis:").grid(row=3, column=0)
        diagnosis_entry = tk.Entry(add_window)
        diagnosis_entry.grid(row=3, column=1)

        tk.Label(add_window, text="Insurance:").grid(row=4, column=0)
        insurance_entry = tk.Entry(add_window)
        insurance_entry.grid(row=4, column=1)

        def add_patient():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            dob = dob_entry.get()
            diagnosis = diagnosis_entry.get()
            insurance = insurance_entry.get().lower()
            visits = 1
            amount_due = 20 if insurance == 'anthem' else 10 if insurance == 'medicare' else 60

            id = self.patient_management.id_generator()
            if not id:
                messagebox.showerror('Error', 'Invalid amount of IDs available!')
                return

            patient = Patient(first_name, last_name, id, dob, diagnosis, insurance, visits)
            self.patient_management.add_patient_data(patient)
            messagebox.showinfo('Success', f'Patient {first_name} {last_name} added successfully with id of {id}!')
            add_window.destroy()

        ttk.Button(add_window, text="Add Patient", command=add_patient).grid(row=5, columnspan=2)
    
    def update_patient_data_window(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Patient Data")

        tk.Label(update_window, text="Patient ID:").grid(row=0, column=0)
        id_entry = tk.Entry(update_window)
        id_entry.grid(row=0, column=1)

        tk.Label(update_window, text="Field to Update:").grid(row=1, column=0)
        field_entry = tk.Entry(update_window)
        field_entry.grid(row=1, column=1)

        tk.Label(update_window, text="New Value:").grid(row=2, column=0)
        value_entry = tk.Entry(update_window)
        value_entry.grid(row=2, column=1)

        def update_patient():
            id = int(id_entry.get())
            field = field_entry.get().lower()
            value = value_entry.get()
            if self.patient_management.update_patient_data(id, field, value):
                messagebox.showinfo('Success', f'Patient with ID {id} has been updated.')
            else:
                messagebox.showerror('Error', 'ID not in Database!')
            update_window.destroy()

        ttk.Button(update_window, text="Update Patient", command=update_patient).grid(row=3, columnspan=2)
    
    def record_patient_visit_window(self):
        visit_window = tk.Toplevel(self.root)
        visit_window.title("Add Patient Visit")

        tk.Label(visit_window, text="Patient ID: ").grid(row=0, column=0)
        id_entry = tk.Entry(visit_window)
        id_entry.grid(row=0, column=1)

        def record_patient_visit():
            id = id_entry.get()
            if self.patient_management.patient_visit(id):
                messagebox.showinfo('Success', f'Patient with ID {id} has been updated.')
            else:
                messagebox.showerror('Error', f'ID {id} not in Database!')
            visit_window.destroy()
        ttk.Button(visit_window, text="Record Patient Visit", command=record_patient_visit).grid(row=2, columnspan=2)

    def patient_pay_window(self):
        pay_window = tk.Toplevel(self.root)
        pay_window.title("Patient Payment")

        tk.Label(pay_window, text="Patient ID: ").grid(row=0, column=0)
        id_entry = tk.Entry(pay_window)
        id_entry.grid(row=0, column=1)

        tk.Label(pay_window, text="Amount Paid: ").grid(row=1, column=0)
        payment_entry = tk.Entry(pay_window)
        payment_entry.grid(row=1, column=1)

        def patient_pay():
            id = id_entry.get()
            payment = float(payment_entry.get())
            if self.patient_management.patient_payment(id, payment):
                messagebox.showinfo('Success', f'Patient with ID {id} has been updated.')
            else:
                messagebox.showerror('Error', f'ID {id} not in Database!')
            pay_window.destroy()

        ttk.Button(pay_window, text="Payment for ID", command=patient_pay).grid(row=2, columnspan=2)
        
    def remove_patient_data_window(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Patient From Database")

        tk.Label(remove_window, text="Patient ID to remove: ").grid(row=0, column=0)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1)

        def remove_patient_data():
            id = id_entry.get()
            if self.patient_management.remove_patient(id):
                messagebox.showinfo("Success", f"Patient with ID {id} has been removed.")
            else:
                messagebox.showerror("Error", f"ID {id} was not found in database!")
            remove_window.destroy()
        
        ttk.Button(remove_window, text="Remove Patient", command=remove_patient_data).grid(row=2, columnspan=2)
    
    
    

