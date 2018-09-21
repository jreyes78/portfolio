from itertools import chain, combinations, product
import operator

def f(numbers):
    
    n = len(numbers)
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i))
    term_lists = [[int(numbers[sl]) for sl in map(slice, chain(b, d), chain(d, e))] for d in splits]
    return term_lists

vals = f("323")[1:]
operators = ['+', '*', '-', '/']

def expressions(values):
    # Base case, only one value left
    if len(values) == 1:
        yield values

    # Iterate over the indexes
    for i in range(len(values)):
        # Pop value from given index and store the remaining values
        # to be used with next recursion
        forward = values[:]
        val = forward.pop(i)

        # Yield all value, operator, subexpression combinations
        for op in operators:
            for rest in expressions(forward):
                yield [val, op] + rest
                
def final(vals):
    for expr in expressions(vals):
        expr = ' '.join(str(x) for x in expr)
        final = eval(expr)
        if final == 3:
            print('{} = {}'.format(expr, eval(expr)))

for x in vals:
    print(final(x))
