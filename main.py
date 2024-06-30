from groq import Groq
from httpx import ConnectError
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# Define the client with the given API key
client = Groq(
    api_key=dotenv_values(".env")['GROQ_API_KEY']
)

# Initialize a flag to track whether a prompt is awaiting a response
prompt_awaiting_response: bool = False

def generate_documentation(directory):
    # Start generating the docs
    print("Generating docs...")
    # Check if the directory exists
    if not os.path.isdir(directory):
        # If it doesn't exist, print an error message and return
        print(f"The directory {directory} does not exist.")
        return

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            # Print the file name
            print(file)
            if str(file).endswith(".py"):
                # If the file is a Python file, document it
                file_path = os.path.join(root, file)
                document_file(file_path)

def document_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read the contents of the file
        code = f.read()

    # Use the client to generate documentation for the file
    documentation = client.chat.completions.create(messages=[
            {"role": "user", "content": code },
            {"role": "system", "content": "Your goal is to add ONLY comments to the code provided. Do not modify the functionality OR SYNTAX of the code. ONLY RETURN THE CODE WITH THE COMMENTS IN PYTHON COMMAND SYNTAX, NO OTHER TEXT LIKE 'HERE IS THE CODE' or 'I'M SORRY' "}
    ], model="llama3-8b-8192")

    # Write the documentation to a file
    with open(file_path, 'w') as doc_file:
        # Get the first choice from the documentation
        docs = documentation.choices[0].message.content.replace('', '')
        # Write the documentation to the file
        doc_file.write(docs)
    # Print a success message
    print(f"{file_path} documented")

# Main function to get the directory path from the user
if __name__ == "__main__":
    # Ask the user for the directory path
    directory = input("Enter the directory path: ")
    # Generate the documentation for the directory
    generate_documentation(directory)

