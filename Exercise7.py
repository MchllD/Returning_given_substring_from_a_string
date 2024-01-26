# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

# pseudocode


# Function to count occurrences of a substring in a given string
# Iterate over the indices of the statement
# Check if the substring matches the segment of the statement
# Return the count of occurrences
# Count occurrences of 'Emma'
# Count occurrences of 'emma' (case-insensitive)
# Combine the counts of 'Emma' and 'emma'

# *************************************** actual code *****************************************


# Function to count occurrences of a substring in a given string
def count_substring(statement, substring):
    print(f"Given String: {statement}")
    count = 0


# Iterate over the indices of the statement
    for i in range(len(statement) - len(substring) + 1):
# Check if the substring matches the segment of the statement
        count += statement[i:i + len(substring)] == substring
      
# Return the count of occurrences
    return count
# Count occurrences of 'Emma'
# Count occurrences of 'emma' (case-insensitive)
# Combine the counts of 'Emma' and 'emma'