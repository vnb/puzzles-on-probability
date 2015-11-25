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

def hist_demand(historical_data):
	""" This function generates random demand values from historical Historical_Data """
	max_value = len(historical_data)
	x = random.randint(0,max_value-1)
	return historical_data[x] 

avg_cost = []
amt_stocked = []
usr_demand = []


def calc_cost(supply, demand, unit_cost_expiration, unit_cost_restock):
	if supply == demand:
		return 0
	elif supply >  demand:
		return unit_cost_expiration*(supply-demand)
	else:
		return unit_cost_restock*(demand-supply)

def find_percentile(parameter, p): 
	r = p*0.01*(len(parameter)+1)
	parameter.sort()
        if r>int(r):
            return (r-int(r))*(parameter[int(r)]-parameter[int(r)-1])+parameter[int(r)-1]
        else:
            return parameter[int(r)-1]

for i in range(0, 10000):
 	x = random.randint(4000,8001)
 	amt_stocked.append(x)
 	demnd = hist_demand(Historical_Data)
 	usr_demand.append(demnd)
 	avg_cost.append(calc_cost(x,demnd,50,150))
ya = []
za = []
dyn_cost = []
ra = []
na = []
for i in range(4000, 8001, 50):
	x = i
	ya.append(x)
	j = 0
	cost_sum = 0
	dyn_cost = []
	while j <= 10000:
		it_cost = calc_cost(x,hist_demand(Historical_Data),50,150)
		cost_sum += it_cost
		j += 1
		dyn_cost.append(it_cost)
	ra.append(find_percentile(dyn_cost,95))
	na.append(find_percentile(dyn_cost, 5))
	za.append(cost_sum/j)


fig = plt.figure(figsize = (10, 10))
axis = fig.add_subplot(1, 1, 1)
line1 = axis.scatter(ya, za, color = "orange", marker = "o", label = "Average Cost")
line2 = axis.scatter(ya, ra, color = "magenta", marker = "o", label = "95th Percentile")
line3 = axis.scatter(ya, na, color = "green", marker = "o", label = "5th Percentile")
axis.set_ylim(0,1000000)
axis.set_title("Stock vs Average Cost")
axis.set_xlabel("Stock") 
axis.set_ylabel("Average Cost($)")
axis.legend([line1, line2, line3], ['Average Cost', "95th Percentile", "5th Percentile" ])
plt.show()
fig.savefig("Stock vs Average Cost.png")
