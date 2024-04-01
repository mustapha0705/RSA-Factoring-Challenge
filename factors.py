import sys

def factorize(number):
    factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            if factors:
                for factor_pair in factors:
                    print(f"{number}={factor_pair[0]}*{factor_pair[1]}")
