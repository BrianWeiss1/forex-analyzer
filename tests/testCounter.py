import os

def get_counter():
    counter_file_path = "documents/counter.txt"

    if os.path.exists(counter_file_path):
        with open(counter_file_path, 'r') as file:
            counter = int(file.read())
    else:
        counter = 1

    return counter

def update_counter(counter):
    counter_file_path = "documents/counter.txt"

    with open(counter_file_path, 'w') as file:
        file.write(str(counter + 1))
def run():
    current_counter = get_counter()
    print(f"== Testing {current_counter} ==\n")
    update_counter(current_counter)
