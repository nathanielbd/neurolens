from scoring import *
import json
import numpy as np

def generate_recommendations(responses):
    diagnosis = responses['diagnosis'].lower()
    drug = responses['drug'].lower()
    submit = responses['submit'].lower()
    if diagnosis == 'depression':
        with open("data/drug_lists/depression/depression_drugs.txt", "r") as d:
            # drugs = list(map(lambda x: x.lower(), d.read().split("\n")))
            drugs = d.read().split("\n")
        similarities = np.loadtxt('depression_similarities.csv')
    else:
        with open("data/drug_lists/schizophrenia/schizophrenia_drugs.txt", "r") as s:
            # drugs = list(map(lambda x: x.lower(), s.read().split("\n")))
            drugs = s.read().split("\n")
        similarities = np.loadtxt('schizophrenia_similarities.csv')
    DRUG_DB = pd.read_csv("data/csv/drugs_lowercase_names.csv")
    with open("data/dictionaries/sq_output.json") as sq:
        MECHANIC_SYMPTOM_DICT = json.loads(sq.read())
    with open("data/symptoms.txt") as s:
        SYMPTOMS = s.read().split('\n')
#    print(f"responses: {responses}")
#    print(f"symptoms: {SYMPTOMS}")
#    # score_drug() returns a tuple, first element is the score
#    results = sorted([(score_drug(d[0].upper() + d[1:], generate_efficacy({k.replace(" ","_"):int(responses[k.replace(" ","_")]) for k in SYMPTOMS}, MECHANIC_SYMPTOM_DICT), DRUG_DB)[0], d[0].upper() + d[1:]) for d in drugs])
    drug_idx = drugs.index(drug[0].upper() + drug[1:])
    #results = sorted([(score_drug(d[0].upper() + d[1:], generate_efficacy({k.replace(" ","_"):float(responses[k.replace(" ","_")]) for k in SYMPTOMS}, MECHANIC_SYMPTOM_DICT), DRUG_DB, similarities, drugs, drug_idx)[0], d[0].upper() + d[1:]) for d in drugs], reverse=True)
    all_results = sorted([(score_drug(d[0].upper() + d[1:], generate_efficacy({k.replace(" ","_"):float(responses[k.replace(" ","_")]) for k in SYMPTOMS},MECHANIC_SYMPTOM_DICT),
                                      DRUG_DB, similarities, drugs, drug_idx), d[0].upper() + d[1:]) for d in drugs],
                        reverse=True, key=lambda x: x[0][0])
    return all_results

def get_desc(drug):
    DRUG_DB = pd.read_csv("data/csv/drugs_lowercase_names.csv")
    desc = DRUG_DB.loc[DRUG_DB["name"] == drug.lower()]["description"].values[0]
    return desc
