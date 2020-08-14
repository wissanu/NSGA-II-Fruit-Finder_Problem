from Fruit_NSGAII.chromosome import Chromosome


def fast_non_dominate_sorting(chromosome_list):
    # calculate niche count ( non-dominate count )
    for x in chromosome_list:
        x.niche_score = sum([1 if y.fitness_cost > x.fitness_cost and y.fitness_piece > x.fitness_piece else 0 for y in chromosome_list])

    # sorted list by niche count (DESC)
    Chromosome.status = 'niche-sort'
    chromosome_list = sorted(chromosome_list)

    # get dominated list ( non-dominate count )
    # !!! This method need to be sorted first. !!!!
    for x in chromosome_list:
        x.dominated_list = [1 if y.fitness_cost > x.fitness_cost and y.fitness_piece > x.fitness_piece else 0 for y in chromosome_list]

    # assign pareto rank regraded Front pareto ranking.
    for index_x, obj in enumerate(chromosome_list):
        # assign pareto for non-dominated solution
        if obj.niche_score == 0:
            obj.pareto_rank = 1
        else:
            # assign pareto for dominated solution
            nearest_rank = 0
            for index_y, compare_obj in enumerate(chromosome_list[index_x].dominated_list):
                if compare_obj == 1:
                    nearest_rank = chromosome_list[index_y].pareto_rank
            chromosome_list[index_x].pareto_rank = nearest_rank + 1

    # sorted list by pareto rank (ASC)
    Chromosome.status = 'pareto-sort'
    chromosome_list = sorted(chromosome_list)

    return chromosome_list
