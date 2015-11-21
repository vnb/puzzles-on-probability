""" HealthCeuticals sells an antibioics which has no seasonality in demand.Avg demand is 5,000 units. 
Expiration cost - $50/unit, Air Frieght(in case of extra supply) - 150$. 
When Demand = Stocked, operating cost is 0. 
Historical Data		
10000,6000,10000,8000,7000,5000,5000,5000,3000,2000,6000,5000,6000,3000,5000,4000,5000,4000,4000,3000,3000,3000,4000,3000,8000,3000,5000,2000,4000,5000,7000,6000,7000,8000,1000,5000
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
		Historical_Data.append(row[1])

file_name = 'HealthCeuticals.csv'
file_select = open(file_name)
data = csv.reader(file_select)


for row in data:
	print(row)
	if row[0] == "Expiration Cost":
		expiration_cost = row[1]
	if row[0] == "Air Freight":
		air_freight = row[1]	
print(expiration_cost, air_freight)

print(Historical_Data)
def demand(historical_data):
	""" This function generates random demand values from historical Historical_Data """
	demand_rand = []
	min_value = 0
	max_value = len(historical_data)
	for i in range(1, max_value):
		j = random.randint(0, max_value-1)
		demand_rand.append(historical_data[j])
	return demand_rand 
# #Need to write exception when historical_data is empty, duration is empty

def avg_demand(rand_demand):
	sum_demand = 0
	for demand in rand_demand:
		sum_demand += int(demand)
	return int(sum_demand/len(rand_demand)
random_demand = demand(Historical_Data)



print(random_demand)
print(avg_demand(random_demand))

# cost = []
# amt_stocked = []
# usr_demand = []
# ##Amount Stocked
# for i in range(min(Historical_Data), max(Historical_Data)):
# 	demnd = avg_demand(demand(Historical_Data))
# 	amt_stocked.append(i)
# 	usr_demand.append(demand)

# 	if i == demnd:
# 		cost.append(0)
# 	elif i > demnd:
# 		cost.append((i-demnd)*50)
# 	else:
# 		cost.append((demnd-i)*150)
# print(cost,amt_stocked,usr_demand)

