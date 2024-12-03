import re

instructions = []
result = 0
first_digit = 0
second_digit = 0
digit_index = 1
mul_enabled = True  # Track whether mul instructions are enabled or disabled

def parse_mul(expression):
    global instructions, result, first_digit, second_digit, digit_index, mul_enabled
    # Use regex to find valid 'mul(X,Y)', 'do()', and 'don't()' patterns
    matches = re.finditer(r'(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))', expression)
    
    for match in matches:
        if match.group(2) and match.group(3):  # Handle 'mul(X,Y)'
            if mul_enabled:
                first_digit = int(match.group(2))
                second_digit = int(match.group(3))
                product = first_digit * second_digit
                result += product
                print(f"Parsed: mul({first_digit},{second_digit})")
                print(f"First digit: {first_digit}")
                print(f"Second digit: {second_digit}")
                print(f"Product: {product}")
        elif match.group(4):  # Handle 'do()'
            mul_enabled = True
            print("Parsed: do() - mul instructions enabled")
        elif match.group(5):  # Handle "don't()"
            mul_enabled = False
            print("Parsed: don't() - mul instructions disabled")
    
    # Reset variables
    first_digit = 0
    second_digit = 0
    digit_index = 1

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        parse_mul(content)

# Example usage
file_path = 'input/input01.txt'  # Replace with your file path
parse_file(file_path)
print("Total Result:", result)