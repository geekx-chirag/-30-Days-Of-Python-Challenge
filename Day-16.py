# Its the sum of the previous two numbers
def avengers_power_levels(n):                   
    a, b = 0, 1
    for _ in range(n):
        yield f"Avenger power level: {a}"
        a, b = b, a + b

n = 9  
for power in avengers_power_levels(n):
    print(power)