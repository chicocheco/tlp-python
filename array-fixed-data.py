NUM_CATEGORIES = 4

category_thresholds = [0.0, 50000.0, 150000.0, 500000.0]
license_cost = [50.0, 200.0, 1000.0, 5000.0]

gross_sales = 65.000

category = 0
while category < NUM_CATEGORIES and category_thresholds[category] <= gross_sales:
    category += 1

cost = license_cost[category - 1]
print(cost)
