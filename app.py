from Fruit_NSGAII.chromosome import Chromosome
from Fruit_NSGAII import Reproduce as ga
from Fruit_NSGAII import plot_graph as pg
from Fruit_NSGAII import FastDominatedSort as metd
from Fruit_NSGAII import CrowdingDistance as cd
from random import random

# -------- Setting parameter --------
gene_num = 5
pop_num = 50
versus = 0.2
max_count_item = 15
number_generation = 100
crossover_rate = 0.7
mutation_rate = 0.1
equation_input = [10, 5, 30, 50, 55]
# ------------ Don't change ---------------
current_list = []
best_chromosome = []
best_fitness_cost = -1
best_fitness_piece = -1

if __name__ == '__main__':

    # create initial pop
    for _ in range(pop_num):
        g = Chromosome(gene_num, pop_num, max_count_item)
        g.initial_pop()
        current_list.append(g)

    # calculate niche score & pareto rank || calculate crowding distance
    current_list = metd.fast_non_dominate_sorting(current_list)
    current_list = cd.crowding_score(current_list)

    # generation loop start
    for gen in range(1, number_generation + 1):
        print('generation', gen)

        next_list = []

        # create next generation
        while len(next_list) < pop_num:

            # select parents
            parent1 = Chromosome.tournament_selection(versus, current_list, pop_num)
            parent2 = Chromosome.tournament_selection(versus, current_list, pop_num)

            # create object child1 and child2
            child1 = Chromosome(gene_num, pop_num, max_count_item)
            child2 = Chromosome(gene_num, pop_num, max_count_item)

            # Crossover process
            if random() < crossover_rate:
                # Do crossover
                child1.chromosome, child2.chromosome = ga.single_point(parent1.chromosome, parent2.chromosome, gene_num)
            else:
                # Use parent as child instead
                child1.chromosome = parent1.chromosome.copy()
                child2.chromosome = parent2.chromosome.copy()

            # Mutation process
            if random() < mutation_rate:
                child1.chromosome = ga.mutation(child1.chromosome, max_count_item, gene_num)
                child2.chromosome = ga.mutation(child2.chromosome, max_count_item, gene_num)

            # calculate fitness
            child1.fitness_finder()
            child2.fitness_finder()

            # check duplicate and constraint
            if child1.fitness_cost <= 1000 and len(next_list) < pop_num:
                check_dup_P = [1 for _ in current_list if child1.chromosome != _.chromosome]
                check_dup_Q = [1 for _ in next_list if child1.chromosome != _.chromosome]
                if (sum(check_dup_P)+sum(check_dup_Q)) == (len(next_list)+len(current_list)):
                    next_list.append(child1)

            if child2.fitness_cost <= 1000 and len(next_list) < pop_num:
                check_dup_P = [1 for _ in current_list if child2.chromosome != _.chromosome]
                check_dup_Q = [1 for _ in next_list if child2.chromosome != _.chromosome]
                if (sum(check_dup_P)+sum(check_dup_Q)) == (len(next_list)+len(current_list)):
                    next_list.append(child2)

        # combine parent and child population into one.
        totalChunk = []
        for _ in current_list:
            totalChunk.append(_)
        for _ in next_list:
            totalChunk.append(_)

        # calculate niche score & pareto rank || calculate crowding distance
        totalChunk = metd.fast_non_dominate_sorting(totalChunk)
        totalChunk = cd.crowding_score(totalChunk)

        # clear memory and reuse current_list
        current_list.clear()
        del next_list

        # divide half top into new parent population
        for _ in range(len(totalChunk)//2):
            current_list.append(totalChunk[_])

        # clear memory
        del totalChunk

        # get best chromosome and fitness
        best_chromosome = current_list[0].chromosome.copy()
        best_fitness_cost = current_list[0].fitness_cost
        best_fitness_piece = current_list[0].fitness_piece

        print(*current_list)

    # ==== Result ====
    print("================")
    print('best chromosome : {!r}'.format(best_chromosome) + '\nbest cost : {}'.format(best_fitness_cost) + '\nbest piece : {}'.format(best_fitness_piece))
    print('Banana : {} pieces'.format(best_chromosome[0]) + ' per 10 baht')
    print('Orange : {} pieces'.format(best_chromosome[1]) + ' per 5 baht')
    print('Apple : {} pieces'.format(best_chromosome[2]) + ' per 30 baht')
    print('Melon : {} pieces'.format(best_chromosome[3]) + ' per 50 baht')
    print('Berry : {} pieces'.format(best_chromosome[4]) + ' per 55 baht')

    # plot graph
    pg.plot_graph(current_list, 5)
