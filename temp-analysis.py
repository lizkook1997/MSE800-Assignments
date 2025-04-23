import numpy as np

temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Average temperature
average_temp = np.mean(temperatures)
print("Average Temperature (°C):", average_temp)

# 2. Highest and Lowest temperature
highest = np.max(temperatures)
lowest = np.min(temperatures)
print("Highest Temperature (°C):", highest)
print("Lowest Temperature (°C):", lowest)

# 3. Convert to Fahrenheit
fahrenheit = temperatures * 9 / 5 + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# 4. Days where temp > 20°C
above_20 = np.where(temperatures > 20)
print("Days (indexes) with temp > 20°C:", above_20[0])
