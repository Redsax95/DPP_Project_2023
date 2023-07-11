def test(t):
    pc = []

    # Test on field "Fnlwgt"
    if int(t['Fnlwgt']) < 500000:
        pc += [('Fnlwgt', '<', '500000')]
    elif int(t['Fnlwgt']) >= 1000000:
        pc += [('Fnlwgt', '>=', '1000000')]
    else:
        pc += [('Fnlwgt', '>=', '500000'), ('Fnlwgt', '<', '1000000')]

    # Test on field "Occupation"
    if t['Occupation'] == 'Tech-support':
        pc += [('Occupation', '==', 'Tech-support')]
    elif t['Occupation'] == 'Craft-repair':
        pc += [('Occupation', '==', 'Craft-repair')]
    elif t['Occupation'] == 'Sales':
        pc += [('Occupation', '==', 'Sales')]
    else:
        pc += [('Occupation', '!=', 'Tech-support'), ('Occupation', '!=', 'Craft-repair'),
               ('Occupation', '!=', 'Sales')]

    # Test on field "Hours-per-Week"
    if int(t['Hours-per-Week']) < 30:
        pc += [('Hours-per-Week', '<', '30')]
    elif int(t['Hours-per-Week']) >= 40:
        pc += [('Hours-per-Week', '>=', '40')]
    else:
        pc += [('Hours-per-Week', '>=', '30'), ('Hours-per-Week', '<', '40')]

    return pc
