from anonymization_modules.anonymization import convert_value
from anonymization_modules.constraint_solver_module import constraint_solver

excluding_fields = ['Sex', 'Makes', 'Capital-Gain', 'Capital-Loss']


# generate the constraints according to the No Field Repeat algorithm
def no_field_repeat(bucket):
    set_of_constraints = []
    for t in bucket:
        for key, value in t.items():
            if key not in excluding_fields:
                set_of_constraints += [(key, '!=', value)]
    return set_of_constraints


# generate the constraints according to the No Tuple Repeat algorithm, taking first field to do that
def no_tuple_repeat(bucket):
    set_of_constraints = []
    for t in bucket:
        set_of_constraints += [('Age', '!=', t['Age'])]
    return set_of_constraints


# this method select the algorithm to apply on the dataset, generate all the constraints and invoke the solver
# method to obtain the released dataset
def constraint_generation(buckets, type_of_algorithm):
    released_dataset = []

    for pc, B in buckets.items():
        if type_of_algorithm == 'P-F':
            set_of_constraints = no_field_repeat(B)
        else:
            set_of_constraints = no_tuple_repeat(B)

        for s in pc.split('|'):
            result = eval(s)
            temp = convert_value(result[0], result[2])
            set_of_constraints += [(result[0], result[1], temp)]

        result_solution = constraint_solver(set_of_constraints)

        # here check if the solver have produced a solution, if yes can add to the released dataset
        if result_solution:
            released_dataset += [result_solution]

    return released_dataset
