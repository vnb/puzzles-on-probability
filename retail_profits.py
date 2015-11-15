"""
Supply - x, Demand - D.
D is a uniform distribution between [80, 140]
Profit = 0.6 * x when x <= D,
       = 0.6 * D -  0.4 * (x - D) when x > D
Calcuate the supply to maximize the expected profit
"""
import random
import matplotlib.pyplot as plt
sales = lambda x, d: 0.6 * x if x <= d else 0.6 * d - 0.4 * (x-d)


def retail_profit(minimum_demand, maximum_demand, profit, loss, iter):
        profit_dict = {}
        for i in range(minimum_demand, maximum_demand+1):
                sum_profit = 0
                for j in range(0, iter+1):
                        demand = random.randint(minimum_demand, maximum_demand+1)
                        sum_profit += sales(i, demand)
                profit_dict[i] = sum_profit*1.0/iter

        x_data = []
        y_data = []
        for key in profit_dict:
                x_data.append(key)
                y_data.append(profit_dict[key])
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(x_data, y_data, color="blue", marker="o")
        ax.set_title("Retail Profits")
        ax.set_xlabel("Supply")
        ax.set_ylabel("Profit")
        fig.savefig("scatterplot.png")
        return max(profit_dict, key=profit_dict.get)
        return max(profit_dict, key=profit_dict.get)
print(retail_profit(80, 140, 0.60, 0.40, 10000))

