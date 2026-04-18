# boolean and operators
like_coding = True
like_tea = False
favorite_food = "pizza"
favorite_number = 42

print(type(like_coding))
print(type(favorite_food))
print(type(favorite_number))


# we have six comparison operators in python
# 1. Equal to (==)
print(1 == 2)  # False
print(1 == 1)  # True

# 2. Not equal to (!=)
print(1 != 2)  # True
print(1 != 1)  # False

# 3. Greater than (>)
print(3 > 2)  # True
print(2 > 3)  # False

# 4. Less than (<)
print(2 < 3)  # True
print(3 < 2)  # False

# 5. Greater than or equal to (>=)
print(3 >= 2)  # True
print(2 >= 3)  # False

# 6. Less than or equal to (<=)
print(2 <= 3)  # True
print(3 <= 2)  # False

# logical operators
# 1. and
print(True and True)  # True
print(True and False)  # False

# 2. or
print(True or False)  # True
print(False or False)  # False

# 3. not
print(not True)  # False
print(not False)  # True

# operator precedence
print(1 + 2 * 3)  # 7
print((1 + 2) * 3)  # 9

#  ! and ~ are also logical operators but they are used for bitwise operations and not for boolean operations.
# ! is used for logical negation and ~ is used for bitwise negation.