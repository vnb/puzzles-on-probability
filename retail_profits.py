"""
Supply - x, Demand - D.
D is a uniform distribution between [80, 140]
Profit = 0.6 * x when x <= D,
       = 0.6 * D -  0.4 * (x - D) when x > D
Calculate the supply to maximize the expected profit
"""

import random
import matplotlib.pyplot as plt
<<<<<<< Updated upstream


class Retailer(object):

    def __init__(self, unit_profit, unit_loss):
        self.unit_profit = unit_profit
        self.unit_loss= unit_loss

    def plot_retail_profits(self, profits):

        x_data = [key for key in profits]
        y_data = [profits[key] for key in profits]

        # begin plotting
        fig = plt.figure(figsize = (10, 10))
        axis = fig.add_subplot(1, 1, 1)
        axis.scatter(x_data, y_data, color = "blue", marker = "o")
        axis.set_title("Retail Profits")
        axis.set_xlabel("Supply")
        axis.set_ylabel("Profit")
        fig.savefig("profits.png")

    def profit_func(self, supply, demand):
        if supply <= demand:
            return self.unit_profit * supply
        else:
            return self.unit_profit * demand - self.unit_loss * (supply - demand)

    def maximize_profit(self, min_demand, max_demand, iterations = 10000):
        profits = {}
        for i in range(min_demand, max_demand+1):
            sum_profit = 0
            for j in range(0, iterations + 1):
                demand = random.randint(min_demand, max_demand+1)
                sum_profit +=  self.profit_func(i, demand)
            profits[i] = (sum_profit*1.0)/iterations

        self.plot_retail_profits(profits)
        return max(profits, key = profits.get)


if __name__ == "__main__":
    r = Retailer(0.6, 0.4)
    print r.maximize_profit(80, 140)


=======
>>>>>>> Stashed changes


class Retailer(object):

    def __init__(self, unit_profit, unit_loss):
        self.unit_profit = unit_profit
        self.unit_loss= unit_loss

    def plot_retail_profits(self, profits):

        x_data = [key for key in profits]
        y_data = [profits[key] for key in profits]

        # begin plotting
        fig = plt.figure(figsize = (10, 10))
        axis = fig.add_subplot(1, 1, 1)
        axis.scatter(x_data, y_data, color = "blue", marker = "o")
        axis.set_title("Retail Profits")
        axis.set_xlabel("Supply")
        axis.set_ylabel("Profit")
        fig.savefig("profits.png")

    def profit_func(self, supply, demand):
        if supply <= demand:
            return self.unit_profit * supply
        else:
            return self.unit_profit * demand - self.unit_loss * (supply - demand)

    def maximize_profit(self, min_demand, max_demand, iterations = 10000):
        profits = {}
        for i in range(min_demand, max_demand+1):
            sum_profit = 0
            for j in range(0, iterations + 1):
                demand = random.randint(min_demand, max_demand+1)
                sum_profit +=  self.profit_func(i, demand)
            profits[i] = (sum_profit*1.0)/iterations

        self.plot_retail_profits(profits)
        return max(profits, key = profits.get)


if __name__ == "__main__":
    r = Retailer(0.6, 0.4)
    print(r.maximize_profit(80, 140))
