def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

x = 2.0
toleransi = 0.00001

print("Metode Newton-Raphson")
print("---------------------")

for i in range(10):

    x_baru = x - f(x)/df(x)

    error = abs((x_baru - x)/x_baru)

    print(
        "Iterasi",
        i+1,
        ": x =",
        round(x_baru,6),
        "Error =",
        round(error,8)
    )

    if error < toleransi:
        break

    x = x_baru

print("\nAkar Persamaan =", round(x_baru,6))