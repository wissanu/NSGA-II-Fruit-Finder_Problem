from random import randint


def single_point(a, b, gene_num):
    point = randint(1, gene_num - 1)
    a[point:], b[point:] = b[point:], a[point:]
    return a.copy(), b.copy()


def mutation(chromosome, max_count_item, gene_num):
    position = randint(0, gene_num - 1)
    chromosome[position] = randint(0, max_count_item)
    return chromosome


def order_xover(a, b, start, stop):
    child = [None] * len(a)
    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]
    # Fill using order from second parent:
    b_ind = stop
    c_ind = stop
    l = len(a)
    while None in child:
        if b[b_ind % l] not in child:
            child[c_ind % l] = b[b_ind % l]
            c_ind += 1
        b_ind += 1
    return child


def order_xover_pair(a, b):
    half = len(a) // 2
    start = randint(0, len(a) - half)
    stop = start + half
    return order_xover(a, b, start, stop)
