from random import randint


def single_point(a, b, gene_num):
    point = randint(1, gene_num - 1)
    a[point:], b[point:] = b[point:], a[point:]
    return a.copy(), b.copy()


def mutation(chromosome, max_count_item, gene_num):
    position = randint(0, gene_num - 1)
    chromosome[position] = randint(0, max_count_item)
    return chromosome

