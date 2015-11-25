""" HealthCeuticals sells an antibioics which has no seasonality in demand.Avg demand is 5,000 units. 
Expiration cost - $50/unit, Air Frieght(in case of extra supply) - 150$. 
When Demand = Stocked, operating cost is 0. 
"""

import random
import csv
import matplotlib.pyplot as plt

file_name = 'HealthCeuticals.csv'
file_select = open(file_name)
data = csv.reader(file_select)
indicator = "black"
Historical_Data = []

for row in data:
	if row[0] == "Month":
		indicator = "yellow"
	if indicator == "yellow" and row[0] != "Month" and row[0] != "":
		Historical_Data.append(int(row[1]))


file_select = open(file_name)
data = csv.reader(file_select)


for row in data:
	if row[0] == "Expiration Cost":
		expiration_cost = row[1]
	if row[0] == "Air Freight":
		air_freight = row[1]	


class supply_stock(object):
	""" Find optimal supply/stocks quantity in to keep cost low.
	Monte Carlo method is used to generate random demand from historical data.   """
	def __init__(self, unit_expiration_cost, unit_air_freight_cost, historical_data):
		self.unit_expiration_cost = unit_expiration_cost
		self.unit_air_freight_cost = unit_air_freight_cost
		self.historical_data = historical_data

	def hist_demand(self):
		""" This function generates random demand values from historical Historical_Data """
		max_value = len(historical_data)
		x = random.randint(0,max_value-1)
		return historical_data[x]

	def calc_cost(self, supply, demand, unit_cost_expiration, unit_cost_restock):
		if supply == demand:
			return 0
		elif supply >  demand:
			return self.unit_expiration_cost*(supply-demand)
		else:
			return self.unit_air_freight_cost*(demand-supply)

	def find_percentile(self, list_cost, percentile): 
		r = percentile*0.01*(len(list_cost)+1)
		list_cost.sort()
		if r>int(r):
			return (r-int(r))*(list_cost[int(r)]-list_cost[int(r)-1])+list_cost[int(r)-1]
		else:
			list_cost[int(r)-1]

	def hist_demand(self, historical_data):
		""" This function generates random demand values from historical Historical_Data """
		max_value = len(historical_data)
		x = random.randint(0,max_value-1)
		return historical_data[x] 

	def plot_optimal_supply(self, average_cost, percentile_95, percentile_5, supply):
		fig = plt.figure(figsize = (10, 10))
		axis = fig.add_subplot(1, 1, 1)
		line1 = axis.scatter(supply, average_cost, color = "orange", marker = "o", label = "Average Cost")
		line2 = axis.scatter(supply, percentile_95, color = "magenta", marker = "o", label = "95th Percentile")
		line3 = axis.scatter(supply, percentile_5, color = "green", marker = "o", label = "5th Percentile")
		axis.set_ylim(0,1000000)
		axis.set_title("Stock vs Average Cost")
		axis.set_xlabel("Stock") 
		axis.set_ylabel("Average Cost($)")
		axis.legend([line1, line2, line3], ['Average Cost', "95th Percentile", "5th Percentile" ])
		plt.show()
		fig.savefig("Stock vs Average Cost.png")

	def minimize_cost(self, supply_minimum, supply_maximum, iterations = 10000 ):
		supply = []
		average_cost = []
		dyn_cost = []
		percentile_95 = []
		percentile_5 = []
		for i in range(supply_minimum, supply_maximum+1, 50):
			x = i
			supply.append(x)
			j = 0
			cost_sum = 0
			dyn_cost = []
			while j <= iterations:
				it_cost = self.calc_cost(x,self.hist_demand(self.historical_data),self.unit_expiration_cost, self.unit_air_freight_cost)
				cost_sum += it_cost
				j += 1
				dyn_cost.append(it_cost)
			percentile_95.append(self.find_percentile(dyn_cost,95))
			percentile_5.append(self.find_percentile(dyn_cost, 5))
			average_cost.append(cost_sum/j)
		self.plot_optimal_supply(average_cost, percentile_95, percentile_5, supply)

if __name__ == "__main__":
    r = supply_stock(50, 150, Historical_Data)
    print(r.minimize_cost(4000, 8000, iterations=10000))




