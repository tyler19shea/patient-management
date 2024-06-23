# patient-management
This project keeps track of patient data including their name, diagnosis, insurance, visits, and the amount due to the healthcare system. It saves its information into a sqlite database to keep track of the data. It also utilizes Object-Oriented Programming (OOP) to allow for a modular, maintainable, and scalable design.

# Features
- Add New Patients: Input details for a new patient and store them in the system.
- Update Patient Data: Modify existing patient information such as name, diagnosis, insurance, visits, and amount due.
- Track Patient Visits: Increase the number of visits and update the amount due based on the patient's insurance type.
- Remove Patients: Delete patient records from the system.
- View All Patient Data: Retrieve and display all patient data stored in the sqlite database.

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

- fetch_all_data: Reads patient data from the sqlite database.
- display_headers: Displays headers for the patient data. 
- get_all_ids: Retrieves all patient IDs from the data.
- id_generator: Generates a unique ID for new patients.
- initial_visit: Collects input for a new patient's details and returns a Patient object.
- add_patient_data: Adds a new patient's data to the sqlite database.
- update_data: Updates specific patient information in the sqlite database.
- get_patient_data: Retrieves data for a specific patient based on ID.
- patient_visit: Records a new visit for a patient and updates their data.
- patient_payment: Updates the amount due for a specific patient based on ID.
- remove_patient: Removes a patient's data from the database.
- main_menu: Provides a menu for user interaction to perform various operations.
# Usage
# Clone the Repository:

Copy code
```
git clone https://github.com/tyler19shea/patient-management.git
cd patient-management
```
# Run the Program:
Copy code:
```
python patient_management.py
```
# Interact with the Menu:

- See Patients Data: View all stored patient information.
- See Single Patients Data: View specific patient information.
- Add New Patient: Input details for a new patient.
- Update Patient Data: Modify existing patient information.
- Patient Visit: Record a new visit for a patient.
- Patient Payment: Alter amount due because of payment by patient.
- Remove Patient: Delete a patient record.
- Exit: Exit the application.
# Example:
```
Welcome to patient management!! What would you like to do?
      1. See Patients Data
      2. See Single Patient
      3. Add New Patient
      4. Update Patient Data
      5. Patient Visit
      6. Patient Payment
      7. Remove Patient
      8. Exit
What would you like to do (type number): 3
What is the patient's name: John Doe
What is the patient's Diagnosis: Flu
What is the patient's Insurance: anthem
New patient added successfully!
```
