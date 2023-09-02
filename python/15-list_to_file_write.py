def add_list_content_to_file(file_path, content_list):
    with open(file_path, 'a') as file:
        for item in content_list:
            file.write(str(item) + '\n')

file_path = input("enter the file path:")  # Replace with the actual file path
content_list = ['item1', 'item2', 'item3']  # Replace with your list

add_list_content_to_file(file_path, content_list)