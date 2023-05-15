'''
Reggie is a mad scientist who has been hired by the local fast food joint to build their newest ball pit
in the play area. As such, he is working on researching the bounciness of different balls so as to 
optimize the pit. He is running an experiment to bounce different sizes of bouncy balls, and then fitting 
lines to the data points he records. He has heard of linear regression, but needs your help to implement
a version of linear regression in Python.'''

'''
Linear Regression is when you have a group of points on a graph, and you find a line that approximately 
resembles that group of points. A good Linear Regression algorithm minimizes the error, or the distance 
from each point to the line. A line with the least error is the line that fits the data the best. 
We call this a line of best fit.

In this project, you’ll combine your knowledge of loops, lists, and arithmetic to create a function 
that will find a line of best fit when given a set of data.
'''


# Task 1
# Write your get_y() function here
def get_y(m, b, x):
    y = m * x + b
    return y


# Uncomment each print() statement to check your work. Each of the following should print True
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# Tasks 2 and 3
# Write your calculate_error() function here
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y_line = get_y(m, b, x_point)
    difference = abs(y_line - y_point)
    return difference

# Task 4
# Uncomment each print() statement and check the output against the expected result

# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
# print(calculate_error(1, 0, (3, 3)))

# the point (3, 4) should be 1 unit away from the line y = x:
# print(calculate_error(1, 0, (3, 4)))

# the point (3, 3) should be 1 unit away from the line y = x - 1:
# print(calculate_error(1, -1, (3, 3)))

# the point (3, 3) should be 5 units away from the line y = -x + 1:
# print(calculate_error(-1, 1, (3, 3)))


# Task 5
# Write your calculate_all_error() function here
def calculate_all_error(m, b, points):
    error = 0
    for point in points:
        error += calculate_error(m, b, point)

    return error


# Task 6
# Uncomment each print() statement and check the output against the expected result
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

# every point in this dataset lies upon y=x, so the total error should be zero:
# print(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
# print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
# print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
# print(calculate_all_error(-1, 1, datapoints))


# Tasks 8 and 9
possible_ms = [round(x*0.1, 1) for x in range(-100, 101, 1)]
possible_bs = [round(x*0.1, 1) for x in range(-200, 201, 1)]

# Task 10
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float('inf')
best_m = 0
best_b = 0


# Tasks 11 and 12
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_m)
print(best_b)
print(smallest_error)

print(get_y(0.4, 1.6, 6))


# Task 13
