from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

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
    cognitive_symptoms = SelectField('Cognitive Symptoms', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2,'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    negative_symptoms = SelectField('Negative Symptoms', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    avolition = SelectField('Avolition', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    extrapyramidal = SelectField('Extrapyramidal', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    positive_symptoms = SelectField('Positive Symptoms', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    psychosis = SelectField('Psychosis', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    depression = SelectField('Depression', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    insomnia = SelectField('Insomnia', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    anxiety = SelectField('Anxiety', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    weight_gain = SelectField('Weight Gain', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    apathy = SelectField('Apathy', choices=[(-2, 'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    motivation = SelectField('Motivation', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    stress = SelectField('Stress', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    fatigue = SelectField('Fatigue', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    suicidal_thoughts = SelectField('Suicidal Thoughts', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    agitation = SelectField('Agitation', choices=[(-2,'Greatly Worsened Symptom'), (-2, 'Significantly Worsened Symptom'),(-1, 'Slightly Worsened Symptom'), (0, 'No effect'), (1, 'Slight Improvement in Symptom'), (2, 'Significant Improvement in Symptom'), (3, 'Great Improvement in Symptom')])
    submit = SubmitField('Submit')


class ProceedForm(FlaskForm):
    submit = SubmitField('Go')
