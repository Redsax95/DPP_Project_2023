Here have the main core of the project with 4 modules used to apply the kb-anonymity:

The "program_execution_module" uses all the raw tuples of the initial dataset to collect their path condition and divide all tuples into the same execution paths.

The "anonymization" module takes a raw dataset and anonymizes it into numerical values.

The "constraint_generation_module" create for all tuples collected in "program_execution_module" some constraints according to the algorithm chosen:
"NoTupleRepeat" or "NoFieldRepeat". After generating the constraints for all tuples of one path, generate the constraints for the path itself and invoke
the solver module to obtain a result. If a result is obtained can be added to the released dataset. This process is done for all the paths that we have 
generated before.

The "constraint_solver_module" generate the range constraint for the dataset, add them and the passed constraint that we have generated before into
a solver and tries to find one or more solutions that respect all the constraints. If find something return it else return nothing.
