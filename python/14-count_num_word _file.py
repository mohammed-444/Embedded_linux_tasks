def count_words(file_path):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

file_path = 'path/to/your/file.txt'  # Replace with the actual file path
word_count = count_words(file_path)
print(f"The file '{file_path}' contains {word_count} words.")