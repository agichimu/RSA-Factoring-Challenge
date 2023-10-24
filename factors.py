import sys

def factorize_number(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def main(input_file):
    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()

        for number in numbers:
            n = int(number)
            factors = factorize_number(n)
            factorization = f"{n}={'*'.join(map(str, factors))}"
            print(factorization)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python factors.py <input_file>")
        sys.exit(1)

    input_file = "alex_numbers.txt" 
    main(input_file)
