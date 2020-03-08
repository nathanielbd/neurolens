from flask import Flask, render_template, request, url_for, redirect
from forms import *
from model import generate_recommendations
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=["GET", "POST"])
def landing():
    title = 'Neurolens'
    form = DiagnosisForm()
    form_name = 'Try your tailored treatment'
    if request.method == 'POST':
        diagnosis = request.form.get("diagnosis")
        return redirect(url_for('drugs', diagnosis=diagnosis))
    return render_template('landing.html', title = title, form = form, form_name = form_name)

@app.route('/drugs', methods=["GET", "POST"])
def drugs():
    title = 'Neurolens'
    diagnosis = request.args.get("diagnosis")
    if diagnosis == 'Schizophrenia':
        form = SchizophreniaDrugForm()
    else:
        form = DepressionDrugForm()
    form_name = 'Select your prescribed drug'
    if request.method == 'POST':
        drug = request.form.get("drug")
        return redirect(url_for('symptoms', diagnosis=diagnosis, drug=drug))
    return render_template('drugs.html', title=title, form=form, form_name=form_name)

@app.route('/symptoms', methods=["GET", "POST"])
def symptoms():
    title = 'Neurolens'
    diagnosis = request.args.get("diagnosis")
    drug = request.args.get("drug")
    form = SymptomsForm()
    form_name = 'Tell us how {drug} has treated you'.format(drug=drug)
    if request.method == 'POST':
        symptoms = request.form
        return redirect(url_for('results', diagnosis=diagnosis, drug=drug, **symptoms))
    return render_template('symptoms.html', title=title, form=form, form_name=form_name)

@app.route('/results', methods=["GET", "POST"])
def results():
    title = 'Based on your responses, we recommend:'
    data = request.args
    recs = generate_recommendations(data)
    drug_1 = recs[0][1]
    drug_2 = recs[1][1]
    drug_3 = recs[2][1]
    return render_template('results.html', title = title, drug_1=drug_1, drug_2=drug_2, drug_3=drug_3)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
