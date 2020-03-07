from bs4 import BeautifulSoup
import requests


def get_drug_bank_id(drug_name):
    starter = "https://en.wikipedia.org/wiki/"
    link = starter + drug_name
    x = requests.get(link)
    soup = BeautifulSoup(x.text, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})
    if infobox:
        db_span = infobox.find('span', {'title': 'www.drugbank.ca'})
        if db_span:
            db_id = db_span.a.string
            return db_id
        else:
            return None
    else:
        return None


def drug_bank_data(db_id):
    starter = 'https://www.drugbank.ca/drugs/'
    link = starter + db_id
    x = requests.get(link)
    soup = BeautifulSoup(x.text, 'html.parser')

    # get description
    description_header = soup.find('dt')
    description = None
    while description_header.string != 'Description':
        description_header = description_header.next_sibling

    if description_header:
        if description_header.string == 'Description':
            description_header = description_header.next_sibling
            description = description_header.text

    # go to pharmacology section
    pharmacology_header = soup.find('h2', {'id': 'pharmacology'})
    conditions = []
    interactions = []
    if pharmacology_header:
        pharmacology_header = pharmacology_header.next_sibling

        # all pharmacology extraction below here
        # ----------------------------------------------- #

        # go to headers above desired fields
        conditions_header = None
        mechanics_header = None
        for x in pharmacology_header.find_all('dt'):
            if x.string == 'Associated Conditions':
                conditions_header = x

            if x.string == 'Mechanism of action':
                mechanics_header = x

        if mechanics_header:
            table = pharmacology_header.find('table', {'id': 'drug-moa-target-table'})
            table = table.tbody
            rows = table.find_all('tr')
            for row in rows:
                target = None
                action = None
                td = row.td
                if td.a:
                    target = td.a.string

                td = td.next_sibling
                if td.div:
                    action = td.div.string

                if target and action:
                    interactions.append((target, action))

        if conditions_header:
            conds_list = pharmacology_header.find('ul', {'class': 'list-unstyled table-list'})
            lines = conds_list.find_all('li')
            for line in lines:
                conditions.append(line.a.string)

    result = dict()
    result['db_id'] = db_id
    result['description'] = description
    result['conditions'] = conditions
    result['mechanics'] = interactions
    return result


def scrape_drug_data(drug_name):
    db_id = get_drug_bank_id(drug_name)
    if db_id:
        return drug_bank_data(db_id)
    else:
        return None


def scrape_mechanics(druglist_file):
    def lines2list(filename) -> list:
        with open(filename, 'r') as f:
            lines = f.readlines()

        drugs = []
        for line in lines:
            drugs.append(line.strip())

        return drugs
    drugs = lines2list(druglist_file)

    drug_dicts = []
    for drug in drugs:
        drug_dict = scrape_drug_data(drug)
        drug_dicts.append(drug_dict)

    return drug_dicts


def lines2list(filename) -> list:
    with open(filename, 'r') as f:
        lines = f.readlines()

    ll = []
    for line in lines:
        ll.append(line.strip())

    return ll

