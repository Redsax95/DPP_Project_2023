from tests import test1 as a
from tests import test2 as b
from tests import test3 as c
from tests import test4 as d


def program_execution(raw_dataset, k):
    pc_buckets = {}
    delete_buckets = []

    for t in raw_dataset:
        # execute the tests with t and collect groups of tuples based on path conditions
        pc = a.test(t)
        pc += b.test(t)
        pc += c.test(t)
        pc += d.test(t)

        try:
            pc_buckets['|'.join(str(i) for i in pc)] += [t]
        except KeyError:
            pc_buckets['|'.join(str(i) for i in pc)] = [t]

    print("Number of path created: ", len(pc_buckets))

    # if some buckets contain less than k elements are discarded
    for pc, B in pc_buckets.items():
        if len(B) < k:
            delete_buckets += [pc]

    for e in delete_buckets:
        del pc_buckets[e]

    print("Number of remaining paths: ", len(pc_buckets))

    return pc_buckets
