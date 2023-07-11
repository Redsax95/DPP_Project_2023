def test(t):
    pc = []

    # Test on field "Age"
    if int(t['Age']) < 30:
        pc += [('Age', '<', '30')]
    elif int(t['Age']) >= 50:
        pc += [('Age', '>=', '50')]
    else:
        pc += [('Age', '>=', '30'), ('Age', '<', '50')]

    # Test on field "Workclass"
    if t['Workclass'] == 'Private':
        pc += [('Workclass', '==', 'Private')]
    elif t['Workclass'] == 'Self-emp-inc':
        pc += [('Workclass', '==', 'Self-emp-inc')]
    elif t['Workclass'] == 'State-gov':
        pc += [('Workclass', '==', 'State-gov')]
    else:
        pc += [('Workclass', '!=', 'Private'), ('Workclass', '!=', 'Self-emp-inc'), ('Workclass', '!=', 'State-gov')]

    # Test on field "Relationship"
    if t['Relationship'] == 'Husband':
        pc += [('Relationship', '==', 'Husband')]
    elif t['Relationship'] == 'Wife':
        pc += [('Relationship', '==', 'Wife')]
    else:
        pc += [('Relationship', '!=', 'Husband'), ('Relationship', '!=', 'Wife')]

    return pc
