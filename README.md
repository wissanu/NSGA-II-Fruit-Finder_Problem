# NSGA-II_Fruit_Finder

Finding a total pieces of five fruit that won't exceed 1000 baht.
In each of fruit has cost. 

This version is implemented on NSGA-II for solving multi objective and the result shows through graph with difference colors
for easy to interpret the Front-Pareto level and so on.

NoTE: cost and pieces constrant can be raise.

Method included
- Tournament Selection ( the candidate is 20% from total population ) (both)
- mutation swap
- crossove and mutation rate , 70% and 10%


Constrain
- 0 <= x1,x2,x3,x4,x5 <= 15
- Objective function (cost) MAX: (x1 * cost1) + (x2 * cost2) + (x2 * cost3) + (x3 * cost4) + (x4 * cost5) <= 1000
- Objective function (piece) MAX: (x1 + x2 + x3 + x4 + x5) <= 75
- cost1 = 10
- cost2 = 5
- cost3 = 30
- cost4 = 50
- cost5 = 55
