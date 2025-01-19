def replace_spaces_with_newlines(text):
    # Replace '|' with '","' and remove spaces
    text = text.replace(' ', ', ')
    
    return text

def process_file(input_file_path, output_file_path):
    # Read text from the input file
    with open(input_file_path, 'r') as file:
        text = file.read()
    
    # Replace spaces with newlines
    modified_text = replace_spaces_with_newlines(text)
    
    # Write the modified text to the output file
    with open(output_file_path, 'w') as file:
        file.write(modified_text)

if __name__ == "__main__":
    # Define the input and output file paths
    input_file_path = "input.txt"
    output_file_path = "output.txt"
    
    # Process the file
    process_file(input_file_path, output_file_path)
    print(f"Processed file '{input_file_path}' and saved result to '{output_file_path}'")
 