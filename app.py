from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response
from forms import ExpensesForm, IncomeForm
from models import expenses, income
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dada'




@app.route('/', methods=['GET', 'POST'])
def spending_main():

    form_inc = IncomeForm()
    form_exp = ExpensesForm()
    error = ''

    res_exp = expenses.suma()
    res_inc = income.suma()
    res = res_inc - res_exp

    if request.method == "POST":

        if form_exp.validate_on_submit():
            if 'exp_btn' in request.form:
                expenses.create(form_exp.data)
                expenses.save_all()

        if form_inc.validate_on_submit():
            if 'inc_btn' in request.form:
                income.create(form_inc.data)
                income.save_all()

        return redirect(url_for('spending_main'))
    
    return render_template('index.html',res=res, form_exp=form_exp, error=error, income=income.all(), form_inc=form_inc, expenses=expenses.all())

@app.route('/exp/<int:index>', methods=['GET', 'POST'])
def exp_details(index):
    
    exp = expenses.get_one(index - 1)
    form_exp = ExpensesForm(data = exp)

    if request.method == "POST":

        if form_exp.validate_on_submit():
            expenses.update(index - 1, form_exp.data)
        return redirect(url_for('spending_main'))
        
    
    return render_template('exp_details.html', form_exp=form_exp, index=index)



@app.route('/inc/<int:index>', methods=['GET', 'POST'])
def inc_details(index):
    
    inc = income.get_one(index - 1)
    form_inc = IncomeForm(data = inc)

    if request.method == "POST":

        if form_inc.validate_on_submit():
            income.update(index - 1, form_inc.data)
        return redirect(url_for('spending_main'))
        
    
    return render_template('inc_details.html', form_inc=form_inc, index=index)



@app.route('/delete_expense/<int:index>', methods=['POST'])
def delete_expense(index):

    if request.method == "POST":
        expense_index = index - 1
        expenses.delete(expense_index) 

    return redirect(url_for('spending_main'))


@app.route('/delete_income/<int:index>', methods=['POST'])
def delete_income(index):

    if request.method == "POST":
        income_index = index - 1
        income.delete(income_index) 

    return redirect(url_for('spending_main'))




# REST API



@app.route('/api/v1/expenses/', methods=["GET"])
def expenses_api_v1():
    return jsonify(expenses.all())

@app.route('/api/v1/income/', methods=["GET"])
def income_api_v1():
    return jsonify(income.all())


# Pobieranie REST Wydatkow i Przychodow

@app.route("/api/v1/expenses/<int:expense_id>", methods=["GET"])
def get_expense(expense_id):
    expense = expenses.get(expense_id)
    if not expense:
        abort(404)
    return jsonify({"expense": expense})

@app.route("/api/v1/income/<int:inc_id>", methods=["GET"])
def get_income(inc_id):
    inc = income.get(inc_id)
    if not inc:
        abort(404)
    return jsonify({"inc": inc})

# Custom wiadomosci REST bledow

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code' : 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


# Tworzenie REST Wydatkow i Przychodow

@app.route('/api/v1/expenses/', methods=['POST'])
def create_expense():
    if not request.json or not 'title' in request.json:
        abort(400)
    expense = {
        'id': str(uuid.uuid4()),
        'title': request.json['title'],
        'type': request.json.get('type', 'Rozrywka'),
        'quantity': request.json.get('quantity', 0)
    }
    expenses.create_rest(expense)
    return jsonify({'expense': expense}), 201

@app.route('/api/v1/income/', methods=['POST'])
def create_income():
    if not request.json or not 'title' in request.json:
        abort(400)
    inc = {
        'id': str(uuid.uuid4()),
        'title': request.json['title'],
        'type': request.json.get('type', 'Praca'),
        'quantity': request.json.get('quantity', 0)
    }
    income.create_rest(inc)
    return jsonify({'expense': inc}), 201

# Usuwanie REST wydatkow i przychodow

@app.route('/api/v1/expenses/<int:index>', methods=["DELETE"])
def delete_exp(index):
    res = expenses.delete(index - 1)
    if not res:
        abort(404)
    return jsonify({'res': res})

@app.route('/api/v1/income/<int:index>', methods=["DELETE"])
def delete_inc(index):
    res = income.delete(index - 1)
    if not res:
        abort(404)
    return jsonify({'res': res})


# Nadpisywanie REST 

@app.route("/api/v1/income/<int:index>", methods=["PUT"])
def update_income(index):
    inc = income.get(index - 1)
    if not inc:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'type' in data and not isinstance(data.get('type'), str),
        'quantity' in data and not isinstance(data.get('quantity'), int)
    ]):
        abort(400)
    inc = {
        'title': data.get('title', inc['title']),
        'type': data.get('type', inc['type']),
        'quantity': data.get('quantity', inc['quantity'])
    }
    income.update_rest(index - 1, inc)
    return jsonify({'inc': inc})

@app.route("/api/v1/expenses/<int:index>", methods=["PUT"])
def update_exp(index):
    expense = expenses.get(index - 1)
    if not expense:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'type' in data and not isinstance(data.get('type'), str),
        'quantity' in data and not isinstance(data.get('quantity'), int)
    ]):
        abort(400)
    expense = {
        'title': data.get('title', expense['title']),
        'type': data.get('type', expense['type']),
        'quantity': data.get('quantity', expense['quantity'])
    }
    expenses.update_rest(index - 1, expense)
    return jsonify({'expense': expense})

if __name__ == '__main__':
    app.run(debug=True, port=7000)
    app.app_context()