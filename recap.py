# 1) Numerical Derivative Finder
def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def take_square(x):
    return x ** 2

# take_square ile test (x = 3 için türev 2*x = 6 çıkmalı)
print("take_square ile türev:", estimate_derivative(take_square, 3))

# lambda fonksiyonu ile aynı test
square_lambda = lambda x: x ** 2
print("lambda ile türev:", estimate_derivative(square_lambda, 3))