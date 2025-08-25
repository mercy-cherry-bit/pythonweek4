def modify_text(text):
    """
    Example modification: convert the text to uppercase.
    You can change this logic (e.g., replace words, reverse lines)
    """
    return text.upper()


def main():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Open and read the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content
        modified_content = modify_text(content)

        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File processed successfully. Modified version saved as {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if _name_ == "_main_":
    main()