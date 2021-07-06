names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0,
                             3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0,
                          3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost_2 = 0
cont = len(actual_insurance_costs)
pos = 0
while pos < cont:
  total_cost_2 += actual_insurance_costs[pos]
  pos += 1

print(total_cost_2)

total_cost = 0
for x in actual_insurance_costs:
    total_cost += x
print(total_cost)
