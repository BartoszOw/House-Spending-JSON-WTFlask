from flask import Flask, request, render_template, redirect, url_for, jsonify
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

            



if __name__ == '__main__':
    app.run(debug=True)
    app.app_context()