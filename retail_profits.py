	
"""
Supply - x, Demand - D. 
D is a uniform distribution between [80, 140]
Profit = 0.6 * x when x <= D, 
       = 0.6 * D -  0.4 * (x - D) when x > D 
Calcuate the supply to maximize the expected profit
"""

import random
import matplotlib.pyplot as plt
def retail_profit(min_D, max_D, Profit, Loss, iter):
	profit_dict = {}
	for i in range(min_D, max_D+1):
		sum_profit = 0
		count = 0
		for j in range(0,iter+1):
			D = random.randint(min_D, max_D+1)
			f = lambda x, d: 0.6 * x if x<=d else 0.6*d - 0.4*(x-d)
			profit = f(i,D)
			sum_profit = sum_profit+profit
			count = count+1
		profit_dict[i] = sum_profit*1.0/iter
	#plotting
	x_data = []
	y_data = []
	for key in profit_dict:
		x_data.append(key)
		y_data.append(profit_dict[key])
	# Create a Figure object.
	fig = plt.figure(figsize=(10, 10))
	# Create an Axes object.
	ax = fig.add_subplot(1,1,1) # one row, one column, first plot
	# Plot the data.
	ax.scatter(x_data, y_data, color="blue", marker="o")
	# Add a title.
	ax.set_title("Retail Profits")
	# Add some axis labels.
	ax.set_xlabel("Supply")
	ax.set_ylabel("Profit")
	# Produce an image.
	fig.savefig("scatterplot.png")	
	return max(profit_dict, key = profit_dict.get)

print(retail_profit(80, 140, 0.60, 0.40, 10000))	




