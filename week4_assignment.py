# Error Handling Lab 🧪
# A program that asks the user for a filename and handles errors gracefully

# Ask the user to enter a filename
filename = input("Enter the name of the file you want to read: ")

try:
    # Try to open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("\n✅ File read successfully!\n")
        print("File content:\n")
        print(content)

except FileNotFoundError:
    # This runs if the file does not exist
    print("❌ Error: The file you entered was not found. Please check the name and try again.")

except PermissionError:
    # This runs if you don’t have permission to read the file
    print("❌ Error: You don’t have permission to access this file.")

except Exception as e:
    # This handles any other unexpected error
    print(f"❌ An unexpected error occurred: {e}")