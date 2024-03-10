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

    def create_rest(self, data):
        self.expenses.append(data)
        self.save_all()
    
    def save_all(self):
        with open('data/expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def update(self, index, data):
        data.pop('csrf_token')
        self.expenses[index] = data
        self.save_all()

    def update_rest(self, id,data):
        exp = self.get(id)
        if exp:
            index = self.expenses.index(exp)
            self.expenses[index] = data
            self.save_all()
            return True
        return False
    
    
    def get_one(self, id):
        return self.expenses[id]
    

    def get(self, id):
        todo = [todo for todo in self.all()]
        if todo[id]:
            return todo[id]
        return []
    
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

    def create_rest(self, data):
        self.income.append(data)
        self.save_all()
    
    def save_all(self):
        with open('data/income.json', 'w') as f:
            json.dump(self.income, f)

    def update(self, index, data):
        data.pop('csrf_token')
        self.income[index] = data
        self.save_all()

    def update_rest(self, id,data):
        inc = self.get(id)
        if inc:
            index = self.income.index(inc)
            self.income[index] = data
            self.save_all()
            return True
        return False
    
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