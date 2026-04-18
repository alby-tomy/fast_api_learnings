# ------------------------------------------------------------
# 10. LOOPS
# ------------------------------------------------------------
# Loops repeat code.
print("\n=== 10. LOOPS ===")

# while loop
print("While loop example:")
count_num = 1
while count_num <= 3:
    print("Count:", count_num)
    count_num += 1

# for loop with range()
print("For loop example:")
for number in range(1, 4):
    print("Number:", number)


my_list = [1,2,3,4,5,6]
ttl = 0
for n in my_list:
    ttl += n
print("Total of my_list:", ttl)
