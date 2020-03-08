from scoring import *
import json

def generate_recommendations(responses):
    diagnosis = responses['diagnosis'].lower()
    drug = responses['drug'].lower()
    submit = responses['submit'].lower()
    if diagnosis == 'depression':
        with open("data/drug_lists/depression/depression_drugs.txt", "r") as d:
            drugs = d.read().split("\n")
    else:
        with open("data/drug_lists/schizophrenia/schizophrenia_drugs.txt", "r") as s:
            drugs = s.read().split("\n")
    DRUG_DB = pd.read_csv("data/csv/drugs_lowercase_names.csv")
    with open("data/dictionaries/sq_output.json") as sq:
        MECHANIC_SYMPTOM_DICT = json.loads(sq.read())
    with open("data/symptoms.txt") as s:
        SYMPTOMS = s.read().split('\n')
    print(f"responses: {responses}")
    print(f"symptoms: {SYMPTOMS}")
    # score_drug() returns a tuple, first element is the score
    results = sorted([(score_drug(d[0].upper() + d[1:], generate_efficacy({k.replace(" ","_"):int(responses[k.replace(" ","_")]) for k in SYMPTOMS}, MECHANIC_SYMPTOM_DICT), DRUG_DB)[0], d[0].upper() + d[1:]) for d in drugs])
    return results

def report_data(data):
    text = str(data)
    return text
