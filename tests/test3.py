def test(t):
    pc = []

    # Test on field "Education"
    if t['Education'] in ['Bachelors', 'Masters', 'Doctorate']:
        pc += [('Education', '==', t['Education'])]
    else:
        pc += [('Education', '!=', 'Bachelors'), ('Education', '!=', 'Masters'), ('Education', '!=', 'Doctorate')]

    # Test on field "Marital-Status"
    if t['Marital-Status'] == 'Married-civ-spouse':
        pc += [('Marital-Status', '==', 'Married-civ-spouse')]
    elif t['Marital-Status'] == 'Divorced':
        pc += [('Marital-Status', '==', 'Divorced')]
    else:
        pc += [('Marital-Status', '!=', 'Married-civ-spouse'), ('Marital-Status', '!=', 'Divorced')]

    # Test on field "Sex"
    if t['Sex'] == 'Male':
        pc += [('Sex', '==', 'Male')]
    else:
        pc += [('Sex', '==', 'Female')]

    return pc
