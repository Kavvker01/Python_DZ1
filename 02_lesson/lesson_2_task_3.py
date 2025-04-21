import math

def square(s1):
    return math.ceil(s1*s1)


side = int(input("Введите длину квадрата: "))
print(f"Площадь квадрата: {square(side)}")