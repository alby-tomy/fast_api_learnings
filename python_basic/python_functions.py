# ------------------------------------------------------------
# 11. FUNCTIONS
# ------------------------------------------------------------
# A function is a reusable block of code.
print("\n=== 11. FUNCTIONS ===")

def greet(person_name):
    """This function greets the given person."""
    print("Hello,", person_name)


greet("Charlie")


def add_numbers(num1, num2):
    """This function returns the sum of two numbers."""
    return num1 + num2

sum_result = add_numbers(5, 7)
print("Sum:", sum_result)