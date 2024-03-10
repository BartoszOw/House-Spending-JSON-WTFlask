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

    def update(self, index, data):
        data.pop('csrf_token')
        self.expenses[index] = data
        self.save_all()
    
    def get_one(self, id):
        return self.expenses[id]
    

    def get(self, id):
        for expense in self.expenses:
            if expense.get('id') == id:
                return expense
        return None
    
    def delete(self, index):
        del self.expenses[index]
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

    def update(self, index, data):
        data.pop('csrf_token')
        self.income[index] = data
        self.save_all()
    
    def get_one(self, id):
        return self.income[id]
    


    def get(self, id):
        inc = [income for income in self.all()]
        if inc[id]:
            return inc[id]
        return []
    
    def delete(self, id):
        inc = self.get(id)
        if inc:
            self.income.remove(inc)
            self.save_all()
            return True
        return False

    def suma(self):
        x = sum([i['quantity'] for i in list(self.income)])
        return x
    

income = Income()