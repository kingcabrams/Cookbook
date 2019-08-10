# TODO: Deepen understanding of lambda expressions


def make_incrementor(n):
    return lambda path: path + n


f = make_incrementor(42)
print(f(0))
print(f(1))
