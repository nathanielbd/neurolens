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
    results = sorted([(score_drug(d[0].upper() + d[1:], generate_efficacy({k.replace(" ","_"):float(responses[k.replace(" ","_")]) for k in SYMPTOMS}, MECHANIC_SYMPTOM_DICT), DRUG_DB), d[0].upper() + d[1:]) for d in drugs], reverse=True)
    return results

def get_desc(drug):
    DRUG_DB = pd.read_csv("data/csv/drugs_lowercase_names.csv")
    desc = DRUG_DB.loc[DRUG_DB["name"] == drug.lower()]["description"].values[0]
    return desc