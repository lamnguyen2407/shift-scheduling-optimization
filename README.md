# shift-scheduling-optimization
A project from Math Modeling Competition 2024

This repository contains our project for the 2024 Mathematical Modeling Contest, developed by team **DK Algebros**. The project addresses the employee shift scheduling problem using the **Simulated Annealing** algorithm to find an optimized work schedule under multiple real-world constraints.

---

## 📌 Problem Statement

We are tasked with creating a 28-day schedule (from August 5 to September 1, 2024) for **8 employees** (4 full-time and 4 part-time), assigning them to either **morning** or **evening** shifts each day. The schedule must:
- Satisfy specific working hour quotas per employee.
- Ensure enough staffing per shift.
- Respect both hard and soft constraints related to fairness and workload balance.

---

## 🧠 Our Approach

We use the **Simulated Annealing (SA)** metaheuristic algorithm to search for optimal or near-optimal schedules. The SA process includes:
- Random schedule initialization.
- Cost function design (penalizing hard and soft constraint violations).
- Temperature-based acceptance of new solutions (including worse ones to avoid local minima).
- Repeated iterations with a cooling schedule until a stable solution is reached.

The cost function combines both **hard constraints** (e.g., required number of shifts) and **soft constraints** (e.g., preferred consecutive working days).

---

## 🔍 Results

We ran the simulation multiple times to find the best possible shift schedule. Among the best results:
- Hard constraint cost: **18**
- Extended solution with soft constraints: **29**

We also considered fairness and practicality in the final evaluation.

---

## 👤 My Contribution

As part of the team, I contributed to:
- Designing and implementing the Simulated Annealing algorithm in Python.
- Developing the cost evaluation function and neighborhood generation logic.
- Testing and analyzing results across multiple runs.
- Writing the final report in Vietnamese and this English summary.

## ⚙️ Technologies Used
Python 3.13
Libraries: numpy, pandas, matplotlib, random

## 📚 References
De Bruecker et al., Workforce planning incorporating skills, European Journal of Operational Research, 2015.

Soto et al., Nurse and paramedic rostering with constraint programming, Romanian Journal of Information Science and Technology, 2013.
