# -*- coding: utf-8 -*-

#import requests
#import spacy
#from statistics import mean
#from bs4 import BeautifulSoup
from metapub import PubMedFetcher
import json
import pickle
#import os
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
## Substitute system specific driver
#driver = webdriver.Firefox()

def make_queries(diagnosis, target_file):
    """Make a list of queries given a dianosis and its corresponding target file"""
    with open(target_file) as f:#"drug_lists/depression/depression_targets.txt") as dt:
    # Drop last element '' created by splitting along  \n
        l = f.read().split("\n")[:-1]
    return [t + " " + diagnosis for t in l]


def get_abstract_from_pmid(pmid, fetcher):
    """Get abstract of an article given its pmid"""
    try:
        return fetcher.article_by_pmid(pmid).abstract
    # Import MetaPubError so it catches that specificaly
    except:
        return None

depression_queries = make_queries("depression", "drug_lists/depression/depression_targets.txt")
fetch = PubMedFetcher()
depression_pmids = [fetch.pmids_for_query(q) for q in depression_queries]
with open("temp/depression_pmids.json", "w") as dpjson:
    dpjson.write(json.dumps(depression_pmids))
# Not sure this part works yet
depression_abstracts = [[get_abstract_from_pmid(p, fetch) for p in l] for l in depression_pmids]
with open("temp/depression_abstracts.json", "w") as dajson:
    dajson.write(json.dumps(depression_abstracts))

schizophrenia_queries = make_queries("schizophrenia",
                                     "drug_lists/schizophrenia/schizophrenia_targets.txt")
fetch = PubMedFetcher()
schizophrenia_pmids = [fetch.pmids_for_query(q) for q in schizophrenia_queries]
with open("temp/schizophrenia_pmids.json", "w") as spjson:
    spjson.write(json.dumps(schizophrenia_pmids))
schizophrenia_abstracts = [[get_abstract_from_pmid(p, fetch) for p in l] for l in schizophrenia_pmids]
with open("temp/schizophrenia_abstracts.json", "w") as sajson:
    sajson.write(json.dumps(schizophrenia_abstracts))

with open("drug_lists/depression/depression_targets.txt") as dt:
    # Drop last element '' created by splitting along  \n
        depression_targets = dt.read().split("\n")[:-1]
with open("drug_lists/schizophrenia/schizophrenia_targets.txt") as st:
    # Drop last element '' created by splitting along  \n
        schizophrenia_targets = st.read().split("\n")[:-1]
        
#depression_dict = {k:v for k, v in zip(depression_targets, depression_abstracts)}
#with open("temp/depression_dict.json", "w") as dd:
#    dd.write(json.dumps(depression_dict))
#
#with open("temp/schizophrenia_abstracts.json", "r") as s:
#    schizophrenia_abstracts = json.loads(s.read())
#schizophrenia_dict = {k:v for k, v in zip(schizophrenia_targets, schizophrenia_abstracts)}
#
#diagnosis_to_target_dict = {"schizophrenia": schizophrenia_dict,
#                  "depression": depression_dict}
#
#with open("dictionaries/diagnosis_to_target_dict.json", "w") as dtd:
#    dtd.write(json.dumps(diagnosis_to_target_dict))
#     
#with open("dictionaries/diagnosis_to_target_dict.p", "wb") as dtdp:
#    pickle.dump(diagnosis_to_target_dict, dtdp)
    
depression_dict = {"Diagnosis": ["depression" for n in range(len(depression_abstracts))], "Target": depression_targets, "Abstracts": depression_abstracts}
schizophrenia_dict = {"Diagnosis": ["depression" for n in range(len(schizophrenia_abstracts))], "Target": schizophrenia_targets, "Abstracts": schizophrenia_abstracts}
depression_df, schizophrenia_df = (pd.DataFrame(depression_dict), pd.DataFrame(schizophrenia_dict))
diagnoses_target_df = pd.concat([depression_df, schizophrenia_df], axis=0)
diagnosis_target_df.to_csv("csv/diagnosis_target.csv")