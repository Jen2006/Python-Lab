# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing elements of a tuple
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Slicing a tuple
print("Slice from index 1 to 2:", my_tuple[1:3])

# Checking if an item exists in a tuple
if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple")

# Iterating through a tuple
for item in my_tuple:
    print("Item:", item)

# Length of a tuple
print("Length of the tuple:", len(my_tuple))

# Concatenation of tuples
new_tuple = my_tuple + ("orange", "grape")
print("Concatenated tuple:", new_tuple)

# Tuple unpacking
a, b, c = my_tuple
print("Unpacked values:", a, b, c)

# Nested tuples
nested_tuple = (my_tuple, ("x", "y", "z"))
print("Nested tuple:", nested_tuple)