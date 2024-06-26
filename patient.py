class Patient:
    def __init__(self, first_name, last_name, id, birthday, diagnosis, insurance, visits) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.birthday = birthday
        self.diagnosis = diagnosis
        self.insurance = insurance
        self.visits = visits
        if self.insurance == 'anthem':
            self.amount_due = 20.00
        elif self.insurance == 'medicare':
            self.amount_due = 10.00
        else:
            self.amount_due = 60.00

    def __str__(self) -> str:
        return f'{self.id}, {self.first_name}, {self.last_name}, {self.birthday}, {self.diagnosis},{self.insurance},{self.visits},{self.amount_due}\n'
    
    def visit_increase(self):
        if self.insurance == 'anthem':
            self.amount_due += 20
        elif self.insurance == 'medicare':
            self.amount_due += 10
        else:
            self.amount_due += 60
        self.visits += 1

