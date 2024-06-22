# patient-management
This project keeps track of patient data including their name, diagnosis, insurance, visits, and the amount due to the healthcare system. It saves its information into a CSV file to keep track of the data. It also utilizes Object-Oriented Programming (OOP) to allow for a modular, maintainable, and scalable design.

# Features
- Add New Patients: Input details for a new patient and store them in the system.
- Update Patient Data: Modify existing patient information such as name, diagnosis, insurance, visits, and amount due.
- Track Patient Visits: Increase the number of visits and update the amount due based on the patient's insurance type.
- Remove Patients: Delete patient records from the system.
- View All Patient Data: Retrieve and display all patient data stored in the CSV file.

# Classes
# Patient
Represents a patient with the following attributes:

- name: Name of the patient.
- id: Unique identifier for the patient.
- diagnosis: Diagnosis of the patient.
- insurance: Insurance type of the patient.
- visits: Number of visits made by the patient.
- amount_due: Amount due by the patient.
# Methods:

- __str__: Returns a string representation of the patient's data.
- visit_increase: Increases the number of visits and updates the amount due based on the insurance type.
# PatientManagement
Handles the operations related to patient data management:

- fetch_all_data: Reads patient data from the CSV file.
- get_all_ids: Retrieves all patient IDs from the data.
- id_generator: Generates a unique ID for new patients.
- initial_visit: Collects input for a new patient's details and returns a Patient object.
- add_patient_data: Appends a new patient's data to the CSV file.
- update_data: Updates specific patient information in the CSV file.
- get_patient_data: Retrieves data for a specific patient based on ID.
- patient_visit: Records a new visit for a patient and updates their data.
- remove_patient: Removes a patient's data from the CSV file.
- main_menu: Provides a menu for user interaction to perform various operations.
# Usage
# Clone the Repository:

Copy code
```
git clone https://github.com/yourusername/patient-management-system.git
cd patient-management-system
```
# Ensure the CSV file (patient-management.csv) exists:

Copy:
```
Name,ID,Diagnosis,Insurance,Visits,Amount-Due
```
# Run the Program:
Copy code:
```
python patient_management.py
```
# Interact with the Menu:

- See Patients Data: View all stored patient information.
- Add New Patient: Input details for a new patient.
- Update Patient Data: Modify existing patient information.
- New Patient Visit: Record a new visit for a patient.
- Remove Patient: Delete a patient record.
- Exit: Exit the application.
# Example:
```
Welcome to patient management!! What would you like to do?
    1. See Patients Data
    2. Add New Patient
    3. Update Patient Data
    4. New Patient Visit
    5. Remove Patient
    6. Exit
What would you like to do (type number): 2
What is the patient's name: John Doe
What is the patient's Diagnosis: Flu
What is the patient's Insurance: anthem
New patient added successfully!
```
