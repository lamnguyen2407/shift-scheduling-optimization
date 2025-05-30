import numpy as np
import random
import math

def cost(schedule):
    hard_cost = 0
    soft_cost = 0

    for day in range(28):
        day_shifts = np.sum(schedule[:, day] == 1)
        night_shifts = np.sum(schedule[:, day] == 2)
        if day_shifts != 3:
            hard_cost += abs(day_shifts - 3) * 10
        if night_shifts != 1:
            hard_cost += abs(night_shifts - 1) * 10

    for i in range(8):
        weekly_shifts = [np.sum(schedule[i, j:j+7] > 0) for j in range(0, 28, 7)]
        for shifts in weekly_shifts:
            if (i < 4 and (shifts < 4 or shifts > 5)):
                soft_cost += abs(shifts - 4)
            elif (i >= 4 and (shifts < 2 or shifts > 3)):
                soft_cost += abs(shifts - 2)

        consecutive_days = 0
        max_consecutive_days = 0
        for day in range(28):
            if schedule[i, day] > 0:
                consecutive_days += 1
            else:
                if consecutive_days > max_consecutive_days:
                    max_consecutive_days = consecutive_days
                consecutive_days = 0
        if consecutive_days > max_consecutive_days:
            max_consecutive_days = consecutive_days

        if (i < 4 and (max_consecutive_days < 4 or max_consecutive_days > 6)):
            soft_cost += abs(max_consecutive_days - 4)
        elif (i >= 4 and (max_consecutive_days < 2 or max_consecutive_days > 3)):
            soft_cost += abs(max_consecutive_days - 2)

    return hard_cost + soft_cost

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
