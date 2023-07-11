def test(t):
    pc = []

    # Test on field "Capital-Gain"
    if int(t['Capital-Gain']) < 5000:
        pc += [('Capital-Gain', '<', '5000')]
    elif int(t['Capital-Gain']) >= 10000:
        pc += [('Capital-Gain', '>=', '10000')]
    else:
        pc += [('Capital-Gain', '>=', '5000'), ('Capital-Gain', '<', '10000')]

    # Test on field "Capital-Loss"
    if int(t['Capital-Loss']) == 0:
        pc += [('Capital-Loss', '==', '0')]
    elif 0 < int(t['Capital-Loss']) <= 4356:
        pc += [('Capital-Loss', '>', '0'), ('Capital-Loss', '<=', '4356')]
    else:
        pc += [('Capital-Loss', '>', '4356')]

    # Test on field "Native-Country"
    if t['Native-Country'] == 'United-States':
        pc += [('Native-Country', '==', 'United-States')]
    elif t['Native-Country'] == 'India':
        pc += [('Native-Country', '==', 'India')]
    elif t['Native-Country'] == 'China':
        pc += [('Native-Country', '==', 'China')]
    else:
        pc += [('Native-Country', '!=', 'United-States'), ('Native-Country', '!=', 'India'),
               ('Native-Country', '!=', 'China')]

    return pc
