# Week 2 Assignment - Python Lists Practice

# Step 1: Create an empty list called my_list
my_list = []  # Right now, my_list has no items

# Step 2: Append the following elements to my_list: 10, 20, 30, 40
# append() adds an item to the end of the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position in the list
# The index starts at 0, so index 1 means the second position
my_list.insert(1, 15)

# Step 4: Extend my_list with another list: [50, 60, 70]
# extend() adds multiple items from another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from my_list
# pop() without an index removes the last element
my_list.pop()

# Step 6: Sort my_list in ascending order (smallest to largest)
# sort() changes the list order permanently
my_list.sort()

# Step 7: Find and print the index of the value 30 in my_list
# index() returns the position of the first matching value
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Extra: Print the final list so we can see the result
print("Final list after all operations:", my_list)