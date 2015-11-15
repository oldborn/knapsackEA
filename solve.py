import random


class Individual:
    fitness = None
    gene = []


class Population:
    individuals = []

    @staticmethod
    def create_random_gene(length):
        gene = []
        while not len(gene) == length:
            gene.append(random.randint(0, 1))
        return gene

    def random_init(self, populationSize, length):
        while not self.individuals.__len__() == populationSize:
            indiv = Individual()
            indiv.gene = self.create_random_gene(length)
            self.individuals.append(indiv)

    def print(self, items, capacity):
        for i in self.individuals:
            print(i.gene)
            print(fitness(i.gene, items, capacity))


def solve_knap_sack(capacity, items):
    population = Population()
    ps = 100
    population.random_init(ps, items.__len__())
    # p.print(items, capacity)
    # calculate fitness values
    for i in population.individuals:
        i.fitness = fitness(i.gene, items, capacity)
    counter = 0
    maxiteration = 1
    while counter != maxiteration:
        counter += 1
        tournament_selection(population, 10, 1, 1)
        # while !terminate
        # selection
        # recombination
        # mutation
        # evaluation

    return 0


def get_random_gene(length):
    gene = []
    while not len(gene) == length:
        gene.append(random.randint(0, 1))
    return gene


def fitness(gene, items, capacity):
    totvalue = 0
    totweight = 0
    penalty = 0
    i = 0
    for g in gene:
        if g == 1:
            totvalue += items[i][0]
            totweight += items[i][1]
        i += 1

    if totweight > capacity:  # not-feasible
        f = totvalue * ((totweight - capacity) / capacity)  # actual value of solution
        f *= penalty
    else:  # feasible
        f = totvalue
    return f


def tournament_selection(evaluatedpopulation, tournamentsize, elitesize, winnersize):
    selection = []
    while selection.__len__() != evaluatedpopulation.individuals.__len__():
        tournamenters = select_n_random_from_list(evaluatedpopulation.individuals, tournamentsize)
        winners = get_n_winners_of_tournament(tournamenters, winnersize)
        selection.append(winners)

    # add elite
    return


def select_n_random_from_list(individuals, n):
    i = 0;
    selection = []
    while i != n:
        i += 1
        selection.append(random.choice(individuals))
    return selection

def get_n_winners_of_tournament(tournamenters, n):
    tournamenters = sorted(tournamenters, key=lambda individual: individual.fitness, reverse=True)
    winners = []
    i = 0
    while winners.__len__() != n:
        winners.append(tournamenters[i])
        i += 1
    return winners