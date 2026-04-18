# A function is a reusable block of code.

def greet(first_name, last_name):
    """This function greets the given person."""
    print("Hello,", first_name, last_name)

greet("Charlie", "Brown")


def my_function():
    print("Inside my function")

my_function()


'''
    And scope is a way for us to define global variables versus internal variables.
    And internal variables are also known as local variables.
'''
def print_color_red():
    color = "red"
    print("Inside function, color:", color)

color = "BLue"
print(color)
print_color_red()

def print_number(lowest_number, highest_number):
    print("Lowest number:", lowest_number)
    print("Highest number:", highest_number)

print_number(highest_number = 10, lowest_number=1)



def add_numbers(num1, num2):
    """This function returns the sum of two numbers."""
    return num1 + num2

sum_result = add_numbers(5, 7)
print("Sum:", sum_result)


def print_list(list_of_items):
    for x in list_of_items:
        print(x)

number_list = [1, 2, 3, 4, 5]
list_of_colors = ["red", "green", "blue"]
print("Number list:",number_list)
print("List of colors:",list_of_colors)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    currnet_tax_rate = 0.03
    return cost_of_item * currnet_tax_rate


final_cost = buy_item(100)
print("Final cost of item:", final_cost)