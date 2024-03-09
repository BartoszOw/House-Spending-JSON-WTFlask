from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    quantity = FloatField('quantity', validators=[DataRequired()])
    type = SelectField('type', validators=[DataRequired()],
                    choices=[('Artykuły spożywcze', 'Artykuły spożywcze'), 
                             ('Rozrywka', 'Rozrywka'),
                             ('Technologia', 'Technologia'),
                             ('Zdrowie', 'Zdrowie'),
                             ('Uzależnienie', 'Uzależnienie'),
                             ('Przedmioty użytku codziennego', 'Przedmioty użytku codziennego'),
                             ('Praca', 'Praca')] 
                      )

class IncomeForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    quantity = FloatField('quantity', validators=[DataRequired()])
    type = SelectField('type', validators=[DataRequired()],
                    choices=[('Praca', 'Praca'), 
                             ('Inwestycje', 'Inwestycje'),
                             ('Prezent', 'Prezent')] 
                      )
