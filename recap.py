import math

# 1) Numerical Derivative Finder
def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def take_square(x):
    return x ** 2

print("take_square ile türev:", estimate_derivative(take_square, 3))
square_lambda = lambda x: x ** 2
print("lambda ile türev:", estimate_derivative(square_lambda, 3))


# 2) Riemann Sum Integrator
def integrate(func, steps=1000):
    total_area = 0.0
    dx = 1 / steps
    for i in range(steps):
        x_i = (i + 0.5) * dx
        total_area += func(x_i) * dx
    return total_area

print("Riemann integrali (x^2, 0'dan 1'e):", integrate(take_square, 1000))


# 3) Do-Twice Function
def f_x_twice(x, f_x):
    return f_x(f_x(x))

print("f_x_twice(16, sqrt):", f_x_twice(16, math.sqrt))
print("f_x_twice(2, lambda x: x**2):", f_x_twice(2, lambda x: x ** 2))