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
        if self.insurance == 'anthem':
            self.amount_due += 20
        elif self.insurance == 'medicare':
            self.amount_due += 10
        else:
            self.amount_due += 60
        self.visits += 1

