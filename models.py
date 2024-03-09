import json

class Expenses:

    def __init__(self):
        try:
            with open('data/expenses.json', 'r') as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        return self.expenses
    
    def create(self, data):
        data.pop('csrf_token')
        self.expenses.append(data)
    
    def save_all(self):
        with open('data/expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.expenses[id] = data
        self.save_all()

    def get(self, id):
        return self.expenses[id]
    
    def delete(self, id):
        self.expenses.remove(id)
        self.save_all()

    def suma(self):
        x = sum([i['quantity'] for i in list(self.expenses)])
        return x
 
expenses = Expenses()


class Income:

    def __init__(self):
        try:
            with open('data/income.json', 'r') as f:
                self.income = json.load(f)
        except FileNotFoundError:
            self.income = []

    def all(self):
        return self.income
    
    def create(self, data):
        data.pop('csrf_token')
        self.income.append(data)
    
    def save_all(self):
        with open('data/income.json', 'w') as f:
            json.dump(self.income, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.income[id] = data
        self.save_all()

    def get(self, id):
        return self.income[id]
    
    def delete(self, id):
        self.income.remove(id)
        self.save_all()

    def suma(self):
        x = sum([i['quantity'] for i in list(self.income)])
        return x
    

income = Income()