def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count

file_path = input("enter the path :")   # Replace with the actual file path
line_count = count_lines(file_path)
print(f"The file '{file_path}' contains {line_count} lines.")