# -*- coding: utf-8 -*-

import drug_data

with open("data/drug_lists/depression/depression_drugs.txt", "r") as d:
    depression_drugs = d.read().split("\n")
    
with open("data/drug_lists/schizophrenia/schizophrenia_drugs.txt", "r") as s:
    schizophrenia_drugs = s.read().split("\n")

depression_drugs = [d.lower() for d in depression_drugs]
schizophrenia_drugs = [s.lower() for s in schizophrenia_drugs]

depression_mechanics = drug_data.scrape_mechanics("data/drug_lists/depression/depression_drugs.txt")
schizophrenia_mechanics = drug_data.scrape_mechanics("data/drug_lists/schizophrenia/schizophrenia_drugs.txt")

def mechanics_to_string_list(dm):
    """Generate a nested list of strings from a nested list of tuples of strings"""
    depression_mechanics_list = []
    for m in dm:
        il = []
        try:
            mechanics_tuple_list = m["mechanics"]
            for t in mechanics_tuple_list:
                il.append(" ".join(t))
            depression_mechanics_list.append(il)
        except TypeError:
            depression_mechanics_list.append(il)
    return depression_mechanics_list

def try_to_retreive(d, k, e):
    try:
        return d[k]
    except TypeError:
        return e
    
    
depression_mechanics_list = mechanics_to_string_list(depression_mechanics)
            
#dml = map(lambda x: map(lambda y: " ".join(y), x), [m["mechanics"] for m in depression_mechanics])
depression_df_dict = {"name": depression_drugs, "drugbank_id": [d["db_id"] for d in depression_mechanics], "mechanics": depression_mechanics_list, "diagnosis": ["depression" for n in range(len(depression_mechanics_list))]}

schizophrenia_mechanics_list = mechanics_to_string_list(schizophrenia_mechanics)
schizophrenia_df_dict = {"name": schizophrenia_drugs, "drugbank_id": [try_to_retreive(d, "db_id", "") for d in schizophrenia_mechanics], "mechanics": schizophrenia_mechanics_list, "diagnosis": ["schizophrenia" for n in range(len(schizophrenia_mechanics_list))]}

import pandas as pd
d_df = pd.DataFrame(depression_df_dict)
s_df = pd.DataFrame(schizophrenia_df_dict)
all_drugs = pd.concat([d_df, s_df], axis=0)
#all_drugs.to_csv("data/csv/drugs_lowercase_names.csv", index=False)

#depression_dict = {k:z for k, z in zip(depression_drugs, depression_mechanics_list)}
#schizophrenia_dict = {k:z for k, z in zip(schizophrenia_drugs, schizophrenia_mechanics_list)}
#all_drugs = {k:v for k, v in zip((depression_drugs + schizophrenia_drugs),
#                                 depression_mechanics_list + schizophrenia_mechanics_list)}
#depression_dict.update(schizophrenia_dict)