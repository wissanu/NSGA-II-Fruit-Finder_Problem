from Fruit_NSGAII import util_func as uf


def crowding_score(chromosome_list):

    min_cost = uf.M_min(chromosome_list, 'cost')
    max_cost = uf.M_max(chromosome_list, 'cost')
    min_piece = uf.M_min(chromosome_list, 'piece')
    max_piece = uf.M_max(chromosome_list, 'piece')
    last_p_rank = chromosome_list[len(chromosome_list) - 1].pareto_rank
    front_set_index = []

    # create range of index in each pareto front.
    # ( For simplify an implementation of calculated crowding distance )
    # rank started at 1 to N, for N = last pareto rank of individual in each generation.
    for p_rank in range(1, last_p_rank + 1):
        sum_of_pareto_front = sum([1 for obj in chromosome_list if p_rank == obj.pareto_rank])

        if p_rank == 1:
            front_set_index.append((0, sum_of_pareto_front - 1))
            last_index = sum_of_pareto_front
        else:
            front_set_index.append((last_index, (last_index + sum_of_pareto_front) - 1))
            last_index = last_index + sum_of_pareto_front

    # calculate crowding distance
    for start, end in front_set_index:
        for index in range(start, end + 1):
            if index == start:
                chromosome_list[index].crowding_score = 0
            elif index == end:
                chromosome_list[index].crowding_score = 1
            else:
                chromosome_list[index].crowding_score = abs((chromosome_list[index - 1].fitness_cost - chromosome_list[index + 1].fitness_cost) / (max_cost - min_cost)) + abs((chromosome_list[index - 1].fitness_piece - chromosome_list[index + 1].fitness_piece) / (max_piece - min_piece))

    return chromosome_list
