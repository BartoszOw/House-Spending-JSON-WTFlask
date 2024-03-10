from flask import Flask, request, render_template, redirect, url_for, jsonify, abort
from forms import ExpensesForm, IncomeForm
from models import expenses, income

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













if __name__ == '__main__':
    app.run(debug=True, port=7000)
    app.app_context()