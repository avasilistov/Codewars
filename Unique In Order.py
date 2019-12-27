from itertools import groupby


def unique_in_order(iterable):
    return [k for k, g in groupby(iterable)]

# test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
