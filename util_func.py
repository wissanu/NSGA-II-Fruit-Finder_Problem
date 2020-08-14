
def M_min(chromosome_list, status):
    if status == 'cost':
        best = chromosome_list[0].fitness_cost
        for i in chromosome_list:
            best = best if best < i.fitness_cost else i.fitness_cost
        return best
    if status == 'piece':
        best = chromosome_list[0].fitness_piece
        for i in chromosome_list:
            best = best if best < i.fitness_piece else i.fitness_piece
        return best


def M_max(chromosome_list, status):
    if status == 'cost':
        best = chromosome_list[0].fitness_cost
        for i in chromosome_list:
            best = best if best > i.fitness_cost else i.fitness_cost
        return best
    if status == 'piece':
        best = chromosome_list[0].fitness_piece
        for i in chromosome_list:
            best = best if best > i.fitness_piece else i.fitness_piece
        return best
