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

    def print(self,items,capacity):
        for i in self.individuals:
            print(i.gene )
            print(fitness(i.gene, items, capacity))


def solve_knap_sack(capacity, items):
    population = Population()
    ps = 100
    population.random_init(ps, items.__len__())
    # p.print(items, capacity)
    # calculate fitness values
    for i in population.individuals:
        i.fitness = fitness(i.gene, items, capacity)

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
    penalty = 0.2
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
