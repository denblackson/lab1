from FileWorker import FileWorker
from GCD import GCD

gcd_worker = GCD()
file_worker = FileWorker()

file_worker.create_and_fill_file('numbers.txt', 10000)
numbers_from_file = file_worker.read_numbers_from_file('numbers.txt')

result = gcd_worker.find_gcd(*numbers_from_file)
print(f"GCD: {result}")