from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    quantity = FloatField('quantity', validators=[DataRequired()])
    type = SelectField('type', validators=[DataRequired()],
                    choices=[(1, 'Artykuły spożywcze'), 
                             (2, 'Rozrywka'),
                             (3, 'Technologia'),
                             (4, 'Zdrowie'),
                             (5, 'Uzależnienie'),
                             (6, 'Przedmioty użytku codziennego'),
                             (7, 'Praca')] 
                      )

class IncomeForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    quantity = FloatField('quantity', validators=[DataRequired()])
    type = SelectField('type', validators=[DataRequired()],
                    choices=[(1, 'Praca'), 
                             (2, 'Inwestycje'),
                             (3, 'Prezent')] 
                      )
