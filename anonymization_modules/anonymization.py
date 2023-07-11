workclass_map = {}
education_map = {}
marital_status_map = {}
occupation_map = {}
relationship_map = {}
race_map = {}
native_country_map = {}


# create a dictionary in order to map the original string values into numeric ones
def create_dictionary(s, d):
    with open("mapping_for_data/" + s + ".txt", 'r') as file:
        for e in file:
            (key, value) = e.split()
            d[key] = int(value)


# convert all values into integers for maintaining privacy
def anonymize(buckets):
    create_dictionary("workclass", workclass_map)
    create_dictionary("marital-status", marital_status_map)
    create_dictionary("occupation", occupation_map)
    create_dictionary("relationship", relationship_map)
    create_dictionary("race", race_map)
    create_dictionary("native-country", native_country_map)

    for pc, B in buckets.items():
        for b in B:
            b['Age'] = int(b['Age'])
            b['Workclass'] = workclass_map[b['Workclass']] if b['Workclass'] in workclass_map.keys() else -1
            b['Fnlwgt'] = int(b['Fnlwgt'])
            b['Education'] = int(b['Education-Num'])
            del b['Education-Num']
            b['Marital-Status'] = marital_status_map[b['Marital-Status']]
            b['Occupation'] = occupation_map[b['Occupation']] if b['Occupation'] in occupation_map.keys() else -1
            b['Relationship'] = relationship_map[b['Relationship']]
            b['Race'] = race_map[b['Race']]
            b['Sex'] = 1 if b['Sex'] == 'Male' else 2
            b['Capital-Gain'] = int(b['Capital-Gain'])
            b['Capital-Loss'] = int(b['Capital-Loss'])
            b['Hours-per-Week'] = int(b['Hours-per-Week'])
            if b['Native-Country'] in native_country_map.keys():
                b['Native-Country'] = native_country_map[b['Native-Country']]
            else:
                b['Native-Country'] = -1
            b['Makes'] = 1 if b['Makes'] == '<=50K.' else 2


# this method convert again a string into a numeric representation
def convert_value(key, value):
    create_dictionary("workclass", workclass_map)
    create_dictionary("education", education_map)
    create_dictionary("marital-status", marital_status_map)
    create_dictionary("occupation", occupation_map)
    create_dictionary("relationship", relationship_map)
    create_dictionary("race", race_map)
    create_dictionary("native-country", native_country_map)

    if key == 'Sex':
        return 1 if value == 'Male' else 2
    elif key == 'Makes':
        return 1 if value == '<=50K.' else 2
    elif key == 'Workclass':
        return workclass_map[value]
    elif key == 'Education':
        return education_map[value]
    elif key == 'Marital-Status':
        return marital_status_map[value]
    elif key == 'Occupation':
        return occupation_map[value]
    elif key == 'Relationship':
        return relationship_map[value]
    elif key == 'Race':
        return race_map[value]
    elif key == 'Native-Country':
        return native_country_map[value]
    else:
        return int(value)
