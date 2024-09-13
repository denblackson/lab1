import time


def read_numbers_from_file(filename):
        with open(filename, 'r') as file:
            numbers = file.read().strip().split()
        return [int(number) for number in numbers]


def advanced_gcd(x, y):
        d = 1
        while x % 2 == 0 and y % 2 == 0:
            x //= 2
            y //= 2
            d *= 2

        u, v = x, y
        A, B, C, D = 1, 0, 0, 1

        while u != 0:
            while u % 2 == 0:
                u //= 2
                if A % 2 == 0 and B % 2 == 0:
                    A //= 2
                    B //= 2
                else:
                    A = (A + y) // 2
                    B = (B - x) // 2

            while v % 2 == 0:
                v //= 2
                if C % 2 == 0 and D % 2 == 0:
                    C //= 2
                    D //= 2
                else:
                    C = (C + y) // 2
                    D = (D - x) // 2

            if u >= v:
                u = u - v
                A = A - C
                B = B - D
            else:
                v = v - u
                C = C - A
                D = D - B

        return d * v

def find_gcd(*numbers):
    if len(numbers) == 0:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = advanced_gcd(result, num)
        if result == 1:
            break
    return result


files = ["Numbers_1000.txt", "Numbers_10000.txt", "Numbers_100000.txt"]


for file in files:
    numbers_from_file = read_numbers_from_file(file)
    print(f"Кількість змінних для обрахунку НСД: {len(numbers_from_file)}")
    start_time = time.perf_counter()
    result = find_gcd(*numbers_from_file)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1e3
    print(f"GCD: {result}")
    print(f"Час виконання: {execution_time:.6f} ms")