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
    print(f"\nGiven String: {statement}")
    count = 0


# Iterate over the indices of the statement
    for i in range(len(statement) - len(substring) + 1):
# Check if the substring matches the segment of the statement
        count += statement[i:i + len(substring)] == substring
      
# Return the count of occurrences
    return count


# Count occurrences of 'Emma'
count_emma_result = count_substring("Emma is a good developer. Emma is a musician, she seamlessly combines technical expertise with artistic brilliance.", "Emma")
print("Emma appeared", count_emma_result, "times")


# Count occurrences of 'emma' (case-insensitive)
count_emma_insensitive_result = count_substring("emma is good developer. emma is a writer".lower(), "emma")
print("emma appeared", count_emma_insensitive_result, "times")

# Combining both counts
combined_count = count_emma_result + count_emma_insensitive_result
print("\nTotal occurrences of 'Emma' and 'emma':", combined_count)
