
"""
Supply - x, Demand - D. 
D is a uniform distribution between [80, 140]
Profit = 0.6 * x when x <= D, 
       = 0.6 * x -  0.4 * (x - D) when x > D 
Calcuate the supply to maximize the expected profit
"""

import random

def retail_profit(min_D, max_D, Profit, Loss, iter):
	profit_dict = {}
	for i in range(min_D, max_D):
		sum_profit = 0
		count = 0
		while count<=iter:
			D = random.randint(min_D, max_D)
			if D>=i:
				profit = Profit*i
			else:
				profit = Profit*D-Loss*(i-D)
			sum_profit = sum_profit+profit
			count = count+1
		profit_dict[i] = round(sum_profit/count, 3)
	avg_prof = []
	for key in profit_dict:
		avg_prof.append(profit_dict[key])
	return max(profit_dict, key = profit_dict.get)

print(retail_profit(80, 140, 0.60, 0.40, 1000))	




