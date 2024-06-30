# Python Code Documentation Generator

This project is a Python script designed to generate documentation for Python files within a specified directory. It leverages the Groq API to automatically add comments to the code without modifying its functionality or syntax.

## Features

- **Directory Traversal**: Recursively traverses through directories to find Python files.
- **Automated Documentation**: Uses the Groq API to generate comments for Python code.
- **Environment Configuration**: Utilizes `dotenv` for loading environment variables.

## Requirements

- Python 3.6+
- `groq`
- `httpx`
- `dotenv`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/python-doc-generator.git
   cd python-doc-generator```
   
2. **Install the required packages:**

   ```bash
    pip install groq httpx python-dotenv```
   
3. **Set up your environment variables:**\
    Create a .env file in the root directory of your project and add your Groq API key:

    ```plaintext
    GROQ_API_KEY=your_api_key_here```

## Usage

1. **Run the script:**

    ```bash
    python document_generator.py```

2. **Enter the directory path:**

    When prompted, enter the path to the directory containing the Python files you want to document.

3. **View the results:**

    The script will traverse the directory, document each Python file, and overwrite them with the commented versions.

# Example
    ```plaintext
    $ python document_generator.py
    Enter the directory path: /path/to/your/python/files
    Generating docs...
    example.py documented
    another_example.py documented

    ```

# Acknowledgments
    Groq for the API.
    httpx for the HTTP library.
    dotenv for environment variable management