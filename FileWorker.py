import random


class FileWorker:
    @staticmethod
    def read_numbers_from_file(filename):
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
        return numbers

    @staticmethod
    def create_and_fill_file(filename, count, min_value=1, max_value=100, base = random.randint(1, 1000)):
        with open(filename, 'w') as file:
            for _ in range(count):
                file.write(f"{base * random.randint(min_value, max_value)}\n")
