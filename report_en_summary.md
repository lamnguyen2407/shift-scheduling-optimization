# Project Summary – Workforce Scheduling Optimization Using Simulated Annealing

## 📌 Problem Overview

This project was developed for the 2024 Mathematical Modeling Contest by team DK Algebros. The main challenge was to generate an optimal 28-day work schedule for a team of 8 employees—4 full-time and 4 part-time—while satisfying a series of hard and soft constraints related to shift allocation.

The work shifts are divided into morning and evening sessions across a 4-week period (August 5–September 1, 2024), totaling 56 time slots. The task was to assign shifts to employees in a way that meets the operational requirements and fairness principles.

## 🧩 Constraints

### Hard Constraints:
1. **Number of Shifts per Employee**:
   - Full-time employees (An, Bình, Châu, Dương) must work exactly 18 shifts.
   - Part-time employees (Linh, Kiệt, Giang, Hiếu) must work exactly 10 shifts.

2. **Shift Staffing Requirements**:
   - Morning shifts must have 10 employees in total over 28 days.
   - Evening shifts must have 3 employees per shift.

### Soft Constraints:
1. **Weekly Shift Range**:
   - Full-time: 4–5 shifts/week.
   - Part-time: 2–3 shifts/week.

2. **Consecutive Working Days**:
   - Full-time: 4–6 consecutive working days.
   - Part-time: 2–3 consecutive working days.

Violations of these constraints incur a cost penalty, weighted differently for hard and soft constraints.

## 💡 Methodology

To solve this problem, we implemented the **Simulated Annealing (SA)** algorithm. Inspired by metallurgical annealing, SA is a probabilistic technique used to approximate the global optimum by allowing occasional acceptance of worse solutions to escape local minima.

### Algorithm Steps:
1. Generate a **random initial schedule**.
2. Define a **cost function** penalizing constraint violations.
3. Iteratively generate **neighbor solutions** by swapping shifts between employees.
4. Accept better solutions or probabilistically accept worse ones based on the **cooling schedule** (starting temperature = 5000, cooling rate = 0.97).
5. Repeat until temperature reaches the **stopping threshold** (0.1).

We also extended the cost function to incorporate soft constraints in later phases.

## 🔍 Results

After running the algorithm over 150 iterations with varying initial seeds, we obtained multiple optimized schedules. The best solution had:
- A hard constraint cost of **18**
- An extended solution with soft constraints included and a best cost of **29**

The scheduling outputs were evaluated based on:
- Lowest total cost
- Fairness in employee shift distribution
- Practical considerations like employee capacity and workload balance

