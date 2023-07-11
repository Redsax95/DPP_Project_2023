import argparse
import json
import time
import convert_dataset as cd
# import privacy_utility_analysis as pu
from anonymization_modules import program_execution_module as pe
from anonymization_modules import anonymization as an
from anonymization_modules import constraint_generation_module as cg

DATA_KEY = 'USCensusOfAdults'


def load_data(dataset):
    r = []
    for t in dataset[DATA_KEY]:
        r += [t]
    return r


def write_data(output_dataset, released_dataset):
    json_dict = {DATA_KEY: released_dataset}
    with open(output_dataset, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_dict, indent=4)
        json_file.write(json_string)


def input_params():
    parser: argparse.ArgumentParser = argparse.ArgumentParser()

    parser.add_argument('-i', type=str, help="input dataset file path", default='datasets/adult.test.csv')
    parser.add_argument('-o', type=str, help="output dataset file path", default='datasets/anonymized.adult.test.json')
    parser.add_argument('-k', type=int, help="anonymity degree for the dataset", default=4)
    parser.add_argument('-f', type=str, help="type of anonymization: P-T or P-F", default='P-T')

    args = parser.parse_args()

    return args.i, args.o, args.k, args.f


def main():
    input_dataset, output_dataset, k, option = input_params()

    print("Execute the program on ", input_dataset, " applying the ", option, " algorithm with k = ", k)

    start_time = time.time()

    converted_dataset = input_dataset.replace('csv', 'json')

    # conversion of the initial csv dataset into a json one
    raw_data = cd.csv_to_json(input_dataset, converted_dataset, DATA_KEY)
    raw_dataset = load_data(raw_data)

    print("Number of initial tuples: ", len(raw_dataset))

    # obtain path conditions for every raw tuples, group them into buckets based on same path conditions
    # and remove buckets with sizes less than k
    pc_buckets = pe.program_execution(raw_dataset, k)

    # anonymize all buckets converting the data into integers values
    an.anonymize(pc_buckets)

    # based on the type of algorithm want to apply, a different constraint generator is called.
    # the function return a new dataset that satisfy the constraint we had generated
    if option == 'P-T':
        released_dataset = cg.constraint_generation(pc_buckets, 'P-T')
    elif option == 'P-F':
        released_dataset = cg.constraint_generation(pc_buckets, 'P-F')
    else:
        print("Not valid option chosen")
        exit(1)

    print("Number of released tuples: ", len(released_dataset))

    write_data(output_dataset, released_dataset)

    end_time = time.time()

    print("Total execution time: ", end_time - start_time)

    # pu.analyze_dataset(released_dataset)


if __name__ == '__main__':
    main()
