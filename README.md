# patient-management
This project keeps track of patient data including their name, diagnosis, insurance, visits, and the amount due to the healthcare system. It saves its information into an SQLite database to keep track of the data. It also utilizes Object-Oriented Programming (OOP) principles and provides a graphical user interface (GUI) using Tkinter.

# Features
- Patient Data Management: Add, update, delete, and view patient data.
- Database Storage: Utilizes SQLite for persistent storage of patient information.
- GUI: User-friendly graphical interface using Tkinter.
- Visit Tracking: Automatically updates the number of visits and the amount due based on insurance type.
- Unique ID Generation: Generates unique IDs for new patients.

# Project Structure
- patient.py: Contains the 'Patient' class, representing patient data.
- database.py: Contains the 'PatientManagement' class, which handles all database interactions such as adding, updating, fetching, and removing patient data.
- gui.py: Contains the 'PatientMangementGUI' class, which handlws the Tkinter GUI setup and user interactions.
- main.py: Entry point of the application, initializing the 'PatientManagementGUI' with the SQLite database file.

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
Methods:
- '__init__': Initializes the database connnection and creates the patients table if it does not exist.
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
  
# PatientManagementGUI
Handles the graphical user interface using Tkinter.
Methods:
- '__init__': Initializes the GUI and the PatientManagement instance.
- create_gui: Sets up the GUI layout and event handlers.
- display_data: Displays all patient data.
- display_single_data: Displays single patient data based on id.
- add_new_patient: Prompts the user to add a new patient.
- update_patient_data: Prompts the user to update a patient's data.
- record_patient_visit: Records a new visit for a patient.
- patient_pay: Updates the amount due based on a payment.
- remove_patient_data: Prompts the user to remove a patient.
# Usage
# Clone the Repository:

Copy code
```
git clone https://github.com/tyler19shea/patient-management.git
cd patient-management
```
# How to Run the Program:
- Ensure you have Python installed on your system.
- Install the required libraries: 
```pip install tk```
- Clone this repository or download the source code.
- Run the main.py file to start the application: 
```python main.py```

# Usage
- See Patients Data: View all patient records stored in the database.
- See Single Patient Data: View specific patient record in the database.
- Add New Patient: Add a new patient by providing their name, diagnosis, and insurance type.
- Update Patient Data: Update a specific attribute for an existing patient.
- Add Patient Visit: Updates the patients visit and increases the amount due for the patient.
- Add Patient Payment: Update the amount due by entering the amount the patient paid.
- New Patient Visit: Record a new visit for a patient, which updates their number of visits and the amount due.
- Remove Patient: Remove a patient from the database
