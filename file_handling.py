# Open the input file for reading
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("Modified content has been saved to output.txt.")

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")