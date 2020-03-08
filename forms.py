from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DecimalRangeField

class DiagnosisForm(FlaskForm):
    diagnosis = SelectField('Diagnosis',choices=[('Schizophrenia','Schizophrenia'), ('Depression','Depression')])
    submit = SubmitField('Submit')

class DepressionDrugForm(FlaskForm):
    drug = SelectField('Prescribed Drug', choices=[('Citalopram',
        'Citalopram'), ('Escitalopram', 'Escitalopram'), ('Fluoxetine',
        'Fluoxetine'), ('Fluvoxamine', 'Fluvoxamine'), ('Paroxetine',
        'Paroxetine'), ('Sertraline', 'Sertraline'),
        ('Duloxetine','Duloxetine'), ('Venlafaxine', 'Venlafaxine'),
        ('Desvenlafaxine', 'Desvenlafaxine'), ('Duloxetine', 'Duloxetine'),
        ('Milnacipran','Milnacipran'), ('Venlafaxine','Venlafaxine'),
        ('Amineptine','Amineptine'), ('Bupropion', 'Bupropion'),
        ('Methylphenidate', 'Methylphenidate'), ('Nomifensine',
            'Nomifensine')])
    submit = SubmitField('Submit')

class SchizophreniaDrugForm(FlaskForm):
    drug = SelectField('Prescribed Drug',
    choices=[('Aripiprazole','Aripiprazole'), ('Clozapine', 'Clozapine'),
    ('Olanzapine', 'Olanzapine'), ('Paliperidone', 'Paliperdone'),
    ('Perospirone', 'Perospirone'), ('Risperidone', 'Risperidone'),
    ('Cariprazine', 'Cariprazine'), ('Quetiapine', 'Quetiapine'), ('Zotepine',
        'Zotepine')])
    submit = SubmitField('Submit')

class SymptomsForm(FlaskForm):
    cognitive_symptoms = DecimalRangeField('Cognitive Symptoms')
    negative_symptoms = DecimalRangeField('Negative Symptoms')
    avolition = DecimalRangeField('Avolition')
    extrapyramidal = DecimalRangeField('Extrapyramidal')
    positive_symptoms_psychosis = DecimalRangeField('Positive Symptoms Psychosis')
    depression = DecimalRangeField('Depression')
    insomnia = DecimalRangeField('Insomnia')
    anxiety = DecimalRangeField('Anxiety')
    weight_gain = DecimalRangeField('Weight Gain')
    apathy = DecimalRangeField('Apathy')
    motivation = DecimalRangeField('Motivation')
    stress = DecimalRangeField('Stress')
    fatigue = DecimalRangeField('Fatigue')
    suicidal_thoughts = DecimalRangeField('Suicidal Thoughts')
    agitation = DecimalRangeField('Agitation')
    submit = SubmitField('Submit')


class ProceedForm(FlaskForm):
    submit = SubmitField('Go')
