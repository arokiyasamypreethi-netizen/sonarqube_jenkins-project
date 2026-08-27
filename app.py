import sys  # unused import -> Sonar will flag this as a code smell


def calculate_total(a, b):
    total = a + b
    return total


def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average


def get_db_password():
    # Hardcoded credential -> Sonar will flag this as a security hotspot
    password = "admin123"
    return password


def divide(a, b):
    return a / b  # no zero-check -> Sonar may flag potential bug


def unused_calculation():
    x = 10
    y = 20
    z = x + y  # z is never used -> Sonar will flag this


if __name__ == "__main__":
    print(calculate_total(5, 10))
    print(calculate_average([1, 2, 3, 4, 5]))
