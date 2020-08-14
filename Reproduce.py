from random import randint


def single_point(a, b, gene_num):
    point1 = randint(1, gene_num - 1)
    point2 = randint(1, gene_num - 1)

    a[point1], b[point2] = b[point2], a[point1]
    return a.copy(), b.copy()


def mutation(chromosome, max_count_item, gene_num):
    position = randint(0, gene_num - 1)
    chromosome[position] = randint(0, max_count_item)
    return chromosome.copy()


