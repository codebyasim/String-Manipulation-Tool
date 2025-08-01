# Prompt the user to enter a string and store it in 'input_string'
input_string = input("Enter a string: ")

# Display a menu of string manipulation options to the user
print("\nString Manipulation Menu:")
print("1. Convert to uppercase")   # Option 1: Convert string to uppercase
print("2. Convert to lowercase")   # Option 2: Convert string to lowercase
print("3. Slice the string")       # Option 3: Extract a substring from the string
print("4. Calculate string length")# Option 4: Find the length of the string
print("5. Loop through characters")# Option 5: Print each character in the string on a new line

# Ask the user to choose an option by entering a number between 1 and 5
choice = int(input("Enter your choice (1-5): "))

# Perform the operation based on the user's choice
if choice == 1:
    # Convert the entire string to uppercase letters and print the result
    result = input_string.upper()
    print("Uppercase:", result)

elif choice == 2:
    # Convert the entire string to lowercase letters and print the result
    result = input_string.lower()
    print("Lowercase:", result)

elif choice == 3:
    # Prompt the user to enter the start and end indices for slicing the string
    start = int(input("Enter start index: "))
    end = int(input("Enter end index: "))
    # Extract and print the substring from 'start' up to but not including 'end'
    result = input_string[start:end]
    print("Sliced string:", result)

elif choice == 4:
    # Calculate and print the number of characters in the string
    length = len(input_string)
    print("String length:", length)

elif choice == 5:
    # Loop through each character in the string and print it on a separate line
    print("Characters:")
    for char in input_string:
        print(char)

else:
    # If the user enters a number outside 1-5, print an error message
    print("Invalid choice.")
