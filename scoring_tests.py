# -*- coding: utf-8 -*-
import pandas as pd
import json
import random
import ast
DRUG_DB = pd.read_csv("data/csv/drugs_lowercase_names.csv")

with open("data/dictionaries/sq_output.json") as sq:
    MECHANIC_SYMPTOM_DICT = json.loads(sq.read())

with open("data/symptoms.txt") as s:
    SYMPTOMS = s.read().split('\n')
    
from scoring import generate_efficacy, get_mechanics, score_drug
# from drug_table import schizophrenia_mechanics_list, depression_mechanics_list
depression_mechanics_list = [ast.literal_eval(x) for x in list(DRUG_DB["mechanics"].loc[DRUG_DB["diagnosis"] == "depression"])]
schizophrenia_mechanics_list = [ast.literal_eval(x) for x in list(DRUG_DB["mechanics"].loc[DRUG_DB["diagnosis"] == "schizophrenia"])]
with open("data/drug_lists/depression/depression_drugs.txt", "r") as d:
    depression_drugs = d.read().split("\n")
    
with open("data/drug_lists/schizophrenia/schizophrenia_drugs.txt", "r") as s:
    schizophrenia_drugs = s.read().split("\n")

# Test get_mechanics
compare = True
for d, t in zip((depression_drugs + schizophrenia_drugs), (depression_mechanics_list + schizophrenia_mechanics_list)):
    compare = compare and (get_mechanics(d, DRUG_DB) == t)
assert compare

# Test generate_efficacy()
all_zero_response = {k:0 for k in SYMPTOMS}
all_one_response = {k:1 for k in SYMPTOMS}
all_negative_one_response = {k:-1 for k in SYMPTOMS}

    

efficacy_dict_all_1 = generate_efficacy(all_one_response, MECHANIC_SYMPTOM_DICT)
efficacy_dict_all_n1 = generate_efficacy(all_negative_one_response, MECHANIC_SYMPTOM_DICT)
efficacy_dict_all_0 = generate_efficacy(all_zero_response, MECHANIC_SYMPTOM_DICT)
    
# Test  score_drug
sorted([(score_drug(d[0].upper() + d[1:], efficacy_dict_all_1, DRUG_DB), d[0].upper() + d[1:])
for d in (depression_drugs + schizophrenia_drugs)])
sorted([(score_drug(d[0].upper() + d[1:], efficacy_dict_all_n1, DRUG_DB), d[0].upper() + d[1:])
for d in (depression_drugs + schizophrenia_drugs)])
sorted([(score_drug(d, efficacy_dict_all_0, DRUG_DB), d[0].upper() + d[1:])
for d in (depression_drugs + schizophrenia_drugs)])

# Generate and process random responses
# Seems like the top 3 usually include Olanzapine, Clozapine, Aripiprazole, and Quetiapine
responses = {k:[] for k in [d[0].upper() + d[1:] for d in (depression_drugs + schizophrenia_drugs)]}
for n in range(500):
    random_response = sorted([(score_drug(d, 
                               generate_efficacy({k:random.uniform(-1, 1) for k in SYMPTOMS}, MECHANIC_SYMPTOM_DICT),
                               DRUG_DB), d[0].upper() + d[1:])
                    for d in (depression_drugs + schizophrenia_drugs)], reverse=True)
    for (eff, drug) in random_response:
        responses[drug].append(eff)
        
# These are always 0, maybe they're not well studied
all(map(lambda x: x[0] == 0, responses["Amineptine"])) # Illicit/withdrawn according to drugbank https://www.drugbank.ca/drugs/DB04836
all(map(lambda x: x[0] == 0, responses["Nomifensine"])) # Withdrawn according to drugbank https://www.drugbank.ca/drugs/DB04821
all(map(lambda x: x[0] == 0, responses["Perospirone"])) # Experimental
