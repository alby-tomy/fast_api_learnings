"""
    Process and return a tuple of items.
    
    A tuple is an immutable, ordered collection of elements in Python.
    Unlike lists, tuples cannot be modified after creation (no adding,
    removing, or changing elements). Tuples are commonly used for:
    - Returning multiple values from a function
    - Using as dictionary keys (since they're immutable)
    - Protecting data from accidental modification
    - Slightly better performance compared to lists
    
    Args:
        items (tuple): An immutable sequence of elements that can contain
                      any data types (integers, strings, objects, etc.).
    
    Returns:
        tuple: A tuple containing the processed items.
"""

my_tuple = (1, 2, 3, "hello", 4.5)
print("My tuple:", my_tuple)

# length of tuple
print("Length of tuple:", len(my_tuple))

# accessing tuple elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])