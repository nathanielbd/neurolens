def generate_efficacy(patient_response, mech_symptom_data):
    # where patient_response is of the format dict[symptom] = label
    #       - this is the user input ranging from -1 to 1
    # mech_symptom_data is of the format dict[mechanic][symptom][field] = value
    # the resulting dict from this function, is what will be called when scoring each mech in a drug for ranking

    efficacy_dict = dict()

    for (mechanic, symptom_dict) in mech_symptom_data.items():
        symptom_keys = symptom_dict.keys()
        # filter to only those in patient response
        s_keys = [s for s in symptom_keys if s in patient_response.keys()]

        high_score = 0
        if len(s_keys) > 0:
            # get mech-symptom weights filtered to those in patient response
            m_s_scores = [mech_symptom_data[mechanic][k]['max_score'] for k in s_keys]
            # get labels
            labels = [patient_response[k] for k in s_keys]
            # zip together lists and take product
            pairings = zip(m_s_scores, labels)
            products = [n1*n2 for (n1, n2) in pairings]
            # take highest score, label, product
            sorted = products.sort()
            high_score = sorted.pop()
        efficacy_dict[mechanic] = high_score

    return efficacy_dict

def get_mechanics(drug_name):
    # this should return a list of mechanics for the given drug name
    return []

def score_drug(drug_name, efficacy_dict):
    # this makes no assumptions about the format of drug, but if its a list of mechanics that is formatted
    # to make key access work smoothly with efficacy_dict, that is ideal

    drug = get_mechanics(drug_name)

    eff_scores = []
    for mechanic in drug:
        score = efficacy_dict[mechanic]
        eff_scores.append(score)
    return sum(eff_scores)

