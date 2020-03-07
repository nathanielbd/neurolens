import requests, spacy
from statistics import mean
from bs4 import BeautifulSoup
from metapub import PubMedFetcher
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def scrape_related_ids(pm_id):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location ="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   options=chrome_options)
        # NOTE: chrome 82 error resolved by replacing chrome install with chrome dev install
        driver.get('https://pubmed.ncbi.nlm.nih.gov/' + pm_id)
        button = driver.find_element_by_css_selector('#similar > div > a')
        button.click()

        show_more = driver.find_element_by_css_selector('#search-results > section > div.search-results-paginator.next-results-paginator.has-nav > button > span')
        show_more.click()

        text = driver.page_source
        soup = BeautifulSoup(text, 'html.parser')
        queries = [x.text for x in soup.find_all('script') if 'searchQuery' in x.text]
        query_text = queries[0]

        split_up = query_text.partition('searchQuery: "')
        id_list = split_up[2].partition('"')[0].split(',')
        return id_list
    except:
        return None


def measure_similarity_abstracts(nlp, pmid):
    def scrape_related_abstracts(pm_id):
        related_ids = scrape_related_ids(pm_id)

        if len(related_ids) > 8:
            related_ids = related_ids[:8]

        abstracts = []

        for related in related_ids:
            starter = 'https://pubmed.ncbi.nlm.nih.gov/'
            link = starter + related

            data = requests.get(link).text
            soup = BeautifulSoup(data, 'html.parser')
            abstract_header = soup.find('div', {'id': 'en-abstract'})
            try:
                abstract = str(abstract_header.p.string).strip()
                abstracts.append(abstract)
            except:
                pass

        return abstracts

    fetch = PubMedFetcher()
    exemplary = fetch.article_by_pmid(pmid).abstract

    doc1 = nlp(exemplary)

    scores = []

    for abstract in scrape_related_abstracts(pmid):
        doc2 = nlp(abstract)
        scores.append(doc1.similarity(doc2))

    return mean(scores)


def measure_all_from_query(query):
    fetch = PubMedFetcher()
    pm_ids = fetch.pmids_for_query(query)

    if len(pm_ids) > 8:
        pm_ids = pm_ids[:8]

    scores = []
    nlp = spacy.load('en_core_sci_lg')
    for id in pm_ids:
        scores.append((id, measure_similarity_abstracts(nlp, id)))

    return scores

with open('data/sq_files/sq_19.txt', 'r') as f:
    for line in f:
        try:
            scores = measure_all_from_query(line.strip())
            query = line.strip()
            print(f'{query}:{scores}')
        except:
            pass

with open('data/sq_files/sq_20.txt', 'r') as f:
    for line in f:
        try:
            scores = measure_all_from_query(line.strip())
            query = line.strip()
            print(f'{query}:{scores}')
        except:
            pass

