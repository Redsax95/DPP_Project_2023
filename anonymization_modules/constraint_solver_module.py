from z3 import *


# this method choose the correct operation in order to be added into a solver
def parse_op(dictionary, attribute, operation, value):
    if operation == '==':
        return dictionary[attribute] == value
    elif operation == '!=':
        return dictionary[attribute] != value
    elif operation == '>=':
        return dictionary[attribute] >= value
    elif operation == '<=':
        return dictionary[attribute] <= value
    elif operation == '>':
        return dictionary[attribute] > value
    elif operation == '<':
        return dictionary[attribute] < value
    else:
        print('Operation not allowed')
        exit(1)


# this method set a dictionary associating to each field a same named variable that will be used by the solver
# to find a solution, for each field set also the range constraint based on the content of the initial dataset
def set_dictionary_and_range_constraints(dictionary, solver):
    dictionary['Age'] = Int('Age')
    solver.add(And(dictionary['Age'] >= 17, dictionary['Age'] <= 90))
    dictionary['Workclass'] = Int('Workclass')
    solver.add(And(dictionary['Workclass'] >= 1, dictionary['Workclass'] <= 8))
    dictionary['Fnlwgt'] = Int('Fnlwgt')
    solver.add(And(dictionary['Fnlwgt'] >= 12200, dictionary['Fnlwgt'] <= 1485000))
    dictionary['Education'] = Int('Education')
    solver.add(And(dictionary['Education'] >= 1, dictionary['Education'] <= 16))
    dictionary['Marital-Status'] = Int('Marital-Status')
    solver.add(And(dictionary['Marital-Status'] >= 1, dictionary['Marital-Status'] <= 7))
    dictionary['Occupation'] = Int('Occupation')
    solver.add(And(dictionary['Occupation'] >= 1, dictionary['Occupation'] <= 14))
    dictionary['Relationship'] = Int('Relationship')
    solver.add(And(dictionary['Relationship'] >= 1, dictionary['Relationship'] <= 6))
    dictionary['Race'] = Int('Race')
    solver.add(And(dictionary['Race'] >= 1, dictionary['Race'] <= 5))
    dictionary['Sex'] = Int('Sex')
    solver.add(Or(dictionary['Sex'] == 1, dictionary['Sex'] == 2))
    dictionary['Capital-Gain'] = Int('Capital-Gain')
    solver.add(And(dictionary['Capital-Gain'] >= 0, dictionary['Capital-Gain'] < 100000))
    dictionary['Capital-Loss'] = Int('Capital-Loss')
    solver.add(And(dictionary['Capital-Loss'] >= 0, dictionary['Capital-Loss'] <= 4356))
    dictionary['Hours-per-Week'] = Int('Hours-per-Week')
    solver.add(And(dictionary['Hours-per-Week'] >= 1, dictionary['Hours-per-Week'] <= 99))
    dictionary['Native-Country'] = Int('Native-Country')
    solver.add(And(dictionary['Native-Country'] >= 1, dictionary['Native-Country'] <= 41))
    dictionary['Makes'] = Int('Makes')
    solver.add(Or(dictionary['Makes'] == 1, dictionary['Makes'] == 2))


# this method try to find a solution to all the constraint passed and also to the range constraints created here,
# if a solution is not found return nothing
def constraint_solver(set_of_constraints):
    solver = Solver()

    dictionary = {}

    set_dictionary_and_range_constraints(dictionary, solver)

    for (attribute, operation, value) in set_of_constraints:
        solver.add(parse_op(dictionary, attribute, operation, value))

    if solver.check() == sat:
        model = solver.model()
        released = {}
        for key, value in dictionary.items():
            released[key] = model[value].as_long()
        return released

    return None
