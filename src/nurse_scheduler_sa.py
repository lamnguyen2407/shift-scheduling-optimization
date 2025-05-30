import numpy as np
import random
import math

def cost(schedule):
    cost = 0
    for day in range(28):
        num_s = np.sum(schedule[:, day] == 1)
        num_t = np.sum(schedule[:, day] == 2)
        cost += abs(num_s - 3)
        cost += abs(num_t - 1)

    for i in range(8):
        num_s = np.sum(schedule[i, :] == 1)
        num_t = np.sum(schedule[i, :] == 2)
        if i < 4:
            cost += abs(num_s + num_t - 18)
        else:
            cost += abs(num_s + num_t - 10)

    return cost

def generate_neighbor(schedule):
    new_schedule = np.copy(schedule)
    i1, j1 = random.randint(0, 7), random.randint(0, 27)
    i2, j2 = random.randint(0, 7), random.randint(0, 27)
    new_schedule[i1, j1], new_schedule[i2, j2] = new_schedule[i2, j2], new_schedule[i1, j1]
    return new_schedule

def simulated_annealing(initial_schedule, initial_temp, alpha, stopping_temp):
    current_schedule = initial_schedule
    current_cost = cost(current_schedule)
    best_schedule = np.copy(current_schedule)
    best_cost = current_cost
    temperature = initial_temp

    while temperature > stopping_temp:
        neighbor = generate_neighbor(current_schedule)
        neighbor_cost = cost(neighbor)
        delta_cost = neighbor_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
            current_schedule = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best_schedule = np.copy(current_schedule)
                best_cost = current_cost

        temperature *= alpha

    return best_schedule, best_cost

def initialize_schedule():
    schedule = np.zeros((8, 28), dtype=int)
    for day in range(28):
        for _ in range(3):
            i = random.randint(0, 7)
            while schedule[i, day] != 0:
                i = random.randint(0, 7)
            schedule[i, day] = 1
        i = random.randint(0, 7)
        while schedule[i, day] != 0:
            i = random.randint(0, 7)
        schedule[i, day] = 2
    return schedule

initial_schedule = initialize_schedule()
initial_temp = 5000
alpha = 0.97
stopping_temp = 0.1

best_schedule, best_cost = simulated_annealing(initial_schedule, initial_temp, alpha, stopping_temp)

print("Best schedule:")
print(best_schedule)
print("Best cost:", best_cost)
