from Fruit_NSGAII.chromosome import Chromosome


def fast_non_dominate_sorting(chromosome_list):
    # calculate niche count ( non-dominate count )
    for x in chromosome_list:
        x.niche_score = sum([1 if y.fitness_cost > x.fitness_cost and y.fitness_piece > x.fitness_piece else 0 for y in chromosome_list])

    # sorted list by niche count (DESC)
    Chromosome.status = 'niche-sort'
    chromosome_list = sorted(chromosome_list)

    # assign pareto rank regraded Front pareto ranking.
    for x in chromosome_list:
        if x.niche_score == 0:
            x.pareto_rank = 1
        else:
            for y in chromosome_list:
                if y.fitness_cost > x.fitness_cost and y.fitness_piece > x.fitness_piece:
                    x.pareto_rank = y.pareto_rank + 1

    # sorted list by pareto rank (ASC)
    Chromosome.status = 'pareto-sort'
    chromosome_list = sorted(chromosome_list)

    return chromosome_list
