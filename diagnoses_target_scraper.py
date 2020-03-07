# -*- coding: utf-8 -*-

#import requests
#import spacy
#from statistics import mean
#from bs4 import BeautifulSoup
from metapub import PubMedFetcher
import json
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

