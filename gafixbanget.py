import math
import random

xLimit = [-1, 2]
yLimit = [-1, 1]
totalGen = 6
totalChromosome = 6
totalPopulation = 100
probability = 0.65
mutationProbability = 0.08

def initiate_chromosome(totalGen):           # fungsi untuk mengenerate chromosome
  chromosome = []                            # inisialisai array untuk chromosome
  for _ in range(totalGen):                  # perulangan untuk generate angka random pada tiap iterasinya
    chromosome.append(random.randint(0,9))
  return chromosome

def initiate_population(totalChromosome, totalGen):  # fungsi untuk mengenerate populasi
  population = []                                   # inisialisasi array untuk populasi
  for _ in range (totalChromosome):                  # perulangan untuk generate random populasi 
    chromosome = initiate_chromosome(totalGen)
    population.append(chromosome)
  return population

def decodeChromosome(chromosome, xLimit, yLimit):
    divider = 9 * (10**-1 + 10**-2 + 10**-3)
    multiplierX = (chromosome[0] * (10**-1) + chromosome[1] * (10**-2) + chromosome[2] * (10**-3))
    multiplierY = (chromosome[3] * (10**-1) + chromosome[4] * (10**-2) + chromosome[5] * (10**-3))
    decodeX = xLimit[0] + (((xLimit[1] - xLimit[0]) / divider) * multiplierX)
    decodeY = yLimit[0] + (((yLimit[1] - yLimit[0]) / divider) * multiplierY)
    return [decodeX, decodeY]
  
def fitnessChromosome(chromosome, xLimit, yLimit):
    decode = decodeChromosome(chromosome, xLimit, yLimit)
    fitness = (math.cos(decode[0]**2) * math.sin(decode[1]**2)) + (decode[0] + decode[1])  
    return fitness

def fitnessPopulation(population, xLimit, yLimit, totalChromosome):
    fitnessPop = []
    for i in range(totalChromosome):
        chrom = fitnessChromosome(population[i], xLimit, yLimit)
        fitnessPop.append(chrom)
    return fitnessPop

def parentSelection(population, xLimit, yLimit, totalChromosome):
    bestChromosome = []
    for i in range(totalChromosome-1):
      chromosome = population[random.randint(0, totalChromosome-1)]
      if (bestChromosome == [] or fitnessChromosome(chromosome, xLimit, yLimit) > fitnessChromosome(bestChromosome, xLimit, yLimit)):
        bestChromosome = chromosome
    return bestChromosome

def crossover(parent1, parent2, probability):
    randomPC = random.random()    # untuk mencari nilai probabilitas crossover yang random
    if (randomPC < probability):    
        randomPoint = random.randint(1, 5)  # untuk mencari nilai probabilitas point yang random
        for i in range (randomPoint):
            temp = parent1[i]
            parent1[i] = parent2[i]
            parent2[i] = temp
    return [parent1, parent2]

def mutation(chromosome1, chromosome2, mutationProbability):
  probRandom = random.random()
  print (probRandom)
  if probRandom < mutationProbability:
      gen1, gen2 = random.randint(0,5), random.randint(0,5)
      genValue1, genValue2 = random.randint(0,9), random.randint(0,9)
      while chromosome1[gen1] == genValue1:
        genValue1 = random.randint(0,9)
      while chromosome2[gen2] == genValue2:
        genValue2 = random.randint(0,9)
      chromosome1[gen1] = genValue1
      chromosome2[gen2] = genValue2
  return chromosome1, chromosome2

def elitism(fitnessPopulation):
  index = fitnessPopulation.index(max(fitnessPopulation))
  return index

population = initiate_population(totalChromosome, totalGen)
chromosome =  initiate_chromosome(totalGen)
decode = decodeChromosome(chromosome, xLimit, yLimit)


print ("population    : ", population)
print("Chromosome     : ", chromosome)
print("Parents        : ", parentSelection(population, xLimit, yLimit, totalChromosome))
print("Decode         : ", decode)
print("Fitness Value  : ", fitnessChromosome(chromosome, xLimit, yLimit))
