# Toby Wright 2023
# The first algorithm introduced in the art of computer programmin volume 1
import random

def euclids_algo(num1: int, num2: int) -> int:
    if num1 < num2:
        num1, num2 = num2, num1
    remainder: int = num1 % num2
    print(f"{num1} // {num2} == {remainder}")
    if remainder != 0:
        return euclids_algo(num2, remainder)
    return num2

if __name__ == "__main__":
    num1, num2 = random.randint(10, 500000), random.randint(10, 500000)  
    num1 = 2166
    num2 = 6099
    highest_common_divisor = euclids_algo(num1, num2)
    print(f"Highest common divisor == {highest_common_divisor}")
