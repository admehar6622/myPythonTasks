import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download the punkt tokenizer data

# Specify the absolute path to the file
file_path = 'new.txt'

# Open the file and read its content
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the words
    tokens = word_tokenize(text)

    # Print the tokens
    print(tokens)

except FileNotFoundError:
    print(f"File not found at: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

