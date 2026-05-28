import time

u = [
    "U     U",
    "U     U",
    "U     U",
    "U     U",
    " UUUUU "
]

a = [
    "   A   ",
    "  A A  ",
    " A___A ",
    "A     A",
    "A     A"
]

b = [
    "BBBBBB ",
    "B     B",
    "BBBBBB ",
    "B     B",
    "BBBBBB "
]

for i in range(5):
    print(u[i] + "   " + a[i] + "   " + b[i])
    time.sleep(0.5)