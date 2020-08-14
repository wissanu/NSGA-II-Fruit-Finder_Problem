from random import sample, randint


class Chromosome:
    status = ''

    def __init__(self, x_gene, x_pop, max_count_item):
        self.chromosome = []
        self.gene_num = x_gene
        self.pop_num = x_pop
        self.fitness_cost = 0
        self.fitness_piece = 0
        self.niche_score = 0
        self.pareto_rank = 0
        self.crowding_score = 0
        self.equation_input = [10, 5, 30, 50, 55]
        self.max_count_item = max_count_item

    def __repr__(self):
        return '\nChromosome : {!r}'.format(self.chromosome) \
               + '\ncost : {} '.format(self.fitness_cost) \
               + 'pieces : {}'.format(self.fitness_piece) \
               + '\ndominated : {!r}'.format(self.dominated_list) \
               + '\nP-rank : {}'.format(self.pareto_rank) \
               + ' CD : {}'.format(self.crowding_score)

    def __lt__(self, other):
        if Chromosome.status == 'niche-sort':
            if self.niche_score != other.niche_score:
                return self.niche_score < other.niche_score
            else:
                if self.fitness_cost != other.fitness_cost:
                    return self.fitness_cost > other.fitness_cost
                elif self.fitness_cost == other.fitness_cost:
                    return self.fitness_piece > other.fitness_piece
        if Chromosome.status == 'pareto-sort':
            return self.pareto_rank < other.pareto_rank

    def initial_pop(self):
        while True:
            self.chromosome = sample(range(0, self.max_count_item), self.gene_num)
            self.fitness_finder()
            if self.fitness_cost <= 1000:
                break

    def fitness_finder(self):
        self.fitness_cost = sum([x * y for x, y in zip(self.chromosome, self.equation_input)])
        self.fitness_piece = sum([x for x in self.chromosome])

    @staticmethod
    def tournament_selection(versus, chromosome_list, pop_num):
        k = [randint(0, pop_num - 1) for _ in range(int(versus * pop_num))]
        best = []
        for _ in k:
            if not best or best.pareto_rank < chromosome_list[_].pareto_rank:
                best = chromosome_list[_].chromosome.copy()
            elif best.pareto_rank == chromosome_list[_].pareto_rank:
                if best.crowding_score > chromosome_list[_].crowding_score:
                    best = chromosome_list[_].chromosome.copy()
            return best
