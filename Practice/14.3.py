def taxi_cost(km, cost_km, start_price):
    total_cost = start_price + km * cost_km
    return total_cost

print(taxi_cost(10,2,5))
print(taxi_cost(1,2,5))

