import math
import matplotlib.pyplot as plt

def analytic_solution(x):
	y = 5 * math.exp(3 * x)
	return y 


start, end = 0, 3
step = 0.001

number_points = int((end - start) / step)

x_values = [start]
analytic_soluton_values = [analytic_solution(start)]

for index_point in range(1, number_points):
	current_x_value = start + index_point * step
	current_analytic_solution_value = analytic_solution(current_x_value)

	x_values.append(current_x_value)
	analytic_soluton_values.append(current_analytic_solution_value)


plt.figure(figsize=(15,6))
plt.plot(x_values, analytic_soluton_values)
plt.show()