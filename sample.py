from polynomial import Polynomial
import random
interval = (-9,9)

m = 10
polynomials = [Polynomial(*[random.randint(*interval) for _ in range(i)]) for i in range(1,m+1)]

print(29*"=" + " PRINT 10 POLYNOMIALS " + 29*"=")
for i, poly in enumerate(polynomials):
    print(f"P{i+1} =",poly)

print("\n}-=:<[ACTIVE EASTER EGG]>:=-{")
Polynomial.easteregg()
for i, poly in enumerate(polynomials):
    print(f"P{i+1} =",poly)


...
