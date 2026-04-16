# ------------------------------------------------------------
# 6. TYPE CONVERSION
# ------------------------------------------------------------
# Sometimes we need to convert one type to another.
print("\n=== 6. TYPE CONVERSION ===")
num_text = "25"
num_value = int(num_text)   # converting string to integer
print("String value:", num_text, "| Type:", type(num_text))
print("Converted value:", num_value, "| Type:", type(num_value))

float_text = "12.5"
float_value = float(float_text)  # converting string to float
print("Converted float:", float_value, "| Type:", type(float_value))